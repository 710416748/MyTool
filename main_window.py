# -*- coding: utf-8 -*-
# @Time        : 2020/7/4
# @Author      : YeChen.Xu
# @Email       : 710416748@qq.com
# @File        : main_window.py
# @Description :


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QApplication, QMessageBox, \
                     QHBoxLayout, QVBoxLayout, QTextEdit
from PyQt5.QtGui import QFont


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        #HEAD part
        self.btnIndex1 = QPushButton('ADB_CMD', self)
        self.btnIndex1.setToolTip('This is a adb <b>QPushButton</b> widget')
        self.btnIndex1.resize(self.btnIndex1.sizeHint())
        #self.btnIndex1.move(0, 0)

        self.btnIndex2 = QPushButton('COM_CMD', self)
        self.btnIndex2.setToolTip('This is a complie <b>QPushButton</b> widget')
        self.btnIndex2.resize(self.btnIndex2.sizeHint())

        self.layoutHead = QHBoxLayout()
        self.layoutHead.addWidget(self.btnIndex1)
        self.layoutHead.addWidget(self.btnIndex2)

        self.widgetHead = QWidget()
        self.widgetHead.setLayout(self.layoutHead)

        #BODY part
        #BODY LEFT
        self.btnCDM1 = QPushButton('CMD1', self)
        self.btnCDM1.resize(self.btnCDM1.sizeHint())

        self.btnCDM2 = QPushButton('CMD2', self)
        self.btnCDM2.resize(self.btnCDM2.sizeHint())

        self.widgetBodyLeftLayout = QVBoxLayout()
        self.widgetBodyLeftLayout.addWidget(self.btnCDM1)
        self.widgetBodyLeftLayout.addWidget(self.btnCDM2)

        self.widgetBodyLeft = QWidget()
        self.widgetBodyLeft.setLayout(self.widgetBodyLeftLayout)

        #BODY MID
        self.textBodyMid = QTextEdit()
        self.textBodyMid.setPlainText("This text1")

        self.widgetBodyMidLayout = QVBoxLayout()
        self.widgetBodyMidLayout.addWidget(self.textBodyMid)

        self.widgetBodyMid = QWidget()
        self.widgetBodyMid.setLayout(self.widgetBodyMidLayout)

        #BODY RIGHT
        self.textBodyRight = QTextEdit()
        self.textBodyRight.setPlainText("This text2")

        self.widgetBodyRightLayout = QVBoxLayout()
        self.widgetBodyRightLayout.addWidget(self.textBodyRight)

        self.widgetBodyRight = QWidget()
        self.widgetBodyRight.setLayout( self.widgetBodyRightLayout)

        #BODY ROOT
        self.layoutBody = QHBoxLayout()
        self.layoutBody.addWidget(self.widgetBodyLeft)
        self.layoutBody.addWidget(self.widgetBodyMid)
        self.layoutBody.addWidget(self.widgetBodyRight)

        self.widgetBody = QWidget()
        self.widgetBody.setLayout(self.layoutBody)

        #root
        self.layoutRoot = QVBoxLayout()
        self.layoutRoot.addWidget(self.widgetHead)
        self.layoutRoot.addWidget(self.widgetBody)
        self.setLayout(self.layoutRoot)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('MyTool')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = MainWidget()

    sys.exit(app.exec_())
