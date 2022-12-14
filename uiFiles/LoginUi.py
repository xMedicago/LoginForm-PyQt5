# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 565)
        Form.setStyleSheet("QPushButton#btn_login{\n"
                           "    background-color: rgb(85, 85, 255);\n"
                           "    border-radius: 7px;\n"
                           "}\n"
                           "\n"
                           "QPushButton#btn_login:hover{\n"
                           "    background-color: rgb(85, 255, 0);\n"
                           "}\n"
                           "\n"
                           "QPushButton#btn_login:pressed{\n"
                           "    padding-left: 5px;\n"
                           "    padding-top: 5px;\n"
                           "    background-color: rgba(150, 123, 111, 255);\n"
                           "}\n"
                           "\n"
                           "QPushButton#GitHub{\n"
                           "    background-color: rgba(0, 0, 0, 0);\n"
                           "    color: rgba(85, 98, 112, 255);\n"
                           "    border-radius: 7px;\n"
                           "}\n"
                           "\n"
                           "QPushButton#GitHub:hover{\n"
                           "    background-color: #a0a0a0;\n"
                           "}\n"
                           "\n"
                           "QPushButton#GitHub:pressed{\n"
                           "    padding-left: 5px;\n"
                           "    padding-top: 5px;\n"
                           "}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.widget.setStyleSheet("background-image: url(:/images/images/bg.jpg);\n"
                                  "border-top-left-radius: 50px;")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 170, 231, 81))
        self.label_3.setStyleSheet("border-top-left-radius: 0px;\n"
                                   "background-color: rgba(0, 0, 0, 75);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.name = QtWidgets.QLabel(self.widget)
        self.name.setGeometry(QtCore.QRect(10, 180, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.authorization_form = QtWidgets.QLabel(Form)
        self.authorization_form.setGeometry(QtCore.QRect(270, 30, 240, 430))
        self.authorization_form.setStyleSheet("background-color: rgba(255, 255, 255, 255);\n"
                                              "border-bottom-right-radius: 50px;")
        self.authorization_form.setText("")
        self.authorization_form.setObjectName("authorization_form")
        self.form_name = QtWidgets.QLabel(Form)
        self.form_name.setGeometry(QtCore.QRect(340, 80, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.form_name.setFont(font)
        self.form_name.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.form_name.setObjectName("form_name")
        self.input_login = QtWidgets.QLineEdit(Form)
        self.input_login.setGeometry(QtCore.QRect(295, 150, 190, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_login.setFont(font)
        self.input_login.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                       "color: rgba(0, 0, 0, 240);\n"
                                       "padding-left: 2px;\n"
                                       "padding-bottom: 5px;")
        self.input_login.setInputMask("")
        self.input_login.setText("")
        self.input_login.setObjectName("input_login")
        self.input_password = QtWidgets.QLineEdit(Form)
        self.input_password.setGeometry(QtCore.QRect(295, 220, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.input_password.setFont(font)
        self.input_password.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                          "border: none;\n"
                                          "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                          "color: rgba(0, 0, 0, 240);\n"
                                          "padding-left: 2px;\n"
                                          "padding-bottom: 5px;")
        self.input_password.setText("")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_password.setClearButtonEnabled(True)
        self.input_password.setObjectName("input_password")
        self.btn_login = QtWidgets.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(295, 295, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("")
        self.btn_login.setObjectName("btn_login")
        self.GitHub = QtWidgets.QPushButton(Form)
        self.GitHub.setGeometry(QtCore.QRect(370, 410, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.GitHub.setFont(font)
        self.GitHub.setStyleSheet("")
        self.GitHub.setCheckable(False)
        self.GitHub.setChecked(False)
        self.GitHub.setAutoRepeat(False)
        self.GitHub.setAutoExclusive(False)
        self.GitHub.setAutoDefault(False)
        self.GitHub.setDefault(False)
        self.GitHub.setObjectName("GitHub")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "by xMedlcago"))
        self.form_name.setText(_translate("Form", "Log In"))
        self.input_login.setPlaceholderText(_translate("Form", "Login"))
        self.input_password.setPlaceholderText(_translate("Form", "Password"))
        self.btn_login.setText(_translate("Form", "Log In"))
        self.GitHub.setText(_translate("Form", ")"))


import res_rc
