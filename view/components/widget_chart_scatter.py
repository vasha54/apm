from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5.QtGui import (
     QPainter
)

from PyQt5 import QtWidgets, QtGui
from view.preferences.preferences import PreferenceGUI
from view.components.charts.chart_scatter import ChartScatter

class WidgetChartScatter(QWidget):
    
    def __init__(self,_correlation,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setMinimumHeight(250)
        layout = QtWidgets.QVBoxLayout(self)
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        dataChart ={'valuesX':_correlation['data-x'],
                    'valuesY':_correlation['data-y'],
                    'title_Y':_correlation['label-y'],
                    'title_X':_correlation['label-x'],
                    'sizePoints':5}
        
        self.chartScatter= ChartScatter(self)
        self.chartScatter.makeChart(dataChart)
        self.chartScatter.setColorAxes(colorAxes)
        self.chartScatter.setColorBackground(colorBackground)
        self.chartScatter.setColorText(colorText)
        
        layout.addWidget(self.chartScatter)
        self.setLayout(layout)