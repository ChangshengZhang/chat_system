#! C:/Program Files (x86)/Python27
# -*- coding: utf-8 -*-
# Project       :计网大作业
# Module        :groupChatChoose.py
# Description   :群聊用户选择界面设计
# Author        :Changsheng Zhang 
# Last edited   :2014/12/23 22:24

from PyQt4 import QtCore, QtGui
from groupChatUI import Ui_MainWindow
import sys
import chatWindow
import UISender

 
class GroupChatChoose(QtGui.QMainWindow):
    def __init__(self,hostname,socket,parent = None):
        QtGui.QMainWindow.__init__(self)
        #QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.socket =socket

        #在线用户列表
        self.friendList = []

        self.showFriendList()

        self.groupChatFriendChoose =[]

        self.chatWindowName = ""

        self.hostName =hostname
        


    def showFriendList(self):
        #读取在线用户列表
        friendInfo,friendNum = UISender.UISender.LoadFriend(self.socket)
        del self.friendList[:]

        for i in friendInfo.keys():
            self.friendList.append(str(friendInfo[i]))
        #显示用户
        #self.ui.listWidgetFriend.setSortingEnabled(1)
        self.friendListItem = []

        j = 0
        for item in self.friendList:
            j = j+1
            path ='icon/'+str(j%10+1)+'.png'
            self.friendListItem.append(QtGui.QListWidgetItem(QtGui.QIcon(path),item))

        for i in range(len(self.friendListItem)):

            self.ui.listWidgetFriend.insertItem(i+1,self.friendListItem[i])

    @QtCore.pyqtSlot(QtGui.QListWidgetItem)
    def on_listWidgetFriend_itemDoubleClicked(self,friendItem):
        #得到索引
        #print self.ui.listWidgetFriend.currentRow()
        self.groupChatFriendChoose.append(self.friendList[self.ui.listWidgetFriend.currentRow()])
        #print self.groupChatFriendChoose
        if len(self.groupChatFriendChoose)==1:
            self.chatWindowName=self.friendList[self.ui.listWidgetFriend.currentRow()]
        else:
            self.chatWindowName=self.chatWindowName+"、"+self.friendList[self.ui.listWidgetFriend.currentRow()]
    @QtCore.pyqtSlot()  
    def on_pushButtonEnter_clicked(self):
        self.groupChat = chatWindow.ChatWindow(self.hostName,self.chatWindowName,self.socket,1)
        self.groupChat.show()
        #exit()
        #关闭原来的
        self.close()

    @QtCore.pyqtSlot()
    def on_pushButtonCancel_clicked(self):
        exit()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = GroupChatChoose()
    w.show()
    sys.exit(app.exec_())