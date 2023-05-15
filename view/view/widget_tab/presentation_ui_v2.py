# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'presentation_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import(
    QPainter, QBrush, QPixmap
)

from PyQt5.QtCore import (
    QRectF, QPoint
)

import view.resource.resource

class Ui_WidgetPresentacion(QtWidgets.QWidget):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
    
    def setupUi(self, WidgetPresentacion):
        self.retranslateUi(WidgetPresentacion)
        QtCore.QMetaObject.connectSlotsByName(WidgetPresentacion)

    def retranslateUi(self, WidgetPresentacion):
        _translate = QtCore.QCoreApplication.translate
        WidgetPresentacion.setWindowTitle(_translate("WidgetPresentacion", "Form"))
        
    def paintEvent(self, ev):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform,1)
        center = QPoint(self.width()/2,self.height()/2)
        painter.translate(center)
        painter.scale(1*self.width()/2579.0,1*self.height()/1576.0)
        painter.translate(0-2579/2,0-1576/2)
        painter.drawPixmap(0,0,2579,1576,QPixmap(":/img/portada_1.png"))
        
       

