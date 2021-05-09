# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

#import winsound
import random
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(820, 569)
        self.font = QtGui.QFont()
        self.font.setPointSize(9)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.fontpicked = QtGui.QFont()
        self.fontpicked.setPointSize(14)
        self.fontpicked.setBold(True)
        self.fontpicked.setWeight(90)
        self.layoutWidget_3 = QtWidgets.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 310, 551, 161))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_28.setAutoFillBackground(True)
        self.label_28.setText("")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_4.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_29.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_4.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_30.setAutoFillBackground(True)
        self.label_30.setText("")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_4.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_31.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_4.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_32.setAutoFillBackground(True)
        self.label_32.setText("")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_4.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_33.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_4.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_34.setAutoFillBackground(True)
        self.label_34.setText("")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_4.addWidget(self.label_34)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_35.setAutoFillBackground(True)
        self.label_35.setText("")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_4.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_36.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_4.addWidget(self.label_36)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_37 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_37.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_5.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_38.setAutoFillBackground(True)
        self.label_38.setText("")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_5.addWidget(self.label_38)
        self.label_39 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_39.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_5.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_40.setAutoFillBackground(True)
        self.label_40.setText("")
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_5.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_41.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_41.setText("")
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_5.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_42.setAutoFillBackground(True)
        self.label_42.setText("")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_5.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_43.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_5.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_44.setAutoFillBackground(True)
        self.label_44.setText("")
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_5.addWidget(self.label_44)
        self.label_45 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_45.setAutoFillBackground(True)
        self.label_45.setText("")
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_5.addWidget(self.label_45)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_46 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_46.setAutoFillBackground(True)
        self.label_46.setText("")
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.horizontalLayout_6.addWidget(self.label_46)
        self.label_47 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_47.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.horizontalLayout_6.addWidget(self.label_47)
        self.label_48 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_48.setAutoFillBackground(True)
        self.label_48.setText("")
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.horizontalLayout_6.addWidget(self.label_48)
        self.label_49 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_49.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.horizontalLayout_6.addWidget(self.label_49)
        self.label_50 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_50.setAutoFillBackground(True)
        self.label_50.setText("")
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_6.addWidget(self.label_50)
        self.label_51 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_51.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_51.setText("")
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_6.addWidget(self.label_51)
        self.label_52 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_52.setAutoFillBackground(True)
        self.label_52.setText("")
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.horizontalLayout_6.addWidget(self.label_52)
        self.label_53 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_53.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_53.setText("")
        self.label_53.setObjectName("label_53")
        self.horizontalLayout_6.addWidget(self.label_53)
        self.label_54 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_54.setAutoFillBackground(True)
        self.label_54.setText("")
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_6.addWidget(self.label_54)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.label_55 = QtWidgets.QLabel(Form)
        self.label_55.setGeometry(QtCore.QRect(26, 249, 121, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_55.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(26)
        self.label_55.setFont(font)
        self.label_55.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_55.setAutoFillBackground(True)
        self.label_55.setStyleSheet("")
        self.label_55.setLineWidth(10)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(Form)
        self.label_56.setGeometry(QtCore.QRect(20, 10, 121, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        self.label_56.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(26)
        self.label_56.setFont(font)
        self.label_56.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_56.setAutoFillBackground(True)
        self.label_56.setStyleSheet("")
        self.label_56.setLineWidth(10)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(Form)
        self.label_57.setGeometry(QtCore.QRect(700, 40, 101, 20))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(12)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(Form)
        self.label_58.setGeometry(QtCore.QRect(720, 80, 51, 31))
        self.label_58.setAutoFillBackground(True)
        self.label_58.setFont(self.fontpicked)
        self.label_58.setText("")
        self.label_58.setObjectName("label_58")
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 70, 551, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAutoFillBackground(True)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setAutoFillBackground(True)
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setAutoFillBackground(True)
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setAutoFillBackground(True)
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setAutoFillBackground(True)
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setAutoFillBackground(True)
        self.label_15.setText("")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setAutoFillBackground(True)
        self.label_17.setText("")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setAutoFillBackground(True)
        self.label_18.setText("")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setAutoFillBackground(True)
        self.label_19.setText("")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_3.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_3.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setAutoFillBackground(True)
        self.label_21.setText("")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_3.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_3.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setAutoFillBackground(True)
        self.label_23.setText("")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_3.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_3.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setAutoFillBackground(True)
        self.label_25.setText("")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_3.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.widget)
        self.label_26.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_3.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.widget)
        self.label_27.setAutoFillBackground(True)
        self.label_27.setText("")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_3.addWidget(self.label_27)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(620, 130, 77, 121))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(590, 330, 206, 81))
        self.widget2.setObjectName("widget2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_60 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.gridLayout.addWidget(self.label_60, 0, 0, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.gridLayout.addWidget(self.label_59, 0, 1, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.widget2)
        self.label_63.setAutoFillBackground(False)
        self.label_63.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_63.setText("")
        self.label_63.setObjectName("label_63")
        self.gridLayout.addWidget(self.label_63, 1, 0, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.widget2)
        self.label_62.setAutoFillBackground(False)
        self.label_62.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_62.setText("")
        self.label_62.setObjectName("label_62")
        self.gridLayout.addWidget(self.label_62, 1, 1, 1, 1)
        self.label_65 = QtWidgets.QLabel(Form)
        self.label_65.setGeometry(QtCore.QRect(130, 500, 135, 40))
        self.label_65.setAutoFillBackground(False)
        self.label_65.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_65.setText("")
        self.label_65.setObjectName("label_65")
        
        
        self.pushButton_3.clicked.connect(self.FillingEmptySlots)
        self.pushButton_4.clicked.connect(self.NumberPick)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_55.setText(_translate("Form", "Player 2"))
        self.label_56.setText(_translate("Form", "Player 1"))
        self.label_57.setText(_translate("Form", "Picked Number"))
        self.pushButton_3.setText(_translate("Form", "InitializeCard"))
        self.pushButton_4.setText(_translate("Form", "Pick"))
        self.label_60.setText(_translate("Form", "Player 1 Score"))
        self.label_59.setText(_translate("Form", "Player 2 Score"))
   
    def FillingEmptySlots(self):
        self.first_team=0
        self.second_team=0
        self.label_63.setText(str(self.first_team))
        self.label_62.setText(str(self.second_team))
        self.random_numbers=[]
        count=0
        while count<15:
            numbers=random.randint(1,91)
            if numbers not in self.random_numbers:
                self.random_numbers.append(numbers)
                count=count + 1              
        print(self.random_numbers)
        
        # I need list for Player 1 Empty Slots and I will turn it in for loop
        self.labelslist1=[self.label,self.label_3,self.label_5,self.label_7,self.label_8,
                     self.label_11,self.label_13,self.label_15,self.label_17,self.label_18,
                     self.label_19,self.label_21,self.label_23,self.label_25,self.label_27]
    
        for i in range(15):
                self.labelslist1[i].setText(str(self.random_numbers[i])) #FILLING SLOTS WITH RANDOM NUMBERS

        self.random_numbers2=[]
        count2=0
        while count2<15:
            numbers2=random.randint(1,90)
            if numbers2 not in self.random_numbers2:
                self.random_numbers2.append(numbers2)
                count2=count2 + 1
        print(self.random_numbers2)
        # I need list for Player 2 Empty Slots and I will turn it in for loop
        self.labelslist2=[self.label_28,self.label_30,self.label_32,self.label_34,self.label_35,
                     self.label_38,self.label_40,self.label_42,self.label_44,self.label_45,
                     self.label_46,self.label_48,self.label_50,self.label_52,self.label_54]
        
        for j in range(15):
                self.labelslist2[j].setText(str(self.random_numbers2[j])) #FILLING SLOTS WITH RANDOM NUMBERS
        
        self.picklist=[]
        for a in range(1,91):
        #It is out of NumberPick()  because if this for is in function 
        #we have always same a from 1 to 90.
        #Now a's number of staff is gonna be decreased
            self.picklist.append(a) 
            
        self.Row1Cinko=0
        self.Row2Cinko=0
        self.Row3Cinko=0
        self.Row4Cinko=0
        self.Row5Cinko=0
        self.Row6Cinko=0
        #Cinkos need to be out of functions too because we need to up theirs values
        
        
        self.Control1 = False ; self.Control2 = False ; self.Control3 = False
        self.Control4 = False ; self.Control5 = False ; self.Control6 = False
        self.First_Cinko = False ; self.Second_Cinko = False ; self.Third_Cinko = False
        self.Fourth_Cinko = False ; self.Fifth_Cinko = False ; self.Sixth_Cinko = False
        #If these ones are in NumberPick() I cannot control the points.
        
    def NumberPick(self):
 
        self.Row1=self.labelslist1[0:5] # first 5 values from QT
        self.Row2=self.labelslist1[5:10]
        self.Row3=self.labelslist1[10:15]
        self.Row4=self.labelslist2[0:5]
        self.Row5=self.labelslist2[5:10]
        self.Row6=self.labelslist2[10:15]
        
        left_number=len(self.picklist) - 1 #NUMBER OF RANDOM IS MISSING STEP BY STEP SO WE SHOW THEM BY USING IT
    
        self.picked_number=self.picklist.pop(random.randint(0,left_number))#GET PICKED NUMBER RANDOM
        
        print(self.picklist)
        print(self.picked_number)
        
        self.label_58.setText(str(self.picked_number))
        
        #CHECKING CINKOS
        for i in range(5):
            if self.Row1[i].text()==str(self.picked_number):
                self.Row1[i].setFont(self.font)
                self.Row1Cinko+=1
                print(self.Row1Cinko)
                if self.Row1Cinko==5:
                     self.Control1=True
                break
        for i in range(5):
            if self.Row2[i].text()==str(self.picked_number):
                self.Row2[i].setFont(self.font)
                self.Row2Cinko+=1
                if self.Row2Cinko==5:
                    self.Control2=True
                break
        for i in range(5):
            if self.Row3[i].text()==str(self.picked_number):
                self.Row3[i].setFont(self.font)
                self.Row3Cinko+=1
                if self.Row3Cinko==5:
                    self.Control3=True
                break
        for i in range(5):
            if self.Row4[i].text()==str(self.picked_number):
                self.Row4[i].setFont(self.font)
                self.Row4Cinko+=1
                if self.Row4Cinko==5:
                    self.Control4=True
                break
        for i in range(5):
            if self.Row5[i].text()==str(self.picked_number):
                self.Row5[i].setFont(self.font)
                self.Row5Cinko+=1
                if self.Row5Cinko==5:
                    self.Control5=True
                break
        for i in range(5):
            if self.Row6[i].text()==str(self.picked_number):
                self.Row6[i].setFont(self.font)
                self.Row6Cinko+=1
                if self.Row6Cinko==5:
                    self.Control6=True                
                break    
            
            
        #FOR PRINTING CINKOS TO THE SCREEN
        if self.Control1 == True or self.Control2 == True or self.Control3 == True:
            if self.First_Cinko==False:
                self.First_Cinko=True
                self.first_team+=10
                #winsound.PlaySound("Mario", winsound.SND_FILENAME)
                self.label_65.setFont(self.font)
                self.label_65.setAlignment(QtCore.Qt.AlignCenter)
                self.label_65.setText("Player 1 First Cinko")
                
        if self.Control4 == True or self.Control5 == True or self.Control6 == True:
            if self.Fourth_Cinko==False:
                self.Fourth_Cinko=True
                self.second_team+=10
               # winsound.PlaySound("Mario", winsound.SND_FILENAME)
               #It is for fun but when it works the program's speed is gonna be slow
                self.label_65.setFont(self.font)
                self.label_65.setAlignment(QtCore.Qt.AlignCenter)
                self.label_65.setText("Player 2 First Cinko")
                
        if (self.Control1 and self.Control2)==True or(self.Control1 and self.Control3)==True or(self.Control2 and self.Control3)==True:
            if self.Second_Cinko==False:
                self.Second_Cinko=True
                self.first_team+=20
                #winsound.PlaySound("Mario", winsound.SND_FILENAME)
                #It is for fun but when it works the program's speed is gonna be slow
                self.label_65.setFont(self.font)
                self.label_65.setAlignment(QtCore.Qt.AlignCenter)
                self.label_65.setText("Player 1 Second Cinko")

            
        if (self.Control4 and self.Control5)==True or(self.Control4 and self.Control6)==True or(self.Control5 and self.Control6)==True:
            if self.Fifth_Cinko==False:
                self.Fifth_Cinko=True
                self.second_team+=20
               #winsound.PlaySound("Mario", winsound.SND_FILENAME)
               #It is for fun but when it works the program's speed is gonna be slow
                self.label_65.setFont(self.font)
                self.label_65.setAlignment(QtCore.Qt.AlignCenter)
                self.label_65.setText("Player 2 Second Cinko")
            
        if self.Control1 == True and self.Control2 == True and self.Control3 == True:
            if self.Third_Cinko==False:
                self.Third_Cinko=True
                self.first_team+=40
               #winsound.PlaySound("Mario", winsound.SND_FILENAME)
               #It is for fun but when it works the program's speed is gonna be slow
                
        if self.Control4==True and self.Control5 == True and self.Control6 == True:
            if self.Sixth_Cinko==False:
                self.Sixth_Cinko=True
                self.second_team+=40
               #winsound.PlaySound("Mario", winsound.SND_FILENAME)
               #It is for fun but when it works the program's speed is gonna be slow
                
        
        self.label_63.setText(str(self.first_team))
        self.label_62.setText(str(self.second_team))
        
        #COMPARING PLAYER 1 AND 2
        if self.first_team==70:
            if self.second_team !=70:
                self.label_65.setGeometry(QtCore.QRect(130, 500, 105, 40))
                self.label_65.setAlignment(QtCore.Qt.AlignCenter)
                self.label_65.setStyleSheet("background-color: rgb(255, 0, 0);") # RED TEAM
                self.label_65.setFont(self.font)
                self.label_65.setText("Player 1 Tombala")
        if self.second_team==70:
            if self.first_team !=70:
                self.label_65.setGeometry(QtCore.QRect(130, 500, 105, 40))
                self.label_65.setAlignment(QtCore.Qt.AlignCenter)
                self.label_65.setStyleSheet("background-color: rgb(0, 0, 255);") # BLUE TEAM
                self.label_65.setFont(self.font)
                self.label_65.setText("Player 2 Tombala")
        if self.first_team==70 and self.second_team==70:
                self.label_65.setGeometry(QtCore.QRect(130, 500, 95, 40))
                self.label_65.setAlignment(QtCore.Qt.AlignCenter)
                self.label_65.setStyleSheet("background-color: rgb(0, 255, 0);") # PEACE :) 
                self.label_65.setFont(self.font)
                self.label_65.setText("TIE !")