

from PyQt5 import QtCore, QtGui, QtWidgets


class Calender(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(978, 665)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(-5, 0, 981, 651))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MIDWAY DRIVING SCHOOL 2020"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Calender()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
