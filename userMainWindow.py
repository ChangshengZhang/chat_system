#! C:/Program Files (x86)/Python27
# -*- coding: utf-8 -*-
# Project       :计网大作业
# Module        :userMainWindow.py
# Description   :用户主界面设计
# Author        :Changsheng Zhang 
# Last edited   :2014/12/23 22:24

from PyQt4 import QtCore, QtGui
from userUI import Ui_MainWindow
import sys
import loginUI
import infoUI
import chatWindow
import groupChatChoose


class UserMainWindow(QtGui.QMainWindow):
	def __init__(self,parent = None):
		QtGui.QMainWindow.__init__(self)
		#QtGui.QWidget.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle("2012011420")

		self.showFriendList()

		#聊天窗口
		self.chatwithFriend =[]
		self.chatNum = 0

		#群聊窗口
		self.groupChatwithFriend = []
		self.groupChatNum = 0



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
		friendListItem = []

		j = 0
		for item in self.friendList:
			j = j+1
			path ='icon/'+str(j%10)+'.png'
			friendListItem.append(QtGui.QListWidgetItem(QtGui.QIcon(path),item))

		for i in range(len(friendListItem)):

			self.ui.listWidgetFriend.insertItem(i+1,friendListItem[i])






#slots
	
	@QtCore.pyqtSlot(QtGui.QListWidgetItem)
	def on_listWidgetFriend_itemDoubleClicked(self,friendItem):

		#得到当前用户索引，从0开始
		#self.ui.listWidgetFriend.currentRow()

		self.chatwithFriend.append(chatWindow.ChatWindow())
		self.chatwithFriend[self.chatNum-1].show()
		self.chatNum = self.chatNum + 1

		#chatwithFriend.exec_()
	
	
	@QtCore.pyqtSlot()
	def on_actionSwitchAccount_triggered(self):
		dialog = loginUI.LoginDialog()
		dialog.exec_()

	@QtCore.pyqtSlot()
	def on_actionQuit_triggered(self):
		exit()

	@QtCore.pyqtSlot()
	def on_actionAuthor_triggered(self):
		dialog = infoUI.AboutAuthor()
		dialog.exec_()

	@QtCore.pyqtSlot()
	def on_actionYouchat_triggered(self):
		dialog = infoUI.AboutYouChat()
		dialog.exec_()

	@QtCore.pyqtSlot()
	def on_actionUpdate_triggered(self):
		dialog = infoUI.AboutUpdate()
		dialog.exec_()

	@QtCore.pyqtSlot()
	def on_actionUseHelp_triggered(self):
		dialog = infoUI.UserHelp()
		dialog.exec_()

	# 刷新好友列表
	@QtCore.pyqtSlot()
	def on_pushButtonRefresh_clicked(self):
		#待写

		#清空好友列表
		self.ui.listWidgetFriend.clear()
		self.showFriendList()


	@QtCore.pyqtSlot()
	def on_pushButtonGroupChat_clicked(self):
		
		self.groupChatwithFriend.append(groupChatChoose.GroupChatChoose())
		#self.chatwithFriend[self.chatNum] = chatWindow.ChatWindow()
		
		self.groupChatwithFriend[self.groupChatNum-1].show()
		#self.chatwithFriend[0].show()
		self.groupChatNum = self.groupChatNum + 1

		


	@QtCore.pyqtSlot()
	def on_searchUserName_clicked(self):
		print "searchUserName"





if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	w = UserMainWindow()
	w.show()
	sys.exit(app.exec_())