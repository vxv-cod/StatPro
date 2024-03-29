# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'okno.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 545)
        Form.setMinimumSize(QtCore.QSize(620, 545))
        Form.setMaximumSize(QtCore.QSize(620, 545))
        Form.setSizeIncrement(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox_1 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_1.setChecked(True)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout_4.addWidget(self.checkBox_1, 0, 0, 1, 1)
        self.progressBar_12 = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar_12.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_12.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_12.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_12.setMinimum(0)
        self.progressBar_12.setMaximum(100)
        self.progressBar_12.setProperty("value", 0)
        self.progressBar_12.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_12.setTextVisible(False)
        self.progressBar_12.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_12.setObjectName("progressBar_12")
        self.gridLayout_4.addWidget(self.progressBar_12, 1, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_4.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.progressBar_13 = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar_13.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_13.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_13.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_13.setMinimum(0)
        self.progressBar_13.setMaximum(100)
        self.progressBar_13.setProperty("value", 0)
        self.progressBar_13.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_13.setTextVisible(False)
        self.progressBar_13.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_13.setObjectName("progressBar_13")
        self.gridLayout_4.addWidget(self.progressBar_13, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 22))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 0, 0, 1, 1)
        self.progressBar_14 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_14.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_14.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_14.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_14.setMinimum(0)
        self.progressBar_14.setMaximum(100)
        self.progressBar_14.setProperty("value", 0)
        self.progressBar_14.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_14.setTextVisible(False)
        self.progressBar_14.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_14.setObjectName("progressBar_14")
        self.gridLayout_3.addWidget(self.progressBar_14, 1, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_3.addWidget(self.checkBox_4, 2, 0, 1, 1)
        self.progressBar_15 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_15.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_15.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_15.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_15.setMinimum(0)
        self.progressBar_15.setMaximum(100)
        self.progressBar_15.setProperty("value", 0)
        self.progressBar_15.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_15.setTextVisible(False)
        self.progressBar_15.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_15.setObjectName("progressBar_15")
        self.gridLayout_3.addWidget(self.progressBar_15, 3, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 22))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 4, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 16))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_2.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_2.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_2.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_2.addWidget(self.progressBar_2, 3, 0, 1, 1)
        self.progressBar_9 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_9.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_9.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_9.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_9.setMinimum(0)
        self.progressBar_9.setMaximum(100)
        self.progressBar_9.setProperty("value", 0)
        self.progressBar_9.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_9.setTextVisible(False)
        self.progressBar_9.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_9.setObjectName("progressBar_9")
        self.gridLayout_2.addWidget(self.progressBar_9, 17, 0, 1, 1)
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_3.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_3.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_3.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_3.setMinimum(0)
        self.progressBar_3.setMaximum(100)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout_2.addWidget(self.progressBar_3, 5, 0, 1, 1)
        self.progressBar_7 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_7.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_7.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_7.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_7.setMinimum(0)
        self.progressBar_7.setMaximum(100)
        self.progressBar_7.setProperty("value", 0)
        self.progressBar_7.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_7.setTextVisible(False)
        self.progressBar_7.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_7.setObjectName("progressBar_7")
        self.gridLayout_2.addWidget(self.progressBar_7, 13, 0, 1, 1)
        self.progressBar_5 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_5.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_5.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_5.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_5.setMinimum(0)
        self.progressBar_5.setMaximum(100)
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_5.setObjectName("progressBar_5")
        self.gridLayout_2.addWidget(self.progressBar_5, 9, 0, 1, 1)
        self.progressBar_1 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_1.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_1.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_1.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_1.setMinimum(0)
        self.progressBar_1.setMaximum(100)
        self.progressBar_1.setProperty("value", 0)
        self.progressBar_1.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_1.setTextVisible(False)
        self.progressBar_1.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_1.setObjectName("progressBar_1")
        self.gridLayout_2.addWidget(self.progressBar_1, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setMinimumSize(QtCore.QSize(0, 33))
        self.label.setMaximumSize(QtCore.QSize(16777215, 33))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 16))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)
        self.progressBar_11 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_11.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_11.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_11.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_11.setMinimum(0)
        self.progressBar_11.setMaximum(100)
        self.progressBar_11.setProperty("value", 0)
        self.progressBar_11.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_11.setTextVisible(False)
        self.progressBar_11.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_11.setObjectName("progressBar_11")
        self.gridLayout_2.addWidget(self.progressBar_11, 21, 0, 1, 1)
        self.progressBar_10 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_10.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_10.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_10.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_10.setMinimum(0)
        self.progressBar_10.setMaximum(100)
        self.progressBar_10.setProperty("value", 0)
        self.progressBar_10.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_10.setTextVisible(False)
        self.progressBar_10.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_10.setObjectName("progressBar_10")
        self.gridLayout_2.addWidget(self.progressBar_10, 19, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 16))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setMinimumSize(QtCore.QSize(0, 16))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 18, 0, 1, 1)
        self.progressBar_6 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_6.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_6.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_6.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_6.setMinimum(0)
        self.progressBar_6.setMaximum(100)
        self.progressBar_6.setProperty("value", 0)
        self.progressBar_6.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_6.setObjectName("progressBar_6")
        self.gridLayout_2.addWidget(self.progressBar_6, 11, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setMinimumSize(QtCore.QSize(0, 16))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 14, 0, 1, 1)
        self.progressBar_4 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_4.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_4.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_4.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_4.setMinimum(0)
        self.progressBar_4.setMaximum(100)
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout_2.addWidget(self.progressBar_4, 7, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setMinimumSize(QtCore.QSize(0, 16))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 16, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setMinimumSize(QtCore.QSize(0, 16))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 20, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 33))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 33))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setMinimumSize(QtCore.QSize(0, 16))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 12, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setMinimumSize(QtCore.QSize(0, 16))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 10, 0, 1, 1)
        self.progressBar_8 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_8.setMinimumSize(QtCore.QSize(0, 8))
        self.progressBar_8.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressBar_8.setStyleSheet("QProgressBar::chunk {\n"
"    background-color: rgb(100, 150, 150);\n"
"    margin: 2px;\n"
"}")
        self.progressBar_8.setMinimum(0)
        self.progressBar_8.setMaximum(100)
        self.progressBar_8.setProperty("value", 0)
        self.progressBar_8.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_8.setTextVisible(False)
        self.progressBar_8.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_8.setObjectName("progressBar_8")
        self.gridLayout_2.addWidget(self.progressBar_8, 15, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 22))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 22, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setMinimumSize(QtCore.QSize(0, 16))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setStyleSheet("color: rgb(0, 0, 152);")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 22))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Классификация грунтов:"))
        self.checkBox_1.setText(_translate("Form", "Классификация талых грунтов:"))
        self.checkBox_2.setText(_translate("Form", "Классификация мерзлых грунтов:"))
        self.pushButton_3.setText(_translate("Form", "Кодирование грунтов"))
        self.pushButton_3.setShortcut(_translate("Form", "Return"))
        self.groupBox_2.setTitle(_translate("Form", "Сортировка грунтов по типам:"))
        self.checkBox_3.setText(_translate("Form", "Таблица рекомендуемых  показателей физико-механических свойств талых грунтов:"))
        self.checkBox_4.setText(_translate("Form", "Таблица рекомендуемых  показателей физико-механических свойств мерзлых грунтов:"))
        self.pushButton_4.setText(_translate("Form", "Сортировка по типам грунта"))
        self.pushButton_4.setShortcut(_translate("Form", "Return"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Классификация грунтов по ГОСТ 25100"))
        self.label_3.setText(_translate("Form", "Таблица 8.2 – Физико-механические свойства талых грунтов:"))
        self.label.setText(_translate("Form", "Сводная таблица рекомендуемых нормативных и расчетных значений показателей физико-механических свойств талых грунтов:"))
        self.label_4.setText(_translate("Form", "Таблица 8.3 – Сопоставление механических свойств талых грунтов:"))
        self.label_5.setText(_translate("Form", "Таблица 8.4 - Расчетные значения физико-механических свойств талых грунтов"))
        self.label_10.setText(_translate("Form", "Таблица 8.10 – Гранулометрический состав грунтов"))
        self.label_8.setText(_translate("Form", "Таблица 8.7 - Механические свойства мерзлых грунтов"))
        self.label_9.setText(_translate("Form", "Таблица 8.8 - Теплофизические свойства грунтов"))
        self.label_11.setText(_translate("Form", "Классификация грунтов по просадочности при оттаивании грунта"))
        self.label_2.setText(_translate("Form", "Сводная таблица рекомендуемых нормативных и расчетных значений показателей физико-механических свойств мерзлых грунтов:"))
        self.label_7.setText(_translate("Form", "Таблица 8.6 – Физические свойства мерзлых грунтов"))
        self.label_6.setText(_translate("Form", "Таблица 8.5 – Физико-механические свойства торфов"))
        self.pushButton.setText(_translate("Form", "Формирование таблиц статической обработки"))
        self.pushButton.setShortcut(_translate("Form", "Return"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Статобработка физико-механических свойств грунтов"))
        self.label_12.setText(_translate("Form", "Стоблцы и название вкладок в шаблоне Excel не менять..."))
        self.pushButton_2.setText(_translate("Form", "Шаблон Excel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
