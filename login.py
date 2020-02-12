import sqlite3
from admin import *

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(651, 658)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, -10, 671, 671))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Screenshot from 2020-01-28 13-55-45.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(260, 530, 251, 71))
        self.login.setStyleSheet("font: bold;\n"
"font-size: 25px;\n"
"color: white;\n"
"background-color: grey;")
        self.login.setObjectName("login")
        ####
        self.login.clicked.connect(self.openAdmin)
        ####
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 161, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 370, 181, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(180, 60, 311, 101))
        self.label_4.setObjectName("label_4")
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(220, 240, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(220, 370, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def record(self):
        username = self.username.text()
        password = self.password.text()
        
        conn = sqlite3.connect("midway.db")
        cur = conn.cursor()
        
        cur.execute("INSERT INTO logins VALUES (?,?)",(username,password))
        
        conn.commit()
        conn.close()
        
    def openAdmin(self):
        self.record()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        Form.hide()
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MIDWAY DRIVING SCHOOL 2020"))
        self.login.setText(_translate("Form", "LOGIN"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#204a87;\">USERNAME</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#204a87;\">PASSWORD</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:72pt; font-weight:600; color:#204a87;\">LOGIN</span></p></body></html>"))
        self.username.setPlaceholderText(_translate("Form", "Enter username here"))
        self.password.setPlaceholderText(_translate("Form", "Enter password here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
