from PyQt5.QtWidgets import (
    QWidget, QDialog, QVBoxLayout
)

from PyQt5 import QtCore, QtGui, QtWidgets
from view.components.widget_chart_scatter import WidgetChartScatter

class DialogDetailsCorrelation(QDialog):
    
    def __init__(self, _correlation,*args, **kwargs):
    
        super(DialogDetailsCorrelation, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()
        widget = WidgetChartScatter(_correlation)
        layout.addWidget(widget)
        self.setWindowTitle("Correlación "+_correlation['label-y']+'-'+_correlation['label-x'])
        self.setLayout(layout)

        