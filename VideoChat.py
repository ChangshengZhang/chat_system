# coding=utf-8  

import socket
import Image
import pygame
import sys
import threading
import time
import pyaudio
from VideoCapture import Device

#define of params

#record time


class MediaTrans:
    def __init__(self,sclint):
        self.audiobuffersize = 200
        self.framerate = 3000
        self.channels = 1
        self.sampwidth = 2
        self.vserverport=9365
        self.aserverport=9366
        self.netserverhost="166.111.180.60"
        self.netserverport=8000
        self.mesport=9355
        self.vsendthread=1
        self.vreavthread=1
        self.asendthread=1
        self.areavthread=1
        self.ischatting=False
        self.chatlock=threading.Lock()
        self.chatuser=""#正在聊天对象的学号
        self.sclint=sclint#从外部传入的Socket，已经和服务器建立好连接
        self.sclintlock=threading.Lock()
#         self.sendthread=threading.Thread(target=self.Send,name="SendThread",args=(cam,))
#         self.sendthread.setDaemon(1)
#         self.sendthread.start()

    def SendVideo(self,username):
        userIp=""
        self.sclintlock.acquire()
        try:
            self.sclint.sendall("q"+username)  #查询在线状态
            feebback=self.sclint.recv(1024)        
            if not feebback.startswith('n') and not feebback.startswith('Ple'):
                userIp=feebback
        except Exception,e:
            print e 
        self.sclintlock.release()
        if userIp=="":
            print "用户不在线或无法连接终止视频发送"
            return False
        cam = Device()
        vclints = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        vclints.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)        
        while self.ischatting==True: 
            im = cam.getImage()
            im = im.resize((160,120))
            da = im.tostring()            
            vclints.sendto(da,(userIp,self.vserverport))
    def StartSendVideo(self,username):
        self.vsendthread=threading.Thread(target=self.SendVideo,name="SendVideoThread",args=(username,))
        self.vsendthread.setDaemon(1)
        self.vsendthread.start()            
    def RecvVideo(self):
        pygame.init()
        screen = pygame.display.set_mode((320,240))
        pygame.display.set_caption("Media Chatting")
        pygame.display.flip()
        vservers = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        vservers.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        vservers.setblocking(False)
        vservers.bind(("", self.vserverport))
        clock = pygame.time.Clock()    
        while self.ischatting==True:         
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()   
            try:
                data,addr=vservers.recvfrom(8000000)
            except:
                continue
            if data=="":
                continue
            camshot = pygame.image.frombuffer(data, (160,120), "RGB")
            camshot=pygame.transform.scale2x(camshot)
            screen.blit(camshot, (0,0))
            pygame.display.update() 
#             print clock.get_fps()   
            clock.tick()
        pygame.quit()
    def StartRecvVideo(self):
        self.vrecvthread=threading.Thread(target=self.RecvVideo,name="RecvVideoThread")
        self.vrecvthread.setDaemon(1)
        self.vrecvthread.start()    

    def SendAudio(self,username):
        #open the input of wave
        userIp=""
        self.sclintlock.acquire()
        try:
            self.sclint.sendall("q"+username)  #查询在线状态
            feebback=self.sclint.recv(1024)        
            if not feebback.startswith('n') and not feebback.startswith('Inc'):
                userIp=feebback
        except Exception,e:
            print e 
        self.sclintlock.release()
        print feebback
        if userIp=="":
            print "用户不在线或无法连接终止音频发送"
            return False
        aclints= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        aclints.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)        
        pa=pyaudio.PyAudio()
        stream = pa.open(format = pyaudio.paInt16, channels =1,
                         rate = self.framerate, input = True,
                         frames_per_buffer = self.audiobuffersize)
        while self.ischatting==True: 
            audiostr = stream.read(self.audiobuffersize)
            aclints.sendto(audiostr,(userIp,self.aserverport))
            
    def StartSendAudio(self,username):
        self.asendthread=threading.Thread(target=self.SendAudio,name="SendAudioThread",args=(username,))
        self.asendthread.setDaemon(1)
        self.asendthread.start()          
    def RecvAudio(self):
        aservers = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        aservers.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        aservers.bind(("", self.aserverport))
        pa=pyaudio.PyAudio()
        stream = pa.open(format = pyaudio.paInt16, channels =1,
                         rate = self.framerate, output = True,
                         )
        while self.ischatting==True:   
            audiostr,addr=aservers.recvfrom(8000000)
            stream.write(audiostr)
    def StartRecvAudio(self):
        self.arecvthread=threading.Thread(target=self.RecvAudio,name="RecvAudioThread")
        self.arecvthread.setDaemon(1)
        self.arecvthread.start()   
    def Chatting(self,username):
        self.chatlock.acquire()
        self.ischatting=True
        self.chatuser=username
        self.StartSendAudio(username)
        self.StartSendVideo(username)
        self.StartRecvAudio()
        self.StartRecvVideo()
        while self.vrecvthread.is_alive():
            pass
        self.ischatting=False
        self.chatuser=""
        
        #通知对方该视频通话已经结束
        self.sclintlock.acquire()
        try:
            self.sclint.sendall("q"+username)  #查询在线状态
            feebback=self.sclint.recv(1024)        
            if not feebback.startswith('n') and not feebback.startswith('Ple'):
                userIp=feebback
            ends=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            ends.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            ends.connect((userIp,self.mesport))
            ends.sendall("che: bye")
            tempback=ends.recv(1024)
            if tempback.startswith("get"):
                ends.close()
        except Exception,e:
            print e 
            
        self.sclintlock.release()
        self.chatlock.release()
    def StartChatting(self,username):
        chatthread=threading.Thread(target=self.Chatting,name="ChatThread",args=(username,))
        chatthread.setDaemon(1)
        chatthread.start()
    def StopChatting(self):
        self.ischatting=False
        
if __name__=="__main__":
    import UISender
    s=UISender.UISender.SocketConnect()
    UISender.UISender.Login(s,"2012011472")
    v=MediaTrans(s)
#   v.SendAudio("2012011472")
    v.StartChatting("2012011472")
#     v.StartRecvAudio()
#     v.StartSendAudio("2012011472")
#     v.StartRecvVideo()
#     v.StartSendVideo("2012011472")
    while True:
        raw_input()
        s.sendall("q2012011472")
        print s.recv(1024)
        pass
#     sendthread=threading.Thread(target=SendVideo,name="SendThread")
#     sendthread.setDaemon(1)
#     sendthread.start()  
#     time.sleep(1)
#     v.StartRecvVideo()
    
  
#     v.SendVideo()

#     v.RecvVideo()