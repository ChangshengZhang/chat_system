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
import MainConnect
import UISender



class UserMainWindow(QtGui.QMainWindow):
	def __init__(self,currentHostUserName,parent = None):
		QtGui.QMainWindow.__init__(self)
		#QtGui.QWidget.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.currentHostUserName = currentHostUserName

		self.setWindowTitle(self.currentHostUserName)
		#self.connect=MainConnect.MainConnect("2012011420")
		
		#socket
		self.socket = UISender.UISender.SocketConnect()

		#在线用户列表
		self.friendList = []

		#聊天窗口
		self.chatwithFriend =[]
		self.chatNum = 0

		#群聊窗口
		self.groupChatwithFriend = []
		self.groupChatNum = 0

		self.showFriendList()

		#mainConnect
		self.mainConnect = MainConnect.MainConnect(self.currentHostUserName)
		self.connect(self.mainConnect,self.mainConnect.mssSignal,self.receiveMessage)
		self.connect(self.mainConnect,self.mainConnect.fileSignal,self.receiveFileRequest)
	def showFriendList(self):
		'''
		f = open('userList/friendList.youchat')
		line = f.readline()
		while line:
			temp = line.split("\n")
			self.friendList.append(temp[0])
			line = f.readline()

		f.close()
		'''
		#得到在线好友清单
		friendInfo,friendNum = UISender.UISender.LoadFriend(self.socket)
		del self.friendList[:]

		for i in friendInfo.keys():
			self.friendList.append(str(friendInfo[i]))
		#显示用户
		self.ui.listWidgetFriend.setSortingEnabled(1)
		friendListItem = []

		j = 0
		for item in self.friendList:
			j = j+1
			path ='icon/'+str(j%10+1)+'.png'
			#path ='icon/'+'2.png'
			friendListItem.append(QtGui.QListWidgetItem(QtGui.QIcon(path),item))

		for i in range(len(friendListItem)):

			self.ui.listWidgetFriend.insertItem(i+1,friendListItem[i])

	def receiveMessage(self,senderName,message):
		#temp = 0 表示需要新建聊天窗口，=1不需要
		temp = 0
		for i in range(len(self.chatwithFriend)):
			if senderName ==self.chatwithFriend[i].userName:
				self.chatwithFriend[i].showChatMessage(senderName,message)
				temp =1
				break
		if temp ==0:
			newChatWindow = chatWindow.ChatWindow(self.currentHostUserName,senderName,self.socket)
			self.chatwithFriend.append(newChatWindow)
			self.chatwithFriend[self.chatNum].show()
			self.chatwithFriend[self.chatNum].showChatMessage(senderName,message)
			self.chatNum =self.chatNum +1

	def receiveFileRequest(self,senderName,fileName,fileSize):
		#temp = 0 表示需要新建聊天窗口，=1不需要
		temp = 0
		acceptTransFile = ""
		filepath = ""
		for i in range(len(self.chatwithFriend)):
			if senderName ==self.chatwithFriend[i].userName:
				acceptTransFile,filepath= self.chatwithFriend[i].receiveFile(senderName,fileName,fileSize)
				temp =1
				break
		if temp ==0:
			newChatWindow = chatWindow.ChatWindow(self.currentHostUserName,senderName,self.socket)
			self.chatwithFriend.append(newChatWindow)
			self.chatwithFriend[self.chatNum].show()
			acceptTransFile,filepath =self.chatwithFriend[self.chatNum].receiveFile(senderName,fileName,fileSize)
			self.chatNum =self.chatNum +1

		#self.acceptFileSignal =QtCore.SIGNAL("acceptFileSignal")
		#self.emit(self.acceptFileSignal,acceptTransFile,filepath)
		#调试用，输出保存文件路径
		print  "1",acceptTransFile, filepath
		self.mainConnect.setFilePath(acceptTransFile,filepath)
		#return acceptTransFile,filepath


#slots
	#双击聊天
	@QtCore.pyqtSlot(QtGui.QListWidgetItem)
	def on_listWidgetFriend_itemDoubleClicked(self,friendItem):

		#得到当前用户索引，从0开始
		#self.ui.listWidgetFriend.currentRow()

		#得到当前好友的学号
		currentUserName = self.ui.listWidgetFriend.currentItem().text()
		#print currentUserName

		temp =chatWindow.ChatWindow(self.currentHostUserName,currentUserName,self.socket)
		#temp.setConnect(self.connect)
		#temp.setCurrentUserName(currentUserName)

		self.chatwithFriend.append(temp)
		self.chatwithFriend[self.chatNum].show()
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
		#清空好友列表
		self.ui.listWidgetFriend.clear()
		self.showFriendList()


	#群聊
	@QtCore.pyqtSlot()
	def on_pushButtonGroupChat_clicked(self):
		
		self.groupChatwithFriend.append(groupChatChoose.GroupChatChoose(self.currentHostUserName,self.socket))
		#self.chatwithFriend[self.chatNum] = chatWindow.ChatWindow()
		
		self.groupChatwithFriend[self.groupChatNum-1].show()
		#self.chatwithFriend[0].show()
		self.groupChatNum = self.groupChatNum + 1

	#查找好友
	@QtCore.pyqtSlot()
	def on_searchUserName_clicked(self):
		searchName = self.ui.inputUserName.text()
		if searchName in self.friendList:
			QtGui.QMessageBox.information(self,u"查找",searchName+u"在线")
		else:
			QtGui.QMessageBox.information(self,u"查找",searchName+u"不在线")



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	w = UserMainWindow("2012011420")
	w.show()
	sys.exit(app.exec_())