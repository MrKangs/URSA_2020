# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\URSA_2020\Playing around with PyQt5\Day 13\Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import numpy as np
import cv2
from sklearn.cluster import KMeans

filePath = []
index = 0
redAverage = 128
redRange = 0
greenAverage = 128
greenRange = 0
blueAverage = 128
blueRange = 0
redValue = 0
greenValue = 0
blueValue = 0
xValue = 0
yValue = 0
num = 1
RGB = []
Prop = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ogImgLbl = QtWidgets.QLabel(self.centralwidget)
        self.ogImgLbl.setGeometry(QtCore.QRect(20, 20, 400, 400))
        self.ogImgLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.ogImgLbl.setText("")
        self.ogImgLbl.setCursor(QtCore.Qt.CrossCursor)
        self.ogImgLbl.setObjectName("ogImgLbl")
        self.executeImgLbl = QtWidgets.QLabel(self.centralwidget)
        self.executeImgLbl.setGeometry(QtCore.QRect(20, 460, 400, 400))
        self.executeImgLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.executeImgLbl.setText("")
        self.executeImgLbl.setObjectName("executeImgLbl")
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextBtn.setGeometry(QtCore.QRect(260, 430, 75, 20))
        self.nextBtn.setObjectName("nextBtn")
        self.previousBtn = QtWidgets.QPushButton(self.centralwidget)
        self.previousBtn.setGeometry(QtCore.QRect(90, 430, 75, 20))
        self.previousBtn.setObjectName("previousBtn")
        self.greenAverageText = QtWidgets.QLabel(self.centralwidget)
        self.greenAverageText.setGeometry(QtCore.QRect(620, 290, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.greenAverageText.setFont(font)
        self.greenAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.greenAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenAverageText.setObjectName("greenAverageText")
        self.redRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.redRangeValue.setGeometry(QtCore.QRect(860, 190, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redRangeValue.setFont(font)
        self.redRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redRangeValue.setText("")
        self.redRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redRangeValue.setObjectName("redRangeValue")
        self.greenRangeText = QtWidgets.QLabel(self.centralwidget)
        self.greenRangeText.setGeometry(QtCore.QRect(630, 370, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.greenRangeText.setFont(font)
        self.greenRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.greenRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenRangeText.setObjectName("greenRangeText")
        self.greenAverageSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenAverageSlider.setGeometry(QtCore.QRect(490, 320, 351, 22))
        self.greenAverageSlider.setMaximum(255)
        self.greenAverageSlider.setProperty("value", 128)
        self.greenAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenAverageSlider.setObjectName("greenAverageSlider")
        self.greenRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenRangeSlider.setGeometry(QtCore.QRect(490, 402, 351, 20))
        self.greenRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.greenRangeSlider.setMaximum(127)
        self.greenRangeSlider.setProperty("value", 0)
        self.greenRangeSlider.setSliderPosition(0)
        self.greenRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenRangeSlider.setObjectName("greenRangeSlider")
        self.blueAverageText = QtWidgets.QLabel(self.centralwidget)
        self.blueAverageText.setGeometry(QtCore.QRect(630, 500, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.blueAverageText.setFont(font)
        self.blueAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueAverageText.setObjectName("blueAverageText")
        self.redRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.redRangeSlider.setGeometry(QtCore.QRect(490, 190, 351, 22))
        self.redRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.redRangeSlider.setMaximum(127)
        self.redRangeSlider.setProperty("value", 0)
        self.redRangeSlider.setSliderPosition(0)
        self.redRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redRangeSlider.setObjectName("redRangeSlider")
        self.blueRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueRangeSlider.setGeometry(QtCore.QRect(490, 620, 351, 22))
        self.blueRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blueRangeSlider.setMaximum(127)
        self.blueRangeSlider.setSliderPosition(0)
        self.blueRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueRangeSlider.setObjectName("blueRangeSlider")
        self.blueAverageSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueAverageSlider.setGeometry(QtCore.QRect(490, 540, 351, 22))
        self.blueAverageSlider.setMaximum(255)
        self.blueAverageSlider.setProperty("value", 128)
        self.blueAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueAverageSlider.setObjectName("blueAverageSlider")
        self.borderLineWithGB = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithGB.setGeometry(QtCore.QRect(440, 470, 511, 20))
        self.borderLineWithGB.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithGB.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithGB.setObjectName("borderLineWithGB")
        self.blueRangeText = QtWidgets.QLabel(self.centralwidget)
        self.blueRangeText.setGeometry(QtCore.QRect(630, 580, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.blueRangeText.setFont(font)
        self.blueRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueRangeText.setObjectName("blueRangeText")
        self.redRangeText = QtWidgets.QLabel(self.centralwidget)
        self.redRangeText.setGeometry(QtCore.QRect(630, 160, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.redRangeText.setFont(font)
        self.redRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.redRangeText.setObjectName("redRangeText")
        self.redAverageSlider = QtWidgets.QSlider(self.centralwidget)
        self.redAverageSlider.setGeometry(QtCore.QRect(490, 110, 351, 22))
        self.redAverageSlider.setMaximum(255)
        self.redAverageSlider.setSliderPosition(128)
        self.redAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redAverageSlider.setObjectName("redAverageSlider")
        self.blueAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.blueAverageValue.setGeometry(QtCore.QRect(860, 540, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueAverageValue.setFont(font)
        self.blueAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueAverageValue.setText("")
        self.blueAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueAverageValue.setObjectName("blueAverageValue")
        self.blueRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.blueRangeValue.setGeometry(QtCore.QRect(860, 620, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueRangeValue.setFont(font)
        self.blueRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueRangeValue.setText("")
        self.blueRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueRangeValue.setObjectName("blueRangeValue")
        self.redAverageText = QtWidgets.QLabel(self.centralwidget)
        self.redAverageText.setGeometry(QtCore.QRect(630, 80, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.redAverageText.setFont(font)
        self.redAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.redAverageText.setObjectName("redAverageText")
        self.redAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.redAverageValue.setGeometry(QtCore.QRect(860, 110, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redAverageValue.setFont(font)
        self.redAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redAverageValue.setText("")
        self.redAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redAverageValue.setObjectName("redAverageValue")
        self.colorRangeText = QtWidgets.QLabel(self.centralwidget)
        self.colorRangeText.setGeometry(QtCore.QRect(580, 40, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.colorRangeText.setFont(font)
        self.colorRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.colorRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.colorRangeText.setObjectName("colorRangeText")
        self.greenAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.greenAverageValue.setGeometry(QtCore.QRect(860, 320, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenAverageValue.setFont(font)
        self.greenAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenAverageValue.setText("")
        self.greenAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenAverageValue.setObjectName("greenAverageValue")
        self.borderLineWithRG = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithRG.setGeometry(QtCore.QRect(440, 260, 511, 20))
        self.borderLineWithRG.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithRG.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithRG.setObjectName("borderLineWithRG")
        self.greenRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.greenRangeValue.setGeometry(QtCore.QRect(860, 400, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenRangeValue.setFont(font)
        self.greenRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenRangeValue.setText("")
        self.greenRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenRangeValue.setObjectName("greenRangeValue")
        self.borderLineWithGB_2 = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithGB_2.setGeometry(QtCore.QRect(440, 680, 511, 20))
        self.borderLineWithGB_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithGB_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithGB_2.setObjectName("borderLineWithGB_2")
        self.yText = QtWidgets.QLabel(self.centralwidget)
        self.yText.setGeometry(QtCore.QRect(680, 700, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yText.setFont(font)
        self.yText.setAlignment(QtCore.Qt.AlignCenter)
        self.yText.setObjectName("yText")
        self.xText = QtWidgets.QLabel(self.centralwidget)
        self.xText.setGeometry(QtCore.QRect(570, 700, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xText.setFont(font)
        self.xText.setAlignment(QtCore.Qt.AlignCenter)
        self.xText.setObjectName("xText")
        self.xValueText = QtWidgets.QLabel(self.centralwidget)
        self.xValueText.setGeometry(QtCore.QRect(570, 740, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xValueText.setFont(font)
        self.xValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.xValueText.setText("")
        self.xValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.xValueText.setObjectName("xValueText")
        self.colorPreviewText = QtWidgets.QLabel(self.centralwidget)
        self.colorPreviewText.setGeometry(QtCore.QRect(790, 760, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.colorPreviewText.setFont(font)
        self.colorPreviewText.setAlignment(QtCore.Qt.AlignCenter)
        self.colorPreviewText.setObjectName("colorPreviewText")
        self.colorPreview = QtWidgets.QLabel(self.centralwidget)
        self.colorPreview.setGeometry(QtCore.QRect(790, 790, 130, 50))
        self.colorPreview.setFrameShape(QtWidgets.QFrame.Box)
        self.colorPreview.setText("")
        self.colorPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.colorPreview.setObjectName("colorPreview")
        self.yValueText = QtWidgets.QLabel(self.centralwidget)
        self.yValueText.setGeometry(QtCore.QRect(680, 740, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yValueText.setFont(font)
        self.yValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.yValueText.setText("")
        self.yValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.yValueText.setObjectName("yValueText")
        self.redValueText = QtWidgets.QLabel(self.centralwidget)
        self.redValueText.setGeometry(QtCore.QRect(460, 820, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redValueText.setFont(font)
        self.redValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.redValueText.setText("")
        self.redValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.redValueText.setObjectName("redValueText")
        self.greenValueText = QtWidgets.QLabel(self.centralwidget)
        self.greenValueText.setGeometry(QtCore.QRect(570, 820, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenValueText.setFont(font)
        self.greenValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.greenValueText.setText("")
        self.greenValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenValueText.setObjectName("greenValueText")
        self.blueValueText = QtWidgets.QLabel(self.centralwidget)
        self.blueValueText.setGeometry(QtCore.QRect(680, 820, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueValueText.setFont(font)
        self.blueValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.blueValueText.setText("")
        self.blueValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueValueText.setObjectName("blueValueText")
        self.redText = QtWidgets.QLabel(self.centralwidget)
        self.redText.setGeometry(QtCore.QRect(460, 800, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redText.setFont(font)
        self.redText.setAlignment(QtCore.Qt.AlignCenter)
        self.redText.setObjectName("redText")
        self.greenText = QtWidgets.QLabel(self.centralwidget)
        self.greenText.setGeometry(QtCore.QRect(570, 800, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenText.setFont(font)
        self.greenText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenText.setObjectName("greenText")
        self.blueText = QtWidgets.QLabel(self.centralwidget)
        self.blueText.setGeometry(QtCore.QRect(680, 800, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueText.setFont(font)
        self.blueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueText.setObjectName("blueText")
        self.commonColorLbl = QtWidgets.QLabel(self.centralwidget)
        self.commonColorLbl.setGeometry(QtCore.QRect(980, 50, 200, 800))
        self.commonColorLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.commonColorLbl.setCursor(QtCore.Qt.CrossCursor)
        self.commonColorLbl.setText("")
        self.commonColorLbl.setObjectName("commonColorLbl")
        self.commonColorSlider = QtWidgets.QSlider(self.centralwidget)
        self.commonColorSlider.setGeometry(QtCore.QRect(1220, 390, 50, 160))
        self.commonColorSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commonColorSlider.setMaximum(5)
        self.commonColorSlider.setMinimum(1)
        self.commonColorSlider.setSliderPosition(0)
        self.commonColorSlider.setOrientation(QtCore.Qt.Vertical)
        self.commonColorSlider.setInvertedAppearance(False)
        self.commonColorSlider.setInvertedControls(False)
        self.commonColorSlider.setObjectName("commonColorSlider")
        self.commonColorValue = QtWidgets.QLabel(self.centralwidget)
        self.commonColorValue.setGeometry(QtCore.QRect(1220, 350, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.commonColorValue.setFont(font)
        self.commonColorValue.setFrameShape(QtWidgets.QFrame.Box)
        self.commonColorValue.setText("")
        self.commonColorValue.setAlignment(QtCore.Qt.AlignCenter)
        self.commonColorValue.setObjectName("commonColorValue")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()

        self.readFile()
        
        # Timer 
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

        # Button
        self.nextBtn.clicked.connect(self.nextImage)
        self.previousBtn.clicked.connect(self.previousImage)

        # Mouse
        self.ogImgLbl.mousePressEvent = self.captureIt
        self.commonColorLbl.mousePressEvent = self.captureCommon

        # Slider
        self.redAverageSlider.valueChanged.connect(self.redAverageUpdate)
        self.redRangeSlider.valueChanged.connect(self.redRangeUpdate)
        self.greenAverageSlider.valueChanged.connect(self.greenAverageUpdate)
        self.greenRangeSlider.valueChanged.connect(self.greenRangeUpdate)
        self.blueAverageSlider.valueChanged.connect(self.blueAverageUpdate)
        self.blueRangeSlider.valueChanged.connect(self.blueRangeUpdate)
        self.commonColorSlider.valueChanged.connect(self.commonColorNumUpdate)

    def readFile(self):
        if not os.path.exists('images'):
            os.makedirs('images')
        global filePath, RGB, Prop
        scale_percent = 50
        j = 0
        path = os.path.abspath(os.getcwd())
        for i, filename in enumerate(os.listdir(path)):
            img = cv2.imread(os.path.join(path, filename))
            if img is not None:
                path += f"\images\{i}.png"
                dsize = (400,400)
                output = cv2.resize(img, dsize)
                cv2.imwrite(path, output)
                filePath.append(path)
                RGB.append([])
                Prop.append([])
                self.analyzeColor(path, j)
                j += 1
                path = os.path.abspath(os.getcwd())

        pixmap = QtGui.QPixmap(filePath[0])
        self.ogImgLbl.setPixmap(pixmap)
        self.ogImgLbl.setAlignment(QtCore.Qt.AlignLeft)

    def analyzeColor(self, filePath, ind):
        global RGB, Prop
        img = cv2.imread(filePath)
        height, width, _ = np.shape(img)
        image = img.reshape((height * width, 3))
        clusters = KMeans(n_clusters=5)
        clusters.fit(image)
        histogram = self.make_histogram(clusters)
        ordered = zip(histogram, clusters.cluster_centers_)
        ordered = sorted(ordered, key=lambda x: x[0], reverse = True)
        for index, row in enumerate(ordered):
            RGB[ind].append((int(row[1][2]), int(row[1][1]), int(row[1][0])))
            Prop[ind].append('%.2f'%(row[0] * 100))

    def make_bar(self, color):
        bar = np.zeros((160, 200, 3), np.uint8)
        bar[:] = [color[2], color[1], color[0]]
        return bar

    def make_histogram(self, clusters):
        numLabels = np.arange(0, len(np.unique(clusters.labels_)) + 1)
        hist, _ = np.histogram(clusters.labels_, bins = numLabels)
        hist = hist.astype('float32')
        hist /= hist.sum()
        return hist


    def nextImage(self):
        global index, filePath
        if (index  == len(filePath) - 1):
            self.error()
            return False
        index += 1
        pixmap = QtGui.QPixmap(filePath[index])
        self.ogImgLbl.setPixmap(pixmap)
        self.ogImgLbl.setAlignment(QtCore.Qt.AlignLeft)

    def previousImage(self):
        global index, filePath
        if (index  == 0):
            self.error()
            return False
        index -= 1
        pixmap = QtGui.QPixmap(filePath[index])
        self.ogImgLbl.setPixmap(pixmap)
        self.ogImgLbl.setAlignment(QtCore.Qt.AlignLeft) 

    def error(self):
        errorMessage2 = QtWidgets.QMessageBox()
        errorMessage2.setWindowTitle("Error")
        errorMessage2.setText("Out of Range")
        errorMessage2.setIcon(QtWidgets.QMessageBox.Critical)
        x = errorMessage2.exec_()

    def commonColorNumUpdate(self):
        global num
        num = self.commonColorSlider.sliderPosition()
    
    def redRangeUpdate(self):
        global redRange
        redRange = self.redRangeSlider.sliderPosition()

    def redAverageUpdate(self):
        global redAverage
        redAverage = self.redAverageSlider.sliderPosition()

    def greenRangeUpdate(self):
        global greenRange
        greenRange = self.greenRangeSlider.sliderPosition()

    def greenAverageUpdate(self):
        global greenAverage
        greenAverage = self.greenAverageSlider.sliderPosition()

    def blueRangeUpdate(self):
        global blueRange
        blueRange = self.blueRangeSlider.sliderPosition()

    def blueAverageUpdate(self):
        global blueAverage
        blueAverage = self.blueAverageSlider.sliderPosition()
    
    def update(self):
        global filePath, index, redAverage, redRange, greenAverage, greenRange, blueAverage, blueRange, redValue, greenValue, blueValue, xValue, yValue, num

        self.redAverageValue.setNum(redAverage)
        self.redRangeValue.setNum(redRange)
        self.greenAverageValue.setNum(greenAverage)
        self.greenRangeValue.setNum(greenRange)
        self.blueAverageValue.setNum(blueAverage)
        self.blueRangeValue.setNum(blueRange)
        self.redAverageSlider.setSliderPosition(redAverage)
        self.redRangeSlider.setSliderPosition(redRange)
        self.greenAverageSlider.setSliderPosition(greenAverage)
        self.greenRangeSlider.setSliderPosition(greenRange)
        self.blueAverageSlider.setSliderPosition(blueAverage)
        self.blueRangeSlider.setSliderPosition(blueRange)
        self.xValueText.setNum(xValue)
        self.yValueText.setNum(yValue)
        self.redValueText.setNum(redValue)
        self.greenValueText.setNum(greenValue)
        self.blueValueText.setNum(blueValue)
        hexColor = '#'+'%02x%02x%02x' % (redValue, greenValue, blueValue)
        self.colorPreview.setStyleSheet(f'background-color: {hexColor}')
        self.commonColorValue.setNum(num)

        self.colorDetect()
        self.showCommonColor()

        

    def colorDetect(self):
        global redAverage, redRange, greenAverage, greenRange, blueAverage, blueRange
        
        redMin = redAverage - redRange
        if (redMin < 0) or (redAverage == 128 and redRange == 127):
            redMin = 0
        redMax = redAverage + redRange
        if (redMax > 255):
            redMax = 255
        greenMin = greenAverage - greenRange
        if (greenMin < 0) or (greenAverage == 128 and greenRange == 127):
            greenMin = 0
        greenMax = greenAverage + greenRange
        if (greenMax > 255):
            greenMax = 255
        blueMin = blueAverage - blueRange
        if (blueMin < 0) or (blueAverage == 128 and blueRange == 127):
            blueMin = 0
        blueMax = blueAverage + blueRange
        if (blueMax > 255):
            blueMax = 255

        self.color_detect(redMin, redMax, greenMin, greenMax, blueMin, blueMax)

    def color_detect(self, redMin, redMax, greenMin, greenMax, blueMin, blueMax):
        global filePath, index
        img = cv2.imread(filePath[index])
        Lower = np.array([blueMin, greenMin, redMin], dtype = "uint8")
        Upper = np.array([blueMax, greenMax, redMax], dtype = "uint8")
        mask = cv2.inRange(img, Lower, Upper)
        output = cv2.bitwise_and(img, img, mask = mask)
        cv2.imwrite("Detection.png", output)
        fileName = "Detection.png"
        pixmap = QtGui.QPixmap(fileName)
        self.executeImgLbl.setPixmap(pixmap)
        self.executeImgLbl.setAlignment(QtCore.Qt.AlignLeft)
        os.remove("Detection.png")

    def captureIt(self, event):
        global xValue, yValue, redValue, greenValue, blueValue, filePath, index
        xValue = event.pos().x()
        yValue = event.pos().y()
        qImg = QtGui.QImage(filePath[index])
        c = qImg.pixel(xValue, yValue)
        colors = QtGui.QColor(c).getRgb()
        redValue = colors[0]
        greenValue = colors[1]
        blueValue = colors[2]

    def captureCommon(self, event):
        global redAverage, blueAverage, greenAverage
        xValue = event.pos().x()
        yValue = event.pos().y()
        qImg = QtGui.QImage("common\Common_Colors.png")
        c = qImg.pixel(xValue, yValue)
        colors = QtGui.QColor(c).getRgb()
        redAverage = colors[0]
        greenAverage = colors[1]
        blueAverage = colors[2]

    def showCommonColor(self):
        global RGB, index, num, Prop
        bars = []
        for i in range(num):
            bar = self.make_bar(RGB[index][i])
            bars.append(bar)
        img = np.vstack(bars)
        for j in range(num):
            if (RGB[index][j][0] <= 100) and (RGB[index][j][1] <= 100)  and (RGB[index][j][2] <= 100):
                textColor = (255, 255, 255)
            else:
                textColor = (0,0,0) 
            img = cv2.putText(img, str(RGB[index][j]), (5, 20 + (j * 160)), cv2.FONT_HERSHEY_TRIPLEX, 0.5, textColor, 1, cv2.LINE_AA)
            img = cv2.putText(img, str(Prop[index][j]) + "%", (5, 40 + (j * 160)), cv2.FONT_HERSHEY_TRIPLEX, 0.5, textColor, 1, cv2.LINE_AA)
        if not os.path.exists('common'):
            os.makedirs('common')
        cv2.imwrite("common\Common_Colors.png", img)
        fileName = "common\Common_Colors.png"
        pixmap = QtGui.QPixmap(fileName)
        self.commonColorLbl.setPixmap(pixmap)
        self.commonColorLbl.setAlignment(QtCore.Qt.AlignLeft)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextBtn.setText(_translate("MainWindow", "Next"))
        self.previousBtn.setText(_translate("MainWindow", "Previous"))
        self.greenAverageText.setText(_translate("MainWindow", "Green Average"))
        self.greenRangeText.setText(_translate("MainWindow", "Green Range"))
        self.blueAverageText.setText(_translate("MainWindow", "Blue Average"))
        self.blueRangeText.setText(_translate("MainWindow", "Blue Range"))
        self.redRangeText.setText(_translate("MainWindow", "Red Range"))
        self.redAverageText.setText(_translate("MainWindow", "Red Average"))
        self.colorRangeText.setText(_translate("MainWindow", "Color Range Detection"))
        self.yText.setText(_translate("MainWindow", "Y"))
        self.xText.setText(_translate("MainWindow", "X"))
        self.colorPreviewText.setText(_translate("MainWindow", "Color Preview"))
        self.redText.setText(_translate("MainWindow", "Red"))
        self.greenText.setText(_translate("MainWindow", "Green"))
        self.blueText.setText(_translate("MainWindow", "Blue"))
        self.commonColorLbl.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())