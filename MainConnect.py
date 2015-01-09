#coding=utf-8

import socket
import threading
import time
import struct  
import copy
import collections
import os
import FileTrans
import sys
from FileTrans import FileTrans
from lib2to3.fixer_util import String
from PyQt4 import QtCore, QtGui
from VideoChat import MediaTrans

#import userMainWindow
reload(sys)
sys.setdefaultencoding('utf-8') 
    


class MainConnect(QtCore.QThread):   #主连接进程
    def __init__(self,username):    
        QtCore.QThread.__init__(self)
        self.username=username              #登录名
        self.friendinfo={}                  #好友信息，结构为{"好友IP"：”好友学号“}
        self.friendnum=0                    #在线好有人数
        self.mestodeal={}                   #记录消息的字典，字典的key为学号，Value为从该学号接收到的待处理消息的列表
        self.dealmes=False                  #是否有信息需要处理，为True时则需要处理
        
        self.islisten=True
        
        self.netserverport =8000
        self.netserverhost="166.111.180.60"
        self.serverport=9355
        #服务器端Socket
        self.sserver=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #客户端socket
        self.sclint=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sclint.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #用于接收信息的锁
        self.mesrecvlock=threading.Lock()     
        #更新好友信息的锁
        self.friendloadlock=threading.Lock() 
        #实现传输文件功能的类
        self.filetrans=FileTrans(9356)
        
        self.serverlistenthread=threading.Thread(target=self.ServerListen,name="ServerListenThread")
        self.serverlistenthread.setDaemon(1)
        self.ConnectInit()
        self.LoadFriend()
        self.serverlistenthread.start()     #一启动就会开始服务器的侦听

        #signal
        self.mssSignal = QtCore.SIGNAL("mssSignal")
        self.fileSignal = QtCore.SIGNAL("fileSignal")

        self.acceptFileSignal ="No"
        self.filePathSignal =""

        self.filesendeusername=""
        self.filesendinfo=""

        self.serverlistenthreadFile=threading.Thread(target=self.WaitForUser_FileTrans,name="WaitForUser_FileTransThread")
        self.serverlistenthreadFile.setDaemon(1)
        self.serverlistenthreadFile.start()

        self.mediatrans=MediaTrans(self.sclint)

        #app = QtGui.QApplication(sys.argv)
        #self.mainWindow = userMainWindow.UserMainWindow(self.username)
        #self.mainWindow.show()
    def setFilePath(self,acceptFileSignal,filePathSignal):
        self.acceptFileSignal = acceptFileSignal
        self.filePathSignal = filePathSignal

    def ConnectInit(self):                  #连接初始化
        tempbool=True    
        try :
            self.sserver.bind(('',self.serverport))
            self.sserver.listen(5)
            print "Create server successfully\n\r"
        except socket.error,e:
            print "Err:%s" %e
            print "Try to create server again\n\r"
        while True:                             #连接网络服务器
            try:
                self.sclint.connect((self.netserverhost,self.netserverport))
                print "Connect with net server successfully"
                self.sclint.sendall(self.username+"_net2014")
                feedback=self.sclint.recv(1024);
                if feedback.startswith("lol"):
                    break;
            except socket.error,e:
                print "Err:%s"%e
                print "Try to connect net server again\n\r"

    def ServerListen(self): #服务器端进程进行监听
        self.islisten=True
        
        while self.islisten:
            conn,(clintIp,clintPort)=self.sserver.accept()
            messagerecv=conn.recv(8096)
            self.mesrecvlock.acquire()
            try:
                if self.mestodeal.has_key(clintIp):
                    self.mestodeal[clintIp].append(messagerecv)
                else :
                    self.mestodeal[clintIp]=[]
                    self.mestodeal[clintIp].append(messagerecv)
                conn.sendall("get hi")          #发送响应表明接收成功
                conn.close()                           
            finally:
                self.mesrecvlock.release() 
            #处理信息的函数
            #  self.MessageDeal()
            c_mestodeal=copy.deepcopy(self.mestodeal)
            serverdealthread=threading.Thread(target=self.MessageDeal,name="ServerDealThread",args=(c_mestodeal,))
            serverdealthread.setDaemon(1)
            serverdealthread.start()
            self.mestodeal.clear()

            
    def MessageDeal(self,c_mestodeal):    #处理接收到信息的函数，每次服务器线程接到新的消息都会被调用，调用完毕后服务器新接收到的信息不再保留
    #self.mestodeal是一个字典，key为Ip，Value为收到的来自这个Ip的消息列表，是一个list，每个元素可以认为是该Ip发过来的一条消息              
    #所有消息格式如下为 消息类型:消息内容 ，其中消息类型固定长为3个字符，:为分隔符，消息内容是对方发送的真正消息
    #定义消息类型的代码：
    #mes表示正常的文本消息，可直接显示在对话框内
    #fsr表示文件传输的询问消息，即对方要想我方传输文件，消息内容固定长度为256个字符，格式为”文件路径&文件名&文件大小&冗余部分“
    #fss表示文件传输的允许消息，即我方向对方发送fsq后对方用fsr来回应我方，表示允许文件发送的操作，消息内容与对应的fsq相同
    #vdr表示视频会话的询问消息，预定义，暂没有提供相应函数处理
    #vds表示视频会话的允许消息
    #rdr表示语音会话的询问消息，预定义，暂没有提供相应函数处理
    #rds表示语音会话的允许消息
        for j in c_mestodeal.keys():           
                username = ""
                for k in c_mestodeal[j]: 
                    mestaype=k[:3]
                    mescontent=k[4:]
                    if self.friendinfo.has_key(j):
                        username=self.friendinfo[j]
                    else :
                        self.LoadFriend()
                        if  not self.friendinfo.has_key(j):    
                            print "Recieve a message for unknownuser" 
                                          
                    if not isinstance(username,str):
                        username=str(username)
                    print type(username)
                    
                    #此时mestaype中放有当前消息的类型
                    #mescontent中放有当前消息内容
                    if mestaype=="mes":#接收到文本消息
                        '''To Do:将以下改为收到新的聊天消息时需要执行的代码，比如在对应窗口上显示和刷新'''
                        
                        #self.mainWindow.receiveMessage(username,mescontent)
                        self.emit(self.mssSignal,username,mescontent)
                        print mescontent

                    elif mestaype=="qme":#收到群消息
                        mescontentlist=mescontent.split(":",1) 
                        qID=mescontentlist[0]
                        mescontent=mescontentlist[1]
                        print "qmes from:",username
                        print "qID:",qID
                        print mescontent
                    elif mestaype=="fsr":    
                        '''To Do:将以下改为收到对方的文件时需要执行的代码，比如在对应窗口上显示是否接收文件，并根据用户选择回复对方'''  
                        
                        #dlg = win32ui.CreateFileDialog(0)
                        #dlg.DoModal()
                        #savefilepath = dlg.GetPathName()   

                        '''执行下面一行后，filename为对方想发送的文件名，filesize为文件字节数,可以根据需要对用户显示'''
                        filepath,filename,filesize,filemd5=self.filetrans.DecodeFileInfo(mescontent)
                        
                        self.emit(self.fileSignal,username,filename,filesize)
                        self.filesendeusername= username
                        self.filesendinfo= mescontent

#                         print "fileinfo in fsr:",mescontent
                    elif mestaype=="fss":
                    #这个分支无需修改，接收到fss（发送允许）类型的消息后自动发送
                        print "get fss"
                        filepath,filename,filesize,filemd5=self.filetrans.DecodeFileInfo(mescontent)
                        print "fileinfo in fss:",mescontent
                        print "filepath in fss:",filepath
                        self.filetrans.SendFile(filepath, j)

                    elif mestaype=="chr":
                    #收到视频对话的询问信息
                        print "recieve chr"
                        self.SendMediaChatSure(username)
                        self.mediatrans.StartChatting(username)
                    elif mestaype=="chs":
                        if self.mediatrans.ischatting==False:
                            self.mediatrans.StartChatting(username)
                    elif mestaype=="che":
                    #接收到视频对话的停止消息
                        if username==self.mediatrans.chatuser:#如果这个消息是来自于正在对话的用户
                            print "close chatting window"
                            self.mediatrans.StopChatting()
                    else:
                        print k

                        
#         self.mesrecvlock.release()
        self.mesrecvlock.acquire()
        message=copy.deepcopy(self.mestodeal)
        self.mestodeal.clear()
        self.mesrecvlock.release()
        return message   

    def Logout(self):                            #登出，并停止监听
        '''在退出程序时调用一次即可，在服务器端登出'''
        usernamenum="logout"+self.username
        while True:
            try:
                self.sclint.sendall(usernamenum)  #查询在线状态
                feebback=self.sclint.recv(1024)
                if feebback.startswith('loo'):
                    break
            except socket.error,e:
                    continue
            self.islisten=False
            
    def LoadFriend(self):              #当前默认将2012011400-2012011520之间的在线用户全部列出       
        '''载入好友列表，也即刷新好友列表
                    可以配合下面的GetFriendInfo函数使用，也即每次先调用该函数刷新好友列表，再用GetFriendInfo获得新的好友信息
        '''  
        #username为用户名，对应好友文档
        usernamerange=range(2012011300,2012011600)        
        #self.friendfile = open('username.txt','rw')
        self.friendnum=0
        self.friendinfo.clear()
        self.friendloadlock.acquire()
        for usernamenum in usernamerange:
            username="%d"%usernamenum       
            try:
                self.sclint.sendall("q"+username)  #查询在线状态
                feebback=self.sclint.recv(1024)
                if not feebback.startswith('n')and not feebback.startswith('Inc'):
                    self.friendinfo[feebback]=usernamenum    #给信息字典中加入新信息/更改信息
                    self.friendnum+=1
            except socket.error,e:
                continue            
        self.friendloadlock.release()        
    
    def GetFriendInfo(self):
        '''获取在线的好友信息，
                        返回两个值
            friendinfo：好友信息，字典。key值为好友学号，value为好友Ip，按学号从大到小排序
                        调用之前可以根据需要先调用上面的LoadFriend函数刷新好友信息
                        如果未刷新就直接调用，返回的是原来的好友信息
                        事实上服务器线程默认每隔20s自动刷新一次好友信息，因此是否在调用前用代码手动刷新好友信息请根据需要判断
        '''
        self.friendloadlock.acquire()
        friendinfo=collections.OrderedDict(sorted(self.friendinfo.items(), key=lambda t: t[1]))
        self.friendloadlock.release()
        return friendinfo,self.friendnum
    
    def SendMessage(self,username,messstr,messtype="mes"):  
        '''
        username用户名，字符串   messstr 要发送的信息 messtype:消息类型 字符串  返回True则发送成功，否则失败
        messtype表示该消息的类型，不同消息类型的定义请见上面ServerListen的注释
                如果不指定消息类型，默认为普通文本消息
                前段调用时只需在username中填入学号，再在messstr中填入要发送的消息即可
        '''
        userIp=self.GetUserIp(username)
        if userIp=="":
            return False
        try:
            tempsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            tempsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tempsocket.connect((userIp,self.serverport))
            tempsocket.sendall(messtype+":"+messstr)
            tempback=tempsocket.recv(1024)
            if tempback.startswith("get"):
                tempsocket.close()
                return True
        except Exception,e:
            print e
        return False

    def SendQMessage(self,qID,usernamelist,messstr):  
        '''发送群消息
        qID:群ID，字符串     usernamelist用户名列表   messstr 要发送的信息    返回True则发送成功，否则失败
        '''
        messtype="qme"
        for i in usernamelist:            
            userIp=self.GetUserIp(i)
            if userIp=="":
                continue
            try:
                tempsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                tempsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                tempsocket.connect((userIp,self.serverport))
                tempsocket.sendall(messtype+":"+qID+":"+messstr)
                tempback=tempsocket.recv(1024)
                if tempback.startswith("get"):
                    tempsocket.close()
                else:
                    continue
            except Exception,e:
                print e
                continue

    def RecMesFSR(self,username,savefilepath,fileinfo):
        '''在MessageDeal函数中接收到fsr类型的消息时，如果允许对方发送文件，调用该函数
        username为用户名，字符串
        savefilepath为保存文件的路径，包含绝对路径和文件名
        fileinfo为接收到的文件信息
              实际调用时，只需要填入savefilepath一项，并将username和fileinfo按照收到信息本身的内容填入即可
               使用示例见MessageDeal函数中相应分支
        '''
        filepath,filename,filesize,filemd5=self.filetrans.DecodeFileInfo(fileinfo)
        savefilepath.replace("\\","/") #用正斜杠替换所有反斜杠
        if not self.SendFileSendingSure(username, fileinfo):
            print"fss send fail"
        self.filetrans.AddRecvFile(filemd5, savefilepath)

    def WaitForUser_FileTrans(self):
        while True:
            if self.acceptFileSignal =="True":
                
                '''如果想接收该文件，将下面函数调用中savefilepath一项改成文件保存路径对应的字符串即可'''
                self.RecMesFSR(self.filesendeusername, self.filePathSignal, self.filesendinfo)
                
                print "111"
                print self.filesendeusername,self.filePathSignal,self.filesendinfo

                self.setFilePath("No","No")

    def SendFileSendingRequire(self,username,filepath):  
        #发送文件传输的询问消息，username 用户名，字符串  filepath:欲发送文件的路径
        #发送成功就返回True，否则返回False
        messtype="fsr"  
        fileinfo=self.filetrans.EncodeFileInfo(filepath)       
        userIp=self.GetUserIp(username)

        if userIp=="" or fileinfo=="":
            return False
        try:
            tempsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            tempsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tempsocket.connect((userIp,self.serverport))
            tempsocket.sendall(messtype+":"+fileinfo)
            tempback=tempsocket.recv(1024)
            if tempback.startswith("get"):
                tempsocket.close()
                return True
        except Exception,e:
            print e
        return False
    def SendFileSendingSure(self,username,fileinfo):  
        #发送文件传输的允许消息，username 用户名，字符串  fileinfo:欲接收文件的信息，与对应的文件询问消息相同
        #发送成功就返回True，否则返回False
        messtype="fss"
        print fileinfo
        print username
        userIp=self.GetUserIp(username)
        print "user ip ois ",userIp

        if userIp=="" or fileinfo=="":
            return False
        try:
            tempsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            tempsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tempsocket.connect((userIp,self.serverport))
            tempsocket.sendall(messtype+":"+fileinfo)
            tempback=tempsocket.recv(1024)
            if tempback.startswith("get"):
                tempsocket.close()
                return True
        except Exception,e:
            print e
        return False        

        
    def AutoRefreshFriend(self,timegap):
    #作为线程使用，每隔一段时间自动刷新好友在线状态
        while True:
            time.sleep(timegap)
            self.friendloadlock.acquire()
            self.LoadFriend()
            self.friendloadlock.release
            
    def GetUserIp(self,username):
    #根据用户名返回Ip，如果用户不在线就返回一个空字符串
        print "GetUserIp username:",username
        userIp=""
        try:
            self.sclint.sendall("q"+username)  #查询在线状态
            feebback=self.sclint.recv(1024)        
            if not feebback.startswith('n') and not feebback.startswith('Inc'):
                userIp=feebback
        finally:
            return userIp

    def SendMediaChatRequire(self,username):
    #发送视频通话的请求
    #发送成功返回True，失败返回False
        messtype="chr"
        print username
        userIp=self.GetUserIp(username)
        if userIp=="" :
            return False
        try:
            tempsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            tempsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tempsocket.connect((userIp,self.serverport))
            tempsocket.sendall(messtype+":")
            tempback=tempsocket.recv(1024)
            if tempback.startswith("get"):
                tempsocket.close()
                return True
        except Exception,e:
            print e
        return False 
    def SendMediaChatSure(self,username):
        #发送视频对话的允许消息，username 用户名
        #发送成功就返回True，否则返回False
        messtype="chs"
        userIp=self.GetUserIp(username)
        if userIp=="" :
            return False
        try:
            tempsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            tempsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tempsocket.connect((userIp,self.serverport))
            tempsocket.sendall(messtype+":")
            tempback=tempsocket.recv(1024)
            if tempback.startswith("get"):
                tempsocket.close()
                return True
        except Exception,e:
            print e
        return False                   
    def SendMediaChatEnd(self,username):
        #发送视频对话的结束消息，username 用户名
        #发送成功就返回True，否则返回False
        messtype="che"
        print username
        userIp=self.GetUserIp(username)
        if userIp=="" :
            return False
        try:
            tempsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            tempsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tempsocket.connect((userIp,self.serverport))
            tempsocket.sendall(messtype+":")
            tempback=tempsocket.recv(1024)
            if tempback.startswith("get"):
                tempsocket.close()
                return True
        except Exception,e:
            print e
        return False       


'''
if __name__=="__main__":
    connect=MainConnect("2012011472")
    friendinfo,friendnum=connect.GetFriendInfo()
     
    print "There are %d firends "%friendnum
    for i in friendinfo.keys():
        print "%s:"%friendinfo[i]
        print i
#     filepath = tkFileDialog.askopenfilename(initialdir = 'T:/') 
 
#     if not connect.SendFileSendingRequire("2012011472", filepath):
#         print  "sending file failed"
    while True:
        mes=raw_input()
        connect.SendQMessage("1234群", ["2012011472"], mes)
        connect.SendMessage("2012011472", mes)
    connect.Logout()
'''
