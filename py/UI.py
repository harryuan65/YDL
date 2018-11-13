# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(478, 351)
        self.pb_dl = QtWidgets.QPushButton(Form)
        self.pb_dl.setGeometry(QtCore.QRect(360, 250, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pb_dl.setFont(font)
        self.pb_dl.setObjectName("pb_dl")
        self.te_url = QtWidgets.QTextEdit(Form)
        self.te_url.setGeometry(QtCore.QRect(100, 30, 231, 31))
        self.te_url.setObjectName("te_url")
        self.lb_url = QtWidgets.QLabel(Form)
        self.lb_url.setGeometry(QtCore.QRect(30, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Headline R")
        font.setPointSize(15)
        self.lb_url.setFont(font)
        self.lb_url.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lb_url.setObjectName("lb_url")
        self.lb_ext = QtWidgets.QLabel(Form)
        self.lb_ext.setGeometry(QtCore.QRect(30, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Headline R")
        font.setPointSize(15)
        self.lb_ext.setFont(font)
        self.lb_ext.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lb_ext.setObjectName("lb_ext")
        self.pb_mp3 = QtWidgets.QPushButton(Form)
        self.pb_mp3.setGeometry(QtCore.QRect(120, 100, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb_mp3.setFont(font)
        self.pb_mp3.setObjectName("pb_mp3")
        self.pb_mp4 = QtWidgets.QPushButton(Form)
        self.pb_mp4.setGeometry(QtCore.QRect(220, 100, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pb_mp4.setFont(font)
        self.pb_mp4.setObjectName("pb_mp4")
        self.lb_display = QtWidgets.QLabel(Form)
        self.lb_display.setGeometry(QtCore.QRect(30, 210, 291, 111))
        self.lb_display.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lb_display.setText("")
        self.lb_display.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_display.setObjectName("lb_display")
        self.lb_console = QtWidgets.QLabel(Form)
        self.lb_console.setGeometry(QtCore.QRect(30, 170, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lb_console.setFont(font)
        self.lb_console.setObjectName("lb_console")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_dl.setText(_translate("Form", "Download"))
        self.lb_url.setText(_translate("Form", "Url:"))
        self.lb_ext.setText(_translate("Form", "Ext."))
        self.pb_mp3.setText(_translate("Form", "mp3"))
        self.pb_mp4.setText(_translate("Form", "mp4"))
        self.lb_console.setText(_translate("Form", "Console"))

