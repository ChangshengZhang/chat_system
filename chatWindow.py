#! C:/Program Files (x86)/Python27
# -*- coding: utf-8 -*-
# Project       :计网大作业
# Module        :chatWindow.py
# Description   :聊天界面
# Author        :Changsheng Zhang 
# Last edited   :2014/12/22 02:56

from PyQt4 import QtCore, QtGui
from chatUI import Ui_MainWindow
import expressionWindow
import sys
import random
import time 
#import MainConnect
import UISender
import time 
from expressionUI import myTextBrowser
sys.setdefaultencoding('utf-8')



class ChatWindow(QtGui.QMainWindow):
	def __init__(self,hostname,username,socket,singleOrGroup=0,parent = None):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#聊天好友学号
		self.userName = str(username)
		#当前用户学号
		self.hostName = hostname
		#print username
		self.setWindowTitle(u"和"+self.userName+u"聊天中")
		self.socket = socket
		self.choseEmotion =0

		#self.ui.graphicsView.setScence(QtGui.QGraphicScene())
	'''
	def loadResource (self, type, name):
		return QtGui.QPixmap("expression/01.png")
	'''
	def writeInFile(self,message):
		f =open("log/"+self.userName+".youchat","a")
		print >> f,message
		f.close()

	def receiveFile(self,senderName,fileName,fileSize):
		button=QtGui.QMessageBox.question(self,u"传输文件",u"是否接收"+fileName+"?",QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel,QtGui.QMessageBox.Ok)  
		if button==QtGui.QMessageBox.Ok: 
			#print "ok"
			#receivePath = QtGui.QFileDialog.getOpenFileName(self,u"请选择保存路径",'.')
			receivePath = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))+"\\"+fileName
			if receivePath:
				return "True",receivePath
		else:
			return "False","False"

	def shakeWindow(self):
		desktop = QtGui.QApplication.desktop().availableGeometry()
		mw = self.geometry()
		for i in range(1,20):
			x =random.uniform(-20,20)
			y =random.uniform(-20,20)
			mw.moveTo(desktop.width()/2-mw.width()/2+x,desktop.height()/2-mw.height()/2+y)
			self.setGeometry(mw)
			time.sleep(0.2)

	def setChoseEmotion(self,choseEmotion):
		self.choseEmotion =choseEmotion


	def showEmotion(self,senderName,filePath):
		print filePath
		filePath = "expression/"+str(filePath)+".png"
		print filePath
		#self.ui.textBrowser.append(u"我说"+"""<br /><img src="test.jpg"/>""")
		self.a = myTextBrowser(filePath)
		self.a.append(senderName+u"发送了表情"+"""<br /><img src="test.jpg"/>""")
		self.a.show()
    	

	def showChatMessage(self,senderName,message):

		self.writeInFile(senderName+"say:"+message)
		if message[0:11] == "shakewindow":
			self.shakeWindow()
		elif message[0:7] == "emotion":
			self.showEmotion(senderName,message[7:9])
		else:
			self.ui.textBrowser.append(senderName+u"说:"+message)


#slots 

	@QtCore.pyqtSlot()
	def on_actionTranFile_triggered(self):
		path = QtGui.QFileDialog.getOpenFileName(self,u"请选择文件",'.')
		#得到文件路径
		#待完善
		if path :
			UISender.UISender.SendFileSendingRequire(self.socket,str(self.userName),path)
			
	#发送表情
	@QtCore.pyqtSlot()
	def on_actionExpression_triggered(self):
		dialog = expressionWindow.ExpressionWindow()
		self.connect(dialog,dialog.emotionSignal,self.setChoseEmotion)
		dialog.exec_()

		if self.choseEmotion !="00":
			inputMessage = "emotion"+self.choseEmotion
			UISender.UISender.SendMessage(self.socket,str(self.userName),unicode(inputMessage,"utf-8"))
			self.imgpath = "expression/"+inputMessage[7:9]+".png"
			#imgpath ="expression//01.png"
			print 1,self.imgpath
			#self.ui.textBrowser.append("""<br /><img src="""+self.imgpath+"""/>""")
			
			self.a = myTextBrowser(self.imgpath)
			self.a.append(u"你发送了表情"+"""<br /><img src=""/>""")
			self.a.show()

			self.choseEmotion =""
		

	@QtCore.pyqtSlot()
	def on_actionVideo_triggered(self):
		UISender.UISender.SendMediaChattingRequire(self.socket,self.userName)

	@QtCore.pyqtSlot()
	def on_actionVoice_triggered(self):
		print 11

	#窗口抖动
	@QtCore.pyqtSlot()
	def on_actionShake_triggered(self):
		inputMessage = u"您发送了一个窗口抖动"
		UISender.UISender.SendMessage(self.socket,self.userName,unicode(inputMessage,"utf-8"))
		self.ui.textBrowser.append(inputMessage)


	@QtCore.pyqtSlot()
	def on_actionHistory_triggered(self):
		self.chatHistoryWindow =myTextBrowser("None")

		f =open("log/"+self.userName+".youchat","r")
		line = f.readline()
		while line:
			print line
			self.chatHistoryWindow.append(str(line))
			line = f.readline()
		f.close()

		self.chatHistoryWindow.show()

	#退出
	@QtCore.pyqtSlot()
	def on_pushButton_2_clicked(self):
		self.close()

	# 发送
	@QtCore.pyqtSlot()
	def on_pushButton_clicked(self):
		#当前输入的文本
		inputMessage = self.ui.textEdit.toPlainText()

		#print inputMessage
		self.writeInFile("I say:"+inputMessage)
		#发送消息
		#UISender.UISender.SendMessage(self.socket,self.userName,inputMessage)
		UISender.UISender.SendMessage(self.socket,str(self.userName),unicode(inputMessage,"utf-8"))

		self.ui.textBrowser.append(u"我说:"+inputMessage)
		self.ui.textEdit.clear()
		

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = ChatWindow("d","a","c")
    w.show()
    sys.exit(app.exec_())