#! C:/Program Files (x86)/Python27
# -*- coding: utf-8 -*-
# Project	  	:计网大作业
# Module		:infoUI.py
# Description	:弹窗信息UI
# Author	  	:Changsheng Zhang 
# Last edited 	:2014/12/22 01:37

from PyQt4 import QtCore, QtGui
import sys

class AboutAuthor(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.setWindowTitle(u'关于作者')
		self.resize(400,300)

		self.textEdit = QtGui.QTextBrowser()
		self.textEdit.setText(u'自22 张昌盛 zhangcsxx@gmail.com \n'+u"自25 谢鸣洲")

		layout =QtGui.QVBoxLayout()

		layout.addWidget(self.textEdit)

		self.setLayout(layout)

class AboutYouChat(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.setWindowTitle(u'关于YouChat')
		self.resize(400,300)

		self.textEdit = QtGui.QTextBrowser()
		self.textEdit.setText(u"CopyRight 2014 YouChat.\n"+"All rights reserved\n"+"version 1.0 Public\n ")

		layout =QtGui.QVBoxLayout()

		layout.addWidget(self.textEdit)

		self.setLayout(layout)
		
class AboutUpdate(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.setWindowTitle(u'关于YouChat')
		self.resize(400,300)

		self.textEdit = QtGui.QTextBrowser()
		self.textEdit.setText(u"当前没有可用更新。您正在使用的YouChat是最新版。")

		layout =QtGui.QVBoxLayout()

		layout.addWidget(self.textEdit)

		self.setLayout(layout)

class UserHelp(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self,parent)
		self.setWindowTitle(u'关于YouChat')
		self.resize(400,300)

		self.textEdit = QtGui.QTextBrowser()
		self.textEdit.setText(u"支持功能：\n1. 双击好友进行聊天；\n2. 发起群聊时，双击选择好友，按确定开始群聊； ")

		layout =QtGui.QVBoxLayout()

		layout.addWidget(self.textEdit)

		self.setLayout(layout)




if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = UserHelp()
    mainWindow.show()
    sys.exit(app.exec_())