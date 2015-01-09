import sys
from PyQt4 import QtGui, QtCore

class myTextBrowser(QtGui.QTextBrowser):
    def __init__(self,path,parent =None):
        QtGui.QTextBrowser.__init__(self)
        self.path =path
    def loadResource (self, type, name):
        return QtGui.QPixmap(self.path)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    a = myTextBrowser("expression/01.png")

    a.append("hi")
    a.append("""My image :<br /><img src="test.jpg"/>""")
    a.show()
    sys.exit(app.exec_())