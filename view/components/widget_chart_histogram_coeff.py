from PyQt5.QtWidgets import (
    QWidget, QLabel
)

from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5.QtGui import (
     QPainter
)

from PyQt5.QtCore import (
    Qt
) 

from PyQt5 import QtWidgets, QtGui
from view.preferences.preferences import PreferenceGUI

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class WidgetChartHistogramCoeff(QWidget):
    
    def __init__(self,_data,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setMinimumHeight(250)
        layout = QtWidgets.QVBoxLayout(self)
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        
        self.labelTitle = QLabel(_data['name'])
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("background-color: "+str(colorBackground)+";")
        self.labelTitle.setScaledContents(True)
        self.labelTitle.setAlignment(Qt.AlignCenter)
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        
        self.graphWidget.setWindowTitle(_data['name'])
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidget.setLabel('left', 'DfBeta', **styles)
        self.graphWidget.setLabel('bottom','Observación', **styles)
        self.graphWidget.setBackground(colorBackground)
        
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        
        x = list()
        y1 = _data['coef']
        
        for i in range(0,len(y1)):
            x.append(i)
        
        bargraph = pg.BarGraphItem(x = x, height = y1, width = 1.0, brush ='g',pen=None)
        
        self.graphWidget.addItem(bargraph)
        
        layout.addWidget(self.labelTitle)
        layout.addWidget(self.graphWidget)
        layout.setSpacing(0)
        self.setLayout(layout)