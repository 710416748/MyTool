# -*- coding: utf-8 -*-
# @Time        : 2020/7/4
# @Author      : YeChen.Xu
# @Email       : 710416748@qq.com
# @File        : main_window.py
# @Description :


import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QApplication, \
                            QMessageBox, QHBoxLayout, QVBoxLayout, QTextEdit, QFrame, \
                            QListWidget, QStackedLayout
from PyQt5.QtGui import QFont
import string
from enum import Enum

class MainWidget(QFrame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.initDone = False
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        '''
        self.widgetList = QListWidget()
        self.widgetList.insertItem(0, 'device cmd')
        self.widgetList.insertItem(1, 'compile cmd')

        self.layoutHead = QHBoxLayout()
        self.layoutHead.addWidget(self.widgetList)

        self.widgetHead = QFrame()
        self.widgetHead.setLayout(self.layoutHead)
        '''
        #HEAD part
        self.btnIndex1 = QPushButton('&ADB CMD', self)
        self.btnIndex1.setToolTip('Show adb command')
        self.btnIndex1.setChecked(True)
        #self.btnIndex1.toggle()
        self.btnIndex1.clicked.connect(lambda: self.onBtnClicked(self.btnIndex1))

        #self.btnIndex1.resize(self.btnIndex1.sizeHint())
        #self.btnIndex1.move(0, 0)

        self.btnIndex2 = QPushButton('&COM CMD', self)
        self.btnIndex2.setToolTip('Show  complie command')
        self.btnIndex1.setChecked(True)
        #self.btnIndex2.resize(self.btnIndex2.sizeHint())
        self.btnIndex2.clicked.connect(lambda: self.onBtnClicked(self.btnIndex2))

        self.layoutHead = QHBoxLayout()

        self.layoutHead.addStretch(1)
        self.layoutHead.addWidget(self.btnIndex1)
        self.layoutHead.addStretch(1)
        self.layoutHead.addWidget(self.btnIndex2)
        self.layoutHead.addStretch(30)


        self.widgetHead = QFrame()
        self.widgetHead.setLayout(self.layoutHead)


        #BODY part
        #BODY LEFT
        '''
        self.btnCDM1 = QPushButton('CMD1_INDEX1', self)
        self.btnCDM1.resize(self.btnCDM1.sizeHint())
        self.btnCDM1.clicked.connect(lambda: self.onBtnClicked(self.btnCDM1))


        self.btnCDM2 = QPushButton('CMD2_INDEX1', self)
        self.btnCDM2.resize(self.btnCDM2.sizeHint())
        self.btnCDM2.clicked.connect(lambda: self.onBtnClicked(self.btnCDM2))
        '''
        self.widgetListBodyLeftIndex1 = QListWidget()
        self.widgetListBodyLeftIndex1.insertItem(0, 'index1 cmd1')
        self.widgetListBodyLeftIndex1.insertItem(1, 'index1 cmd2')
        self.widgetListBodyLeftIndex1.setFixedWidth(120)
        self.widgetListBodyLeftIndex1.itemDoubleClicked.connect(
            lambda: self.excuteCMD(1, self.widgetListBodyLeftIndex1.currentRow()))

        self.widgetListBodyLeftIndex2 = QListWidget()
        self.widgetListBodyLeftIndex2.insertItem(0, 'index2 cmd1')
        self.widgetListBodyLeftIndex2.insertItem(1, 'index2 cmd2')
        self.widgetListBodyLeftIndex2.setFixedWidth(120)
        self.widgetListBodyLeftIndex2.itemDoubleClicked.connect(
            lambda: self.excuteCMD(2, self.widgetListBodyLeftIndex2.currentRow()))

        self.widgetBodyLeftLayout = QStackedLayout()
        self.widgetBodyLeftLayout.addWidget(self.widgetListBodyLeftIndex1)
        self.widgetBodyLeftLayout.addWidget(self.widgetListBodyLeftIndex2)


        self.widgetBodyLeft = QFrame()
        self.widgetBodyLeft.setLayout(self.widgetBodyLeftLayout)

        #BODY MID
        self.textBodyMid = QTextEdit()
        self.textBodyMid.setPlainText("This text1")

        self.widgetBodyMidLayout = QVBoxLayout()
        self.widgetBodyMidLayout.addWidget(self.textBodyMid)

        self.widgetBodyMid = QFrame()
        self.widgetBodyMid.setLayout(self.widgetBodyMidLayout)

        #BODY RIGHT
        self.textBodyRight = QTextEdit()
        self.textBodyRight.setPlainText("This text2")

        self.widgetBodyRightLayout = QVBoxLayout()
        self.widgetBodyRightLayout.addWidget(self.textBodyRight)

        self.widgetBodyRight = QFrame()
        self.widgetBodyRight.setLayout(self.widgetBodyRightLayout)

        #BODY ROOT
        self.layoutBody = QHBoxLayout()
        self.layoutBody.addWidget(self.widgetBodyLeft)
        self.layoutBody.addWidget(self.widgetBodyMid)
        self.layoutBody.addWidget(self.widgetBodyRight)

        self.widgetBody = QFrame()
        self.widgetBody.setLayout(self.layoutBody)

        #root
        self.layoutRoot = QVBoxLayout()
        self.layoutRoot.addWidget(self.widgetHead)
        self.layoutRoot.addWidget(self.widgetBody)
        self.setLayout(self.layoutRoot)

        self.setGeometry(1200, 300, 800, 600)
        self.setWindowTitle('MyTool')
        self.initDone = True
        self.show()

    def onBtnClicked(self, btn):
        type = self.getBtnType(btn)

        typeFuntion = {
            self.btnType.INDEX: lambda btn:self.changeCMDList(btn),
            self.btnType.CMD: lambda btn: self.excuteCMD(btn),
        }

        print(type.name)
        typeFuntion[type](btn)


    def getBtnType(self, btn):
        if btn == self.btnIndex1 or btn == self.btnIndex2:
            return self.btnType.INDEX
        elif btn == self.btnCDM1 or btn == self.btnCDM2:
            return self.btnType.CMD
        else:
            return self.btnType.UNKNOWN


    def changeCMDList(self, btn):
        self.textBodyMid.setPlainText("enter " + btn.text())
        if btn == self.btnIndex1:
            self.widgetBodyLeftLayout.setCurrentIndex(0)
        elif btn == self.btnIndex2:
            self.widgetBodyLeftLayout.setCurrentIndex(1)
        else:
            self.widgetBodyLeftLayout.setCurrentIndex(0)

    def excuteCMD(self, i = 0, j = 0):
        self.textBodyMid.setPlainText("i = " + i.__str__() + "; j = " + j.__str__())

        if j == 0:
            obj = subprocess.Popen('adb devices', stdout=subprocess.PIPE)
            out = obj.stdout.read()
            obj.stdout.close()
            self.textBodyMid.setPlainText(out.__str__())
        elif j == 1:
            obj = subprocess.Popen('dir', stdout=subprocess.PIPE)
            out = obj.stdout.read()
            obj.stdout.close()
            self.textBodyMid.setPlainText(out.__str__())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    class btnType(Enum):
        UNKNOWN = -1
        INDEX = 0
        CMD = 1


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = MainWidget()

    sys.exit(app.exec_())
