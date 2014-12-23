#! C:/Program Files (x86)/Python27
# -*- coding: utf-8 -*-
# Project	  	:计网大作业
# Module		:loginUI.py
# Description	:UI界面设计
# Author	  	:Changsheng Zhang 
# Last edited 	:2014/12/15 10:30

from PyQt4 import QtGui
from PyQt4 import QtCore
import userMainWindow  
#from time import clock

class LoginDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setWindowTitle(u'YouChat Login')
        self.resize(500, 300)
        
        self.userName =[]
        self.passWord =[]

        f = open("log/cookies.youchat")
        line = str(f.readline())
        self.userNum = 0
        self.passNum = 0
        while line:
            #是否有记住密码
            #记住密码
            temp =line.split(" ")
            if len(temp)==2:
                self.userName.append(temp[0])
                self.userNum =self.userNum+1
                temp2 = temp[1].split("\n")
                self.passWord.append(temp2[0])
                self.passNum =self.passNum+1
            #没有记住密码
            else:
                temp3 =line.split("\n")
                self.userName.append(temp3[0])
                self.userNum =self.userNum+1
                self.passWord.append("")
            line =f.readline()

        f.close()

        self.leName = QtGui.QLineEdit(self)
        
        if(self.userNum!=0):
            self.leName.setText(self.userName[0])
            #self.leName.setPlaceholderText(self.userName[0])
        else:
            self.leName.setPlaceholderText(u'请输入账号')
        
        self.lePassword = QtGui.QLineEdit(self)
        self.lePassword.setEchoMode(QtGui.QLineEdit.Password)
        
        if(self.passNum!=0):
            #self.lePassword.setPlaceholderText(self.passWord[0])
            self.lePassword.setText(str(self.passWord[0]))
        else:
            self.lePassword.setPlaceholderText(u'请输入密码')
        
        self.pbLogin = QtGui.QPushButton(u'登录', self)
        self.pbCancel = QtGui.QPushButton(u'取消', self)
        
        self.remAccount = QtGui.QCheckBox(u"记住账号",self)
        self.remPassword = QtGui.QCheckBox(u"记住密码",self)

        self.remAccount.toggle()
        self.remPassword.toggle()

        self.remAccount.stateChanged.connect(self.changeRemAcc)
        self.remPassword.stateChanged.connect(self.changeRemPass)


        self.pbLogin.clicked.connect(self.login)
        self.pbCancel.clicked.connect(self.reject)
        
        self.loginIcon = QtGui.QLabel(self)
        self.loginIcon.setPixmap(QtGui.QPixmap("img/loginIcon.png"))

        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.leName)
        layout.addWidget(self.lePassword)
 
        #复选框布局
        checkBoxLayout = QtGui.QHBoxLayout()
        spancerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        checkBoxLayout.addItem(spancerItem)
        checkBoxLayout.addWidget(self.remAccount)
        checkBoxLayout.addWidget(self.remPassword)

        layout.addLayout(checkBoxLayout)


        # 放一个间隔对象美化布局
        spacerItem = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
        

        # 按钮布局
        buttonLayout = QtGui.QHBoxLayout()
        # 左侧放一个间隔
        spancerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        buttonLayout.addItem(spancerItem2)
        buttonLayout.addWidget(self.pbLogin)
        buttonLayout.addWidget(self.pbCancel)
 
        layout.addLayout(buttonLayout)
        
        grid =QtGui.QGridLayout()
        grid.addWidget(self.loginIcon,0,0)

        mainLayout = QtGui.QGridLayout(self)
        mainLayout.setMargin(15)
        mainLayout.setSpacing(10)
        mainLayout.addLayout(grid,0,0)
        mainLayout.addLayout(layout,0,1)

        grid.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        self.setLayout(mainLayout)
    
    def changeRemAcc(self,state):
        if self.remAccount.isChecked()==False:
            self.remPassword.setChecked(False)

    def changeRemPass(self,state):
        if self.remPassword.isChecked()==True:
            self.remAccount.setChecked(True)


    def login(self):
        #print 'login'
        if str(self.leName.text()) == '2012011420' and str(self.lePassword.text()) == 'net2014':
            if self.remAccount.isChecked():
                f1= open('log/cookies.youchat','w')
                f1.write(str(self.leName.text()))
                if self.remPassword.isChecked():
                    f1.write(" "+str(self.lePassword.text()))
                f1.write("\n")
                f1.close()
            self.accept() # 关闭对话框并返回1
        else:
            QtGui.QMessageBox.critical(self, u'错误', u'用户名密码不匹配')

    def getleName(self):
        return str(self.leName.text())
'''
def login():
    """返回True或False"""
    dialog = LoginDialog()
    if dialog.exec_():
        return True
    else:
        return False
''' 
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    dialog = LoginDialog()

    if dialog.exec_():
        userName = dialog.getleName()
        #MainWindow = QtGui.QMainWindow()
        ui = userMainWindow.UserMainWindow()
        #ui.setupUi(MainWindow,userName)
        #MainWindow.show()
        ui.show()
        sys.exit(app.exec_())