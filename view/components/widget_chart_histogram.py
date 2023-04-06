from PyQt5.QtWidgets import (
    QWidget, QLabel
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

class WidgetChartHistogram(QWidget):
    
    def __init__(self,_data,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setMinimumHeight(250)
        layout = QtWidgets.QVBoxLayout(self)
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        mean = _data['mean']
        std = _data['std']
        median = _data['median']
        cv = _data['cv']
        
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
        
        self.labelMean = QLabel("Media: "+str(format(mean,formatStr)))
        self.labelMean.setStyleSheet("background-color: "+str(colorBackground)+";")
        self.labelMean.setScaledContents(True)
        self.labelMean.setAlignment(Qt.AlignRight)
        
        self.labelCV = QLabel("CV: "+str(format(cv,formatStr)))
        self.labelCV.setStyleSheet("background-color: "+str(colorBackground)+";")
        self.labelCV.setScaledContents(True)
        self.labelCV.setAlignment(Qt.AlignRight)
        
        self.labelMedian = QLabel("Mediana: "+str(format(median,formatStr)))
        self.labelMedian.setStyleSheet("background-color: "+str(colorBackground)+";")
        self.labelMedian.setScaledContents(True)
        self.labelMedian.setAlignment(Qt.AlignRight)
        
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        
        self.graphWidget.setWindowTitle(_data['name'])
        
        styles = {'color':colorText, 'font-size':'10px'}
        self.graphWidget.setLabel('left', 'Frecuencia', **styles)
        self.graphWidget.setLabel('bottom','Coeficientes', **styles)
        self.graphWidget.setBackground(colorBackground)
        
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        
        y1 = [ ]
        x = [ ]
        
        bars = _data['bars']
        
        
        for k,v in bars.items():
            y1.append(v['frequency'])
            x.append(k)
        
        bargraph = pg.BarGraphItem(x = x, height = y1, width = 1.0, brush ='g',pen=None)
        
        
        self.graphWidget.addItem(bargraph)
        
        
        layout.addWidget(self.labelTitle)
        layout.addWidget(self.labelMean)
        layout.addWidget(self.labelCV)
        layout.addWidget(self.labelMedian)
        layout.addWidget(self.graphWidget)
        layout.setSpacing(0)
        self.setLayout(layout)