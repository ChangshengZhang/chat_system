#coding=utf-8   
 
import socket  
import time  
import struct  
import tkFileDialog
import os  
import threading 
import hashlib
import traceback

import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

class FileTrans:
    def __init__(self,targetport=9356): 
        self.fileinfosize = 512   #文件信息最长256个字节，包含文件路径、文件名和文件大小
        self.targetport=targetport      #接收文件的服务程序监听的端口
        self.filerecvdict={}      #存放待接收的文件信息的任务字典，每次需要接收文件时只需往该字典中添加相关项即可
        
        self.filerecvdictlock=threading.Lock()#保护filerecvdict的锁
        
        self.serversock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#创建tcp连接   
        self.serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serversock.bind(('',self.targetport))#定于端口和ip   
        self.serversock.listen(5)#监听   
        
        self.FileRecvServerThread = threading.Thread(target=self.FileRecvServer,name="RecvServerThreading")
        self.FileRecvServerThread.setDaemon(1)  
        self.FileRecvServerThread.start()#执行线程

    def EncodeFileInfo(self,filepath):
    #从给定的文件路径获取文件信息并编码成用于发送的字符串
        fileinfo=""

        try:
            filepath.replace("\\","/") #路径标准化，用正斜杠替换所有反斜杠
            filepathlist=filepath.split("/")           
            filename=filepathlist[len(filepathlist)-1]#从路径中获取文件名
            print "EncodeFileinfo filename is",filename
            try:
                path=filepath
                print "EncodeFileinfo filepath is",filepath
                print path.decode("utf-8")
                print "size"
                filesize=os.stat(filepath.decode("utf-8")).st_size #获取文件大小 
                print "sizesuceess"
            except Exception,e:
                print "sizeerr"               
                print e
                info=sys.exc_info() 
                print info
                traceback.print_exc()
            print "EncodeFileinfo filesize is",filesize    
            filemd5=hashlib.md5(filename).hexdigest()     
            fileinfo=filepath+"&"+filename+"&"+str(filesize)+"&"+filemd5+"&"
            fileinfo=fileinfo.ljust(self.fileinfosize,"+")  
        finally:
            return fileinfo
    
    def DecodeFileInfo(self,fileinfo):
    #解码用于发送的文件信息字符串
        filepath=""
        filename=""
        filesize=""
        filemd5=""
        try: 
            fileinfo = fileinfo.split("&")
            filepath = fileinfo[0]
            filename = fileinfo[1]
            filesize = int(fileinfo[2]) 
            filemd5  = fileinfo[3] 
        finally:
            return filepath,filename,filesize,filemd5
            
    def SendFile(self,filepath,targetIp): 
    #向目标Ip发送文件路径指定的文件名，接收方所用端口号为类属性中的targetport
    #filepath:文件路径，字符串,包含文件绝对路径和文件名 
    #targetIp:目标Ip
        print"Sendfile filepath is",filepath
        fileinfo=self.EncodeFileInfo(filepath)
        filesocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
        filesocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        filesocket.settimeout(1)  
        #先发送文件信息并等待对方回应
        print "Send File fileinfo",fileinfo
        e=0  
        try:  
            filesocket.connect((targetIp,self.targetport))  
        except socket.timeout,e:  
            print 'timeout',e  
        except socket.error,e:  
            print 'error',e  
        except e:  
            print 'any',e  
        if not e:     
            try:
                filesocket.send(fileinfo)#发送文件基本信息数据   
                filetosend = open(filepath.decode("utf-8"),'rb')  
                while True:        #发送文件   
                    filedata = filetosend.read(1024)  
                    if not filedata:  
                        break  
                    filesocket.send(filedata)  
                print "sending over..."  
                filetosend.close()  
            except Exception,e:
                print "sending failed:",e
            
    def RecvFile(self,filesocket,filesavepath,filesize):
    #与SendFile对应，获得与SendFile相连的filesocket后，将接收文件存入指定路径中
    #filesocket：接收文件的socket，有接收文件的服务程序提供
    #filesavepath: 接收文件的保存路径，字符串，含绝对路径和文件名          
        while True:       
#             headsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
#             headsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#             headsocket.settimeout(1)  
#         
#             filesocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
#             filesocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#             filesocket.settimeout(1)  
            try:                  
                filetosave = open(filesavepath,'wb')#新建文件，并且准备写入   
                restsize = filesize
                print "recving..."  
                while True:  
#                   #每次接收1024个字节
                    filedata = filesocket.recv(1024)  
                    if not filedata and restsize<=0: 
                    #没有数据时，等待一秒检测是否有数据到达，还是没有就认为已经传输完毕
                        time.sleep(1)
                        filedata = filesocket.recv(1024) 
                        break  
                    filetosave.write(filedata)  
                    restsize -= 1024#计算剩余数据包大小   
                filetosave.close()  
                print "File receieve success!"
                break
            except socket,e:  
                print e
                print "Server error occur"
                filesocket.close()
                break  

    def FileRecvServer(self):
        while True:
            conn,(clintIp,clintPort)=self.serversock.accept()  
            print "Server get a connect"
            try:  
                fileinfo = conn.recv(self.fileinfosize)  
                print "fileinfo is:",fileinfo
                filepath,filename,filesize,filemd5=self.DecodeFileInfo(fileinfo)
                if not self.filerecvdict.has_key(filemd5):#检索要接收的文件是否存在于待接收文件列表中
                    print "filerecvdict is:",self.filerecvdict
                    print "md5 wanted is",filemd5
                    conn.close()#如果不在就关闭这个连接，不接收
                else:
                    self.filerecvdictlock.acquire()
                    filesavepath=self.filerecvdict.pop(filemd5) #否则从字典中得到这个文件要在本地存储的路径,并从任务字典中删去这一条
                    self.filerecvdictlock.release()
                    #然后执行一个线程以接收文件
                    RecvFileThread = threading.Thread(target=self.RecvFile,name=filename+"RecvThreading",args=(conn,filesavepath,filesize))  
                    RecvFileThread.start()#执行线程
            except :
                conn.close()
                continue
    
    def AddRecvFile(self,filemd5,filesavepath):
    #往存有接收文件信息的任务字典中增加新项
    #filemd5:对方发送文件的md5码，作为字典的key
    #filesavepath:要将对方发送的文件保存的本地路径，字符串 ，作为字典的value
        filesavepath.replace("\\","/")#路径标准化，使用正斜杠           
        self.filerecvdictlock.acquire()
        self.filerecvdict[filemd5]=filesavepath
        self.filerecvdictlock.release()           

                       
            
if __name__=="__main__":
    sendfilepath = tkFileDialog.askopenfilename(initialdir = 'T:/w.txt')        
    savefilepath =  tkFileDialog.askdirectory(initialdir = 'D:/')
    
    savefilepath.replace("\\","/") #用正斜杠替换所有反斜杠
    sendfilepath.replace("\\","/")
  
        
    filetrans=FileTrans()
    fileinfo=filetrans.EncodeFileInfo(sendfilepath)

    filepath,filename,filesize,filemd5=filetrans.DecodeFileInfo(fileinfo)
    filetrans.AddRecvFile(filemd5, savefilepath+"/"+filename)

    filetrans.SendFile(sendfilepath, "183.173.33.159")
    time.sleep(20)    
    print 'end' 


 

