#! C:/Program Files (x86)/Python27
# -*- coding: utf-8 -*-
# Project       :计网大作业
# Module        :chatUI.py
# Description   :聊天界面设计
# Author        :Changsheng Zhang 
# Last edited   :2014/12/22 02:56


# Form implementation generated from reading ui file 'chatUI.ui'
#
# Created: Mon Dec 22 02:15:32 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(712, 663)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 511, 411))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 440, 511, 111))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 560, 89, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 560, 89, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionTranFile = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTranFile.setIcon(icon)
        self.actionTranFile.setObjectName(_fromUtf8("actionTranFile"))
        self.actionExpression = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/f118.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExpression.setIcon(icon1)
        self.actionExpression.setObjectName(_fromUtf8("actionExpression"))
        self.actionVideo = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/web_camera.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVideo.setIcon(icon2)
        self.actionVideo.setObjectName(_fromUtf8("actionVideo"))
        self.actionVoice = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/voicedialer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVoice.setIcon(icon3)
        self.actionVoice.setObjectName(_fromUtf8("actionVoice"))
        self.actionShake = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/ringtone.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShake.setIcon(icon4)
        self.actionShake.setObjectName(_fromUtf8("actionShake"))
        self.actionHistory = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/bubbles.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHistory.setIcon(icon5)
        self.actionHistory.setObjectName(_fromUtf8("actionHistory"))
        self.toolBar.addAction(self.actionTranFile)
        self.toolBar.addAction(self.actionExpression)
        self.toolBar.addAction(self.actionVideo)
        self.toolBar.addAction(self.actionVoice)
        self.toolBar.addAction(self.actionShake)
        self.toolBar.addAction(self.actionHistory)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_2.setText(_translate("MainWindow", "关闭", None))
        self.pushButton.setText(_translate("MainWindow", "发送", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionTranFile.setText(_translate("MainWindow", "传输文件", None))
        self.actionTranFile.setToolTip(_translate("MainWindow", "传输文件", None))
        self.actionExpression.setText(_translate("MainWindow", "动态表情", None))
        self.actionExpression.setToolTip(_translate("MainWindow", "动态表情", None))
        self.actionVideo.setText(_translate("MainWindow", "视频聊天", None))
        self.actionVideo.setToolTip(_translate("MainWindow", "视频聊天", None))
        self.actionVoice.setText(_translate("MainWindow", "语音聊天", None))
        self.actionVoice.setToolTip(_translate("MainWindow", "语音聊天", None))
        self.actionShake.setText(_translate("MainWindow", "窗口振动", None))
        self.actionShake.setToolTip(_translate("MainWindow", "窗口振动", None))
        self.actionHistory.setText(_translate("MainWindow", "聊天记录", None))
        self.actionHistory.setToolTip(_translate("MainWindow", "聊天记录", None))

