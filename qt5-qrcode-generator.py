#!/bin/python2
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PIL.ImageQt import ImageQt
import qrcode
import sys

class App():

    def show_qr(self,data):
        self.app = QApplication(sys.argv)
        self.widget = QWidget()
        self.widget.setWindowTitle("Window")
        self.widget.setGeometry(10,10,500,500)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image() # PIL format

        qim = ImageQt(img)
        pixmap = QtGui.QPixmap.fromImage(qim)
        label = QLabel(self.widget)
        label.setPixmap(pixmap)
        self.widget.resize(pixmap.width(),pixmap.height())
        self.widget.show()
        self.app.exec_()



ex = App()
ex.show_qr(sys.argv[1])

