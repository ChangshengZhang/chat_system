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

 
class GroupChatChoose(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)
        #QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.showFriendList()

        self.groupChatFriendChoose =[]
        


    def showFriendList(self):
        #读取在线用户列表
        self.friendList = []
        f = open('userList/friendList.youchat')
        line = f.readline()
        while line:
            temp = line.split("\n")
            self.friendList.append(temp[0])
            line = f.readline()

        f.close()
        #显示用户
        self.ui.listWidgetFriend.setSortingEnabled(1)
        self.friendListItem = []

        j = 0
        for item in self.friendList:
            j = j+1
            path ='icon/'+str(j%10)+'.png'
            self.friendListItem.append(QtGui.QListWidgetItem(QtGui.QIcon(path),item))

        for i in range(len(self.friendListItem)):

            self.ui.listWidgetFriend.insertItem(i+1,self.friendListItem[i])

    @QtCore.pyqtSlot(QtGui.QListWidgetItem)
    def on_listWidgetFriend_itemDoubleClicked(self,friendItem):
        #得到索引
        #print self.ui.listWidgetFriend.currentRow()
        self.groupChatFriendChoose.append(self.friendList[self.ui.listWidgetFriend.currentRow()])
        #print self.groupChatFriendChoose
    
    @QtCore.pyqtSlot()  
    def on_pushButtonEnter_clicked(self):
        self.groupChat = chatWindow.ChatWindow()
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