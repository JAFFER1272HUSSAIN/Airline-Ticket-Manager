# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crudofUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(694, 579)
        Form.setStyleSheet("background-color: rgb(104, 38, 38);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 651, 392))
        self.tableWidget.setStyleSheet("colo:rgb(255, 255, 255);\n"
"background-color: rgb(104, 38, 38);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.graph_bt_2 = QtWidgets.QPushButton(Form)
        self.graph_bt_2.setGeometry(QtCore.QRect(230, 510, 251, 51))
        self.graph_bt_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.graph_bt_2.setObjectName("graph_bt_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(240, 30, 251, 51))
        self.plainTextEdit.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(99, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"border-color: rgb(104, 38, 38);\n"
"border:1px solid  rgb(99, 0, 0);")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Flight#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Pilot"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Seats"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "From"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "To"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Time"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "class"))
        self.graph_bt_2.setText(_translate("Form", "Book Flight"))
        self.plainTextEdit.setPlainText(_translate("Form", "Available Flights"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
