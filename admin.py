import sqlite3
from calender import *
from register import *

from PyQt5 import QtCore, QtGui, QtWidgets

conn = sqlite3.connect("midway.db")

cur = conn.cursor()
    
final = cur.execute("SELECT * FROM admins")

for x in final:
    name  = x[0] 
    surname = x[1]
    contact = x[2]
    address = x[3]
    username = x[4]

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1418, 819)
        MainWindow.setStyleSheet("*\n"
"{\n"
"    color: black;\n"
"    font: bold;\n"
"}\n"
"\n"
"#add\n"
"{\n"
"    color : white;\n"
"    background-color: blue;\n"
"    font-size: 20px;\n"
"    font: bold;\n"
"}\n"
"\n"
"#progress\n"
"{\n"
"    color : white;\n"
"    background-color: green;\n"
"    font-size: 20px;\n"
"    font: bold;\n"
"}\n"
"\n"
"#calender\n"
"{\n"
"    color : white;\n"
"    background-color: red;\n"
"    font-size: 20px;\n"
"    font: bold;\n"
"}\n"
"\n"
"#remove\n"
"{\n"
"    color : white;\n"
"    background-color: brown;\n"
"    font-size: 20px;\n"
"    font: bold;\n"
"}\n"
"#exit\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"    font: bold;\n"
"}\n"
"#line1\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: red;\n"
"}\n"
"\n"
"#line2\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: red;\n"
"}\n"
"\n"
"#line3\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: red;\n"
"}\n"
"\n"
"#line4\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: red;\n"
"}\n"
"\n"
"#line5\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: red;\n"
"}\n"
"#line6\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: red;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(10, 60, 431, 51))
        self.line1.setObjectName("line1")
        self.line3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(10, 110, 431, 51))
        self.line3.setObjectName("line3")
        self.line6 = QtWidgets.QLineEdit(self.centralwidget)
        self.line6.setGeometry(QtCore.QRect(10, 210, 431, 51))
        self.line6.setObjectName("line6")
        self.line5 = QtWidgets.QLineEdit(self.centralwidget)
        self.line5.setGeometry(QtCore.QRect(10, 160, 431, 51))
        self.line5.setObjectName("line5")
        self.line4 = QtWidgets.QLineEdit(self.centralwidget)
        self.line4.setGeometry(QtCore.QRect(10, 260, 431, 51))
        self.line4.setObjectName("line4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(440, 9, 961, 761))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.exit = QtWidgets.QPushButton(self.frame)
        self.exit.setGeometry(QtCore.QRect(770, 700, 151, 51))
        self.exit.setObjectName("exit")
        self.calender = QtWidgets.QPushButton(self.frame)
        self.calender.setGeometry(QtCore.QRect(60, 390, 341, 261))
        self.calender.setObjectName("calender")
        self.add = QtWidgets.QPushButton(self.frame)
        self.add.setGeometry(QtCore.QRect(60, 50, 341, 261))
        self.add.setObjectName("add")
        self.remove = QtWidgets.QPushButton(self.frame)
        self.remove.setGeometry(QtCore.QRect(550, 50, 341, 261))
        self.remove.setObjectName("remove")
        self.progress = QtWidgets.QPushButton(self.frame)
        self.progress.setGeometry(QtCore.QRect(550, 390, 341, 261))
        self.progress.setObjectName("progress")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1418, 22))
        self.menubar.setObjectName("menubar")
        self.menuADMIN = QtWidgets.QMenu(self.menubar)
        self.menuADMIN.setObjectName("menuADMIN")
        self.menuSTATISTICS = QtWidgets.QMenu(self.menuADMIN)
        self.menuSTATISTICS.setObjectName("menuSTATISTICS")
        self.menuRESULT_CHECK = QtWidgets.QMenu(self.menuADMIN)
        self.menuRESULT_CHECK.setObjectName("menuRESULT_CHECK")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLOGOUT_2 = QtWidgets.QAction(MainWindow)
        self.actionLOGOUT_2.setObjectName("actionLOGOUT_2")
        self.actionLOG = QtWidgets.QAction(MainWindow)
        self.actionLOG.setObjectName("actionLOG")
        self.actionVERIFY_RESULTS = QtWidgets.QAction(MainWindow)
        self.actionVERIFY_RESULTS.setObjectName("actionVERIFY_RESULTS")
        self.actionPUBLISH_RESULTS = QtWidgets.QAction(MainWindow)
        self.actionPUBLISH_RESULTS.setObjectName("actionPUBLISH_RESULTS")
        self.menuSTATISTICS.addSeparator()
        self.menuSTATISTICS.addAction(self.actionLOG)
        self.menuRESULT_CHECK.addAction(self.actionVERIFY_RESULTS)
        self.menuRESULT_CHECK.addAction(self.actionPUBLISH_RESULTS)
        self.menuADMIN.addAction(self.menuRESULT_CHECK.menuAction())
        self.menuADMIN.addAction(self.menuSTATISTICS.menuAction())
        self.menuADMIN.addAction(self.actionLOGOUT_2)
        self.menubar.addAction(self.menuADMIN.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.calender.clicked.connect(self.enterCalender)
        self.add.clicked.connect(self.enterRegister)
        
        ###
        self.line3.setText(name.upper()+ " "+surname.upper())
        self.line6.setText(str(contact) + " / 3918800")
        self.line4.setText(address.upper())
        self.line5.setText(username)
        self.line1.setText("Admin 1")
#        self.line6.setText()
        ###
        
    def enterRegister(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Register()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()
    
    def enterCalender(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Calender()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MIDWAY DRIVING SCHOOL 2020"))
        self.exit.setText(_translate("MainWindow", "EXIT"))
        self.calender.setText(_translate("MainWindow", "CALENDER"))
        self.add.setText(_translate("MainWindow", "REGISTER STUDENT"))
        self.remove.setText(_translate("MainWindow", "REMOVE STUDENT"))
        self.progress.setText(_translate("MainWindow", "PROGRESS"))
        self.menuADMIN.setTitle(_translate("MainWindow", "ADMIN"))
        self.menuSTATISTICS.setTitle(_translate("MainWindow", "STATISTICS"))
        self.menuRESULT_CHECK.setTitle(_translate("MainWindow", "RESULT CHECK"))
        self.actionLOGOUT_2.setText(_translate("MainWindow", "LOGOUT"))
        self.actionLOG.setText(_translate("MainWindow", "LOG"))
        self.actionVERIFY_RESULTS.setText(_translate("MainWindow", "VERIFY RESULTS"))
        self.actionPUBLISH_RESULTS.setText(_translate("MainWindow", "PUBLISH RESULTS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
