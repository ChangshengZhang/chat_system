#! C:/Program Files (x86)/Python27
# -*- coding: utf-8 -*-
# Project	  	:计网大作业
# Module		:chatUI.py
# Description	:UI界面设计
# Author	  	:Changsheng Zhang 
# Last edited 	:2014/12/15 10:30

class chatUI():
	"""docstring for UIInit"""
	def __init__(self):
		super(UIInit, self).__init__()
		self.initUI()

	def initUI(self):
		#设置窗口大小
		self.resize(600,400)
		self.setWindowTitle("YouChat")
		screen =QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
		
		#定义组件
		
		
		