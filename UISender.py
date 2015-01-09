#coding=utf-8
import socket 
import os
import sys
import hashlib
import tkFileDialog
reload(sys)
sys.setdefaultencoding('utf-8') 

'''以下的类包含了登入、登出、普通消息发送、文件传输请求消息发送、载入在线好友功能
所有方法是静态方法，通过UISender.XXX即可直接调用
已经可以直接使用，使用实例见最后
'''
class UISender:  
    netserverhost="166.111.180.60"
    netserverport=8000
    mesport=9355 
    fileinfosize=512
    @staticmethod
    def SocketConnect():
        sclint=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sclint.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sclint.connect((UISender.netserverhost,UISender.netserverport))
        return sclint
    @staticmethod    
    def Login(sclint,username):               
        while True:                             
            try:                
                print "Connect with net server successfully"
                sclint.sendall(username+"_net2014")
                feedback=sclint.recv(1024);
                if feedback.startswith("lol"):
                    break;
            except socket.error,e:
                print "Err:%s"%e
                print "Try to connect net server again\n\r"   
                
    @staticmethod
    def Logout(sclint,username):                            #�ǳ�����ֹͣ����
        usernamenum="logout"+username
        while True:
            try:
                sclint.sendall(usernamenum)  #��ѯ����״̬
                feebback=sclint.recv(1024)
                if feebback.startswith('loo'):
                    break
            except socket.error,e:
                    continue
    @staticmethod            
    def LoadFriend(sclint):              #��ǰĬ�Ͻ�2012011400-2012011520֮��������û�ȫ���г�       
        usernamerange=range(2012011300,2012011600)        
        #self.friendfile = open('username.txt','rw')
        friendnum=0
        friendinfo={}
        for usernamenum in usernamerange:
            username="%d"%usernamenum       
            try:
                sclint.sendall("q"+username)  #��ѯ����״̬
                feebback=sclint.recv(1024)
                if not feebback.startswith('n')and not feebback.startswith('Inc'):
                    friendinfo[feebback]=usernamenum    #����Ϣ�ֵ��м�������Ϣ/�����Ϣ
                    friendnum+=1
            except socket.error,e:
                continue            
        return friendinfo,friendnum       
    @staticmethod    
    def SendMessage(sclint,username,messstr,messtype="mes"): 
        userIp=""
        try:
            print "UISender getIp, username:",username
            sclint.sendall("q"+str(username))  #查询在线状态
            #sclint.sendall("q"+"2012011472")  #查询在线状态
            print "q"+username
            feedback=sclint.recv(1024)  
            print "feeback:",feedback      
            if not feedback.startswith('n') and not feedback.startswith('Ple'):
                userIp=feedback
        except Exception,e:
            
            print e 
        if userIp=="":
            return False
        print "User IP",userIp
        try:
            tempsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            tempsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tempsocket.connect((userIp,UISender.mesport))
            tempsocket.sendall(messtype+":"+messstr)
            tempback=tempsocket.recv(1024)
            if tempback.startswith("get"):
                print tempsocket.getpeername()
                print tempback
                tempsocket.close()
                return True
        except Exception,e:
            print "UISender send mes fail"
            print e
        return False
    @staticmethod
    def SendQMessage(sclint,qID,usernamelist,messstr):  
        '''发送群消息
        qID:群ID，字符串     usernamelist用户名列表   messstr 要发送的信息    返回True则发送成功，否则失败
        '''
        messtype="qme"
        for i in usernamelist:            
            userIp=""
            try:
                sclint.sendall("q"+i)  #查询在线状态
                feebback=sclint.recv(1024)        
                if not feebback.startswith('n') and not feebback.startswith('Inc'):
                    userIp=feebback
            except Exception,e:
                print e 
            if userIp=="":
                continue
            try:
                tempsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                tempsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                tempsocket.connect((userIp,UISender.mesport))
                tempsocket.sendall(messtype+":"+qID+":"+messstr)
                tempback=tempsocket.recv(1024)
                if tempback.startswith("get"):
                    tempsocket.close()
                else:
                    continue
            except:
                continue
    @staticmethod
    def SendFileSendingRequire(sclint,username,filepath):  
        #发送文件传输的询问消息，sclint:与网络服务器通信的socket  username:用户名，字符串  filepath:欲发送文件的路径
        #发送成功就返回True，否则返回False
#         filepath=filepath.encode("utf-8")
        messtype="fsr"  
        fileinfo=""
        filesize=0
        try:
            filepath.replace("\\","/") #路径标准化，用正斜杠替换所有反斜杠
            filepathlist=filepath.split("/")           
            filename=filepathlist[len(filepathlist)-1]#从路径中获取文件名
            try:
                path=filepath
                filesize=os.stat(filepath.decode("utf-8")).st_size #获取文件大小 
            except Exception,e:              
                print e
                info=sys.exc_info() 
                print info
            print "filesize",filesize
            filemd5=hashlib.md5(filename).hexdigest()     
            fileinfo=filepath+"&"+filename+"&"+str(filesize)+"&"+filemd5+"&"
            fileinfo=fileinfo.ljust(UISender.fileinfosize,"+")  
        except Exception,e:
            print e
        userIp=""
        try:
            sclint.sendall("q"+username)  #查询在线状态
            feebback=sclint.recv(1024)        
            if not feebback.startswith('n') and not feebback.startswith('Inc'):
                userIp=feebback
        except Exception,e:
            print e 
        if userIp=="" or fileinfo=="":
            return False
        try:
            tempsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            tempsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tempsocket.connect((userIp,UISender.mesport))
            tempsocket.sendall(messtype+":"+fileinfo)
            tempback=tempsocket.recv(1024)
            if tempback.startswith("get"):
                tempsocket.close()
                return True
        except Exception,e:
            print e
        return False
    @staticmethod
    def SendMediaChattingRequire(sclint,username):
    #发送视频通话的请求
    #发送成功返回True，失败返回False
        messtype="chr"
        userIp=""
        try:
            sclint.sendall("q"+username)  #查询在线状态
            feebback=sclint.recv(1024)        
            if not feebback.startswith('n') and not feebback.startswith('Inc'):
                userIp=feebback
        except Exception,e:
            print e 
        if userIp=="":
            return False
        try:
            tempsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            tempsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            tempsocket.connect((userIp,UISender.mesport))
            tempsocket.sendall(messtype+":")
            tempback=tempsocket.recv(1024)
            if tempback.startswith("get"):
                tempsocket.close()
                return True
        except Exception,e:
            print e
        return False 
if __name__=="__main__":
    soc=UISender.SocketConnect()
    '''首先声明一个socket变量连接服务器，直接令该变量=UISender.SocketConnect()即可，
        注意后面所有函数的sclint参数都必须是这个变量，也即打开子窗口需要发送时也要把这个变量传到子窗口内，否则这些函数会失效
    '''
    UISender.Login(soc, "2012011472")
    '''登陆，soc为上面提到的连接服务器的socket，后面为学号，即用这个学号登陆'''
    friendinfo,friendnum=UISender.LoadFriend(soc)
    '''获取好友信息，
        返回的friend是一个字典，其key为Ip，value为学号，包含2012011300-2012011600之间所有在线的学号
    friend是以上学号范围中在线的总人数
    '''

    UISender.SendMessage(soc, "2012011472", u"a message from UISender")  
    '''向用户发送信息
        更改其中的学号和信息字符串就会向不同的用户发送不同信息
        返回一个bool值，发送成功则返回True，否则为False
    '''
    
    UISender.SendQMessage(soc,"test群", ["2012011472"], "a message from UISender")  
    '''向用户发送信息
        更改其中的学号和信息字符串就会向不同的用户发送不同信息
        返回一个bool值，发送成功则返回True，否则为False
    '''
    
    filepath = tkFileDialog.askopenfilename(initialdir = 'T:/') 
    UISender.SendFileSendingRequire(soc, "2012011420", filepath)  
    '''向用户发送文件传输请求
        更改学号会发到不同用户处
    filepath为要发送的文件路径名
        发送成功返回True，否则False
        注意filepath的编码，有时候发送不成功是因为编码问题，具体怎么编码我不清楚，但是用tk返回的路径可以成功
    '''

