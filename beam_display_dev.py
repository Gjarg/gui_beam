# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beam_display.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import os
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1087, 542)
        self.DisplayGraph = QtWidgets.QGraphicsView(Form)
        self.DisplayGraph.setGeometry(QtCore.QRect(44, 185, 371, 301))
        self.DisplayGraph.setObjectName("DisplayGraph")
        self.PathImage = QtWidgets.QTextEdit(Form)
        self.PathImage.setGeometry(QtCore.QRect(43, 43, 291, 31))
        self.PathImage.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.PathImage.setObjectName("PathImage")
        self.PathImage.setPlaceholderText('Drag and drop your image')
        self.ShowBeamButton = QtWidgets.QPushButton(Form, clicked= lambda:self.press_it())
        self.ShowBeamButton.setGeometry(QtCore.QRect(41, 115, 161, 28))
        self.ShowBeamButton.setObjectName("ShowBeamButton")
        self.DisplayPath = QtWidgets.QLabel(Form)
        self.DisplayPath.setGeometry(QtCore.QRect(230, 120, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DisplayPath.setFont(font)
        self.DisplayPath.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.DisplayPath.setObjectName("DisplayPath")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def press_it(self):
        val = self.PathImage.toPlainText()
        #self.DisplayPath.setText(val)
        #val[8:] if any(val.startswith(x) for x in ('file:///')) else val
        if 'file:///' in val:
            val = val[len('file:///'):]
            print(val)
        beam = np.asarray(Image.open(val))
        plt.imshow(beam)
        plt.show()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.PathImage.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.ShowBeamButton.setText(_translate("Form", "show me the beam"))
        self.DisplayPath.setText(_translate("Form", "hello world"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
