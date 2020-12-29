# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\URSA_2020\Playing around with PyQt5\Day 4\ColorDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 245)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.centralwidget.setObjectName("centralwidget")

        self.colorDisplay = QtWidgets.QLabel(self.centralwidget)
        self.colorDisplay.setGeometry(QtCore.QRect(550, 50, 91, 61))
        self.colorDisplay.setFrameShape(QtWidgets.QFrame.Box)
        self.colorDisplay.setObjectName("colorDisplay")
        self.colorDisplay.setStyleSheet("background-color: red")
        

        self.redValue = QtWidgets.QLineEdit(self.centralwidget)
        self.redValue.setGeometry(QtCore.QRect(60, 60, 61, 41))
        self.redValue.setObjectName("redValue")

        self.greenValue = QtWidgets.QLineEdit(self.centralwidget)
        self.greenValue.setGeometry(QtCore.QRect(190, 60, 61, 41))
        self.greenValue.setObjectName("greenValue")

        self.blueValue = QtWidgets.QLineEdit(self.centralwidget)
        self.blueValue.setGeometry(QtCore.QRect(320, 60, 61, 41))
        self.blueValue.setObjectName("blueValue")

        self.redText = QtWidgets.QLabel(self.centralwidget)
        self.redText.setGeometry(QtCore.QRect(60, 100, 61, 21))
        self.redText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.redText.setAlignment(QtCore.Qt.AlignCenter)
        self.redText.setObjectName("redText")

        self.greenText = QtWidgets.QLabel(self.centralwidget)
        self.greenText.setGeometry(QtCore.QRect(190, 100, 61, 21))
        self.greenText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.greenText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenText.setObjectName("greenText")

        self.blueText = QtWidgets.QLabel(self.centralwidget)
        self.blueText.setGeometry(QtCore.QRect(320, 100, 61, 21))
        self.blueText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueText.setObjectName("blueText")

        self.displayColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.displayColorBtn.setGeometry(QtCore.QRect(430, 70, 75, 23))
        self.displayColorBtn.setObjectName("displayColorBtn")

        self.colorSelectorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.colorSelectorBtn.setGeometry(QtCore.QRect(430, 150, 75, 23))
        self.colorSelectorBtn.setObjectName("colorSelectorBtn")

        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        # Global Variables
        self.redValueInput = 255
        self.greenValueInput = 0
        self.blueValueInput = 0
                
        # Functions with Buttons
        self.displayColorBtn.clicked.connect(self.displayColor)
        self.colorSelectorBtn.clicked.connect(self.selectionPopup)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.redText.setText(_translate("MainWindow", "Red"))
        self.greenText.setText(_translate("MainWindow", "Green"))
        self.blueText.setText(_translate("MainWindow", "Blue"))
        self.displayColorBtn.setText(_translate("MainWindow", "Display Color"))
        self.colorSelectorBtn.setText(_translate("MainWindow", "Color Selector"))

    def selectionPopup(self):
        QtWidgets.QColorDialog.getColor()

    def displayColor(self):
        # TODO: Slider for choosing color is better rather than inputting number values since users do not know the range
        self.redValueInput = int(self.redValue.text())
        self.greenValueInput = int(self.greenValue.text())
        self.blueValueInput = int(self.blueValue.text())
        hexColor = '#'+'%02x%02x%02x' % (self.redValueInput, self.greenValueInput, self.blueValueInput)
        self.colorDisplay.setStyleSheet(f'background-color: {hexColor}')
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())