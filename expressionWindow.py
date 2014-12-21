#! C:/Program Files (x86)/Python27
# -*- coding: utf-8 -*-
# Project       :计网大作业
# Module        :expressionWindow.py
# Description   :聊天界面
# Author        :Changsheng Zhang 
# Last edited   :2014/12/22 02:56

from PyQt4 import QtCore, QtGui
import expression 
import sys

class ExpressionWindow(QtGui.QDialog):
	def __init__(self,parent =None):
		QtGui.QDialog.__init__(self)
		self.ui = expression.Ui_Dialog()
		self.ui.setupUi(self)
		self.chosenEmotion = 0
		#self.Emotion =0
	@QtCore.pyqtSlot()
	def on_pushButton_01_clicked(self):
		self.chosenEmotion =1
		#print self.chosenEmotion
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_02_clicked(self):
		#print 2
		self.chosenEmotion =2
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_03_clicked(self):
		self.chosenEmotion =3
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_04_clicked(self):
		self.chosenEmotion =4
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_05_clicked(self):
		self.chosenEmotion =5
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_06_clicked(self):
		self.chosenEmotion =6
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_07_clicked(self):
		self.chosenEmotion =7
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_08_clicked(self):
		self.chosenEmotion =8
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_09_clicked(self):
		self.chosenEmotion =9
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_10_clicked(self):
		self.chosenEmotion =10
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_11_clicked(self):
		self.chosenEmotion =11
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_12_clicked(self):
		self.chosenEmotion =12
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_13_clicked(self):
		self.chosenEmotion =13
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_14_clicked(self):
		self.chosenEmotion =14
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_15_clicked(self):
		self.chosenEmotion =15
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_16_clicked(self):
		self.chosenEmotion =16
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_17_clicked(self):
		self.chosenEmotion =17
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_18_clicked(self):
		self.chosenEmotion =18
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_19_clicked(self):
		self.chosenEmotion =19
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_20_clicked(self):
		self.chosenEmotion =20
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_21_clicked(self):
		self.chosenEmotion =21
		self.sendEmotion(self.chosenEmotion)
	@QtCore.pyqtSlot()
	def on_pushButton_22_clicked(self):
		self.chosenEmotion =22
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_23_clicked(self):
		self.chosenEmotion =23
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_24_clicked(self):
		self.chosenEmotion =24
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_25_clicked(self):
		self.chosenEmotion =25
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_26_clicked(self):
		self.chosenEmotion =26
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_27_clicked(self):
		self.chosenEmotion =27
		self.sendEmotion(self.chosenEmotion)
	@QtCore.pyqtSlot()
	def on_pushButton_28_clicked(self):
		self.chosenEmotion =28
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_29_clicked(self):
		self.chosenEmotion =29
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_30_clicked(self):
		self.chosenEmotion =30
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_31_clicked(self):
		self.chosenEmotion =31
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_32_clicked(self):
		self.chosenEmotion =32
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_33_clicked(self):
		self.chosenEmotion =33
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_34_clicked(self):
		self.chosenEmotion =34
		self.sendEmotion(self.chosenEmotion)

	@QtCore.pyqtSlot()
	def on_pushButton_35_clicked(self):
		self.chosenEmotion =35
		self.sendEmotion(self.chosenEmotion)
	
	@QtCore.pyqtSlot()
	def on_pushButton_36_clicked(self):
		self.chosenEmotion =36
		self.sendEmotion(self.chosenEmotion)

	#发送表情
	def sendEmotion(self,chosenEmotion):
		print chosenEmotion

		#待写


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = ExpressionWindow()
    w.show()
    sys.exit(app.exec_())

