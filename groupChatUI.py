# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupchatUI.ui'
#
# Created: Wed Dec 24 02:19:37 2014
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
        MainWindow.resize(357, 616)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.listWidgetFriend = QtGui.QListWidget(self.centralwidget)
        self.listWidgetFriend.setGeometry(QtCore.QRect(10, 30, 341, 481))
        self.listWidgetFriend.setObjectName(_fromUtf8("listWidgetFriend"))
        self.pushButtonCancel = QtGui.QPushButton(self.centralwidget)
        self.pushButtonCancel.setGeometry(QtCore.QRect(200, 540, 101, 31))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.pushButtonEnter = QtGui.QPushButton(self.centralwidget)
        self.pushButtonEnter.setGeometry(QtCore.QRect(50, 540, 93, 31))
        self.pushButtonEnter.setObjectName(_fromUtf8("pushButtonEnter"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "请选择群聊好友", None))
        self.pushButtonCancel.setText(_translate("MainWindow", "取消", None))
        self.pushButtonEnter.setText(_translate("MainWindow", "确定", None))

