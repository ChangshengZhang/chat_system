#! C:/Program Files (x86)/Python27
# -*- coding: utf-8 -*-
# Project       :计网大作业
# Module        :userUI.py
# Description   :用户主界面设计
# Author        :Changsheng Zhang 
# Last edited   :2014/12/19 2:24
# Form implementation generated from reading ui file 'userUI.ui'
#
# Created: Fri Dec 19 02:24:20 2014
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
        MainWindow.resize(357, 667)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.inputUserName = QtGui.QLineEdit(self.centralwidget)
        self.inputUserName.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.inputUserName.setObjectName(_fromUtf8("inputUserName"))
        self.searchUserName = QtGui.QPushButton(self.centralwidget)
        self.searchUserName.setGeometry(QtCore.QRect(280, 10, 71, 31))
        self.searchUserName.setObjectName(_fromUtf8("searchUserName"))
        self.listWidgetFriend = QtGui.QListWidget(self.centralwidget)
        self.listWidgetFriend.setGeometry(QtCore.QRect(10, 50, 341, 481))
        self.listWidgetFriend.setObjectName(_fromUtf8("listWidgetFriend"))
        self.pushButtonGroupChat = QtGui.QPushButton(self.centralwidget)
        self.pushButtonGroupChat.setGeometry(QtCore.QRect(200, 550, 101, 31))
        self.pushButtonGroupChat.setObjectName(_fromUtf8("pushButtonGroupChat"))
        self.pushButtonRefresh = QtGui.QPushButton(self.centralwidget)
        self.pushButtonRefresh.setGeometry(QtCore.QRect(60, 550, 93, 31))
        self.pushButtonRefresh.setObjectName(_fromUtf8("pushButtonRefresh"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 357, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuAccount = QtGui.QMenu(self.menuBar)
        self.menuAccount.setObjectName(_fromUtf8("menuAccount"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionFriend = QtGui.QAction(MainWindow)
        self.actionFriend.setObjectName(_fromUtf8("actionFriend"))
        self.actionSwitchAccount = QtGui.QAction(MainWindow)
        self.actionSwitchAccount.setObjectName(_fromUtf8("actionSwitchAccount"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionYouchat = QtGui.QAction(MainWindow)
        self.actionYouchat.setObjectName(_fromUtf8("actionYouchat"))
        self.actionUpdate = QtGui.QAction(MainWindow)
        self.actionUpdate.setObjectName(_fromUtf8("actionUpdate"))
        self.actionAuthor = QtGui.QAction(MainWindow)
        self.actionAuthor.setObjectName(_fromUtf8("actionAuthor"))
        self.actionUseHelp = QtGui.QAction(MainWindow)
        self.actionUseHelp.setObjectName(_fromUtf8("actionUseHelp"))
        self.toolBar.addAction(self.actionFriend)
        self.menuAccount.addAction(self.actionSwitchAccount)
        self.menuAccount.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionUseHelp)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addAction(self.actionYouchat)
        self.menuHelp.addAction(self.actionAuthor)
        self.menuBar.addAction(self.menuAccount.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.searchUserName.setText(_translate("MainWindow", "查找", None))
        self.pushButtonGroupChat.setText(_translate("MainWindow", "发起群聊", None))
        self.pushButtonRefresh.setText(_translate("MainWindow", "刷新好友", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.menuAccount.setTitle(_translate("MainWindow", "账户", None))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助", None))
        self.actionFriend.setText(_translate("MainWindow", "我的好友", None))
        self.actionFriend.setToolTip(_translate("MainWindow", "我的好友", None))
        self.actionSwitchAccount.setText(_translate("MainWindow", "切换账户", None))
        self.actionSwitchAccount.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionQuit.setText(_translate("MainWindow", "退出", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Alt+X", None))
        self.actionYouchat.setText(_translate("MainWindow", "关于YouChat", None))
        self.actionYouchat.setShortcut(_translate("MainWindow", "Ctrl+Y", None))
        self.actionUpdate.setText(_translate("MainWindow", "软件更新", None))
        self.actionUpdate.setShortcut(_translate("MainWindow", "Ctrl+U", None))
        self.actionAuthor.setText(_translate("MainWindow", "关于作者", None))
        self.actionAuthor.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.actionUseHelp.setText(_translate("MainWindow", "使用说明", None))
        self.actionUseHelp.setShortcut(_translate("MainWindow", "F1", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

