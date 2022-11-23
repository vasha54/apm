from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5 import QtCore, QtWidgets, QtGui

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg


class WidgetChartItem(QWidget):
    
   
    
    def __init__(self,_correlation,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setMinimumHeight(250)
        layout = QtWidgets.QVBoxLayout(self)
        self.graphWidget = pg.PlotWidget()
        styles = {'color':'b', 'font-size':'10px'}
        self.graphWidget.setLabel('left', _correlation['label-y'], **styles)
        self.graphWidget.setLabel('bottom', _correlation['label-x'], **styles)
        self.graphWidget.setBackground('w')
        
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        
        self.graphWidget.plot(_correlation['data-x'], _correlation['data-y'],pen=None,symbol='o', symbolSize=5, symbolBrush=brush)
        
        layout.addWidget(self.graphWidget)
        self.setLayout(layout)