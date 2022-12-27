from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5.QtGui import (
     QPainter
)

from PyQt5 import QtWidgets, QtGui
from view.preferences.preferences import PreferenceGUI

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg


class WidgetChartItem(QWidget):
    
   
    
    def __init__(self,_correlation,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setMinimumHeight(250)
        layout = QtWidgets.QVBoxLayout(self)
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        
        
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidget.setLabel('left', _correlation['label-y'], **styles)
        self.graphWidget.setLabel('bottom', _correlation['label-x'], **styles)
        self.graphWidget.setBackground(colorBackground)
        
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        
        self.graphWidget.plot(_correlation['data-x'], _correlation['data-y'],pen=None,symbol='o', symbolSize=5, symbolBrush=brush)
        
        layout.addWidget(self.graphWidget)
        self.setLayout(layout)