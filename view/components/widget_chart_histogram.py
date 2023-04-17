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
from view.components.charts.chart_histogram import ChartHistogram

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
        self.labelTitle.setScaledContents(True)
        self.labelTitle.setAlignment(Qt.AlignCenter)
        
        self.labelMean = QLabel("Media: "+str(format(mean,formatStr)))
        self.labelMean.setScaledContents(True)
        self.labelMean.setAlignment(Qt.AlignRight)
        
        self.labelCV = QLabel("CV: "+str(format(cv,formatStr)))
        self.labelCV.setScaledContents(True)
        self.labelCV.setAlignment(Qt.AlignRight)
        
        self.labelMedian = QLabel("Mediana: "+str(format(median,formatStr)))
        self.labelMedian.setScaledContents(True)
        self.labelMedian.setAlignment(Qt.AlignRight)
        
        heights = []
        bars = []
        xticklabels = []
        
        data = _data['bars']
        
        for k,v in data.items():
            heights.append(v['frequency'])
            bars.append(k)
        
        dataChart ={'heights':heights,
               'bars':bars,
               'title_Y':'Frecuencia',
               'title_X':'Coeficientes',
               'xticks':bars}
        
        self.chartHistogram = ChartHistogram(self)
        self.chartHistogram.makeChart(dataChart)
        self.chartHistogram.setColorText(colorText)
        self.chartHistogram.setColorAxes(colorAxes)
        self.chartHistogram.setColorBackground(colorBackground)
        
        layout.addWidget(self.labelTitle)
        layout.addWidget(self.labelMean)
        layout.addWidget(self.labelCV)
        layout.addWidget(self.labelMedian)
        layout.addWidget(self.chartHistogram)
        layout.setSpacing(0)
        self.setLayout(layout)