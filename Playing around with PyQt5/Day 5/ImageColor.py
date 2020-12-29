# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\URSA_2020\Playing around with PyQt5\Day 5\ImageColor.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import imageio



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(20, 20, 531, 481))
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")
        self.imageLbl.setCursor(QtCore.Qt.CrossCursor)

        self.imageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.imageBtn.setGeometry(QtCore.QRect(620, 470, 75, 23))
        self.imageBtn.setObjectName("imageBtn")

        self.xText = QtWidgets.QLabel(self.centralwidget)
        self.xText.setGeometry(QtCore.QRect(580, 50, 47, 13))
        self.xText.setAlignment(QtCore.Qt.AlignCenter)
        self.xText.setObjectName("xText")

        self.yText = QtWidgets.QLabel(self.centralwidget)
        self.yText.setGeometry(QtCore.QRect(690, 50, 47, 13))
        self.yText.setAlignment(QtCore.Qt.AlignCenter)
        self.yText.setObjectName("yText")

        self.xValueText = QtWidgets.QLabel(self.centralwidget)
        self.xValueText.setGeometry(QtCore.QRect(580, 80, 51, 31))
        self.xValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.xValueText.setObjectName("xValueText")

        self.yValueText = QtWidgets.QLabel(self.centralwidget)
        self.yValueText.setGeometry(QtCore.QRect(690, 80, 51, 31))
        self.yValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.yValueText.setObjectName("yValueText")

        self.redText = QtWidgets.QLabel(self.centralwidget)
        self.redText.setGeometry(QtCore.QRect(570, 160, 47, 13))
        self.redText.setObjectName("redText")

        self.redValueText = QtWidgets.QLabel(self.centralwidget)
        self.redValueText.setGeometry(QtCore.QRect(610, 150, 61, 31))
        self.redValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.redValueText.setObjectName("redValueText")

        self.greenText = QtWidgets.QLabel(self.centralwidget)
        self.greenText.setGeometry(QtCore.QRect(570, 240, 47, 13))
        self.greenText.setObjectName("greenText")

        self.blueText = QtWidgets.QLabel(self.centralwidget)
        self.blueText.setGeometry(QtCore.QRect(570, 310, 47, 13))
        self.blueText.setObjectName("blueText")

        self.previewColor = QtWidgets.QLabel(self.centralwidget)
        self.previewColor.setGeometry(QtCore.QRect(570, 360, 171, 91))
        self.previewColor.setFrameShape(QtWidgets.QFrame.Box)
        self.previewColor.setObjectName("previewColor")

        self.greenValueText = QtWidgets.QLabel(self.centralwidget)
        self.greenValueText.setGeometry(QtCore.QRect(610, 230, 61, 31))
        self.greenValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.greenValueText.setObjectName("greenValueText")

        self.blueValueText = QtWidgets.QLabel(self.centralwidget)
        self.blueValueText.setGeometry(QtCore.QRect(610, 300, 61, 31))
        self.blueValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.blueValueText.setObjectName("blueValueText")

        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        # Global Variables
        self.filePath = "No_Path"
        self.xValue = 0
        self.yValue = 0
        self.redValue = 0
        self.greenValue = 0
        self.blueValue = 0



        # Functions with Button
        self.imageBtn.clicked.connect(self.setImage)

        # Functions with Mouse Event
        self.imageLbl.mousePressEvent = self.getPositionAndColor

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.imageBtn.setText(_translate("MainWindow", "Select Image"))
        self.xText.setText(_translate("MainWindow", "X"))
        self.yText.setText(_translate("MainWindow", "Y"))
        self.redText.setText(_translate("MainWindow", "Red"))
        self.greenText.setText(_translate("MainWindow", "Green"))
        self.blueText.setText(_translate("MainWindow", "Blue"))

    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)") # Ask for file
        self.filePath = fileName
        if (fileName): # If the user gives a file
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            self.imageLbl.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageLbl.adjustSize()
            self.imageLbl.setAlignment(QtCore.Qt.AlignLeft)

    def getPositionAndColor(self, event):
        self.xValue = event.pos().x()
        self.yValue = event.pos().y()
        self.xValueText.setNum(self.xValue)
        self.yValueText.setNum(self.yValue)
        # Must need a filepath before you click something on the label
        # TODO: Need some help from Sogol for programming aspect
        qImg = QtGui.QImage(self.filePath)
        c = qImg.pixel(self.xValue, self.yValue)
        colors = QtGui.QColor(c).getRgb()
        self.redValue = colors[0]
        self.blueValue = colors[1]
        self.greenValue = colors[2]
        self.redValueText.setNum(self.redValue)
        self.greenValueText.setNum(self.greenValue)
        self.blueValueText.setNum(self.blueValue)
        hexColor = '#'+'%02x%02x%02x' % (self.redValue, self.greenValue, self.blueValue)
        self.previewColor.setStyleSheet(f'background-color: {hexColor}')
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
