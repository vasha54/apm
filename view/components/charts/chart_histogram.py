import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pandas as pd
from math import pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from view.preferences.preferences import PreferenceGUI
class ChartHistogram(FigureCanvas):
        
    def __init__(self,parent):
        self.fig,self.ax = plt.subplots(1,1,constrained_layout=True)
        super().__init__(self.fig)
        self.setParent(parent)
        
    def makeHistogramChart(self,_data):
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        
        
        x = list()
        y1 = _data['coef']
        
        for i in range(0,len(y1)):
            x.append(i)
        
        plt.bar(x, height=y1)
       
        
        self.ax.set_title(_data['name'],fontsize=10,color=colorText)
        xlabel = ''
        ylabel = ''
        if 'title_X' in _data.keys():
            xlabel=_data['title_X']
            self.ax.set_xlabel(xlabel,fontsize=8,color=colorText)
        if 'title_Y' in _data.keys():
            ylabel=_data['title_Y']
            self.ax.set_ylabel(ylabel,fontsize=8,color=colorText)
        self.fig.patch.set_facecolor('#000000FF')
        self.fig.patch.set_alpha(0)
        self.ax.set_facecolor(colorBackground)
        self.ax.tick_params(axis='x', colors=colorAxes)    
        self.ax.tick_params(axis='y', colors=colorAxes)
        self.ax.spines['left'].set_color(colorAxes)        
        self.ax.spines['bottom'].set_color(colorAxes)
        self.ax.spines['top'].set_alpha(0)        
        self.ax.spines['right'].set_alpha(0)
        
        
        
        

        
        