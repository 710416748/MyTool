# -*- coding: utf-8 -*-
# @Time        : 2020/7/4
# @Author      : YeChen.Xu
# @Email       : 710416748@qq.com
# @File        : main_window.py
# @Description :


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox
from PyQt5.QtGui import QFont


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('CMD1', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(0, 0)

        self.setGeometry(300, 300, 300, 200)
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
