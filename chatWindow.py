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


class ChatWindow(QtGui.QMainWindow):
	def __init__(self,parent = None):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#self.ui.graphicsView.setScence(QtGui.QGraphicScene())

#slots 
	@QtCore.pyqtSlot()
	def on_actionTranFile_triggered(self):
		path = QtGui.QFileDialog.getOpenFileName(self,u"请选择文件",'.')
		#得到文件路径
		#待完善
		if path :
			print path 

	@QtCore.pyqtSlot()
	def on_actionExpression_triggered(self):
		dialog = expressionWindow.ExpressionWindow()
		dialog.exec_()
		

	@QtCore.pyqtSlot()
	def on_actionVideo_triggered(self):
		print 11

	@QtCore.pyqtSlot()
	def on_actionVoice_triggered(self):
		print 11

	#窗口抖动
	@QtCore.pyqtSlot()
	def on_actionShake_triggered(self):
		desktop = QtGui.QApplication.desktop().availableGeometry()
		mw = self.geometry()
		for i in range(1,20):
			x =random.uniform(-20,20)
			y =random.uniform(-20,20)
			mw.moveTo(desktop.width()/2-mw.width()/2+x,desktop.height()/2-mw.height()/2+y)
			self.setGeometry(mw)
			time.sleep(0.2)

		print 11

	@QtCore.pyqtSlot()
	def on_actionHistory_triggered(self):
		print 11

	#退出
	@QtCore.pyqtSlot()
	def on_pushButton_2_clicked(self):
		exit()

	# 发送
	@QtCore.pyqtSlot()
	def on_pushButton_1_clicked(self):
		exit()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = ChatWindow()
    w.show()
    sys.exit(app.exec_())