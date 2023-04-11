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
        self.data = {}
        self.setParent(parent)
        
    def makeHistogramChart(self,_data):
        self.data=_data
        
        x = list()
        y1 = _data['coef']
        
        for i in range(0,len(y1)):
            x.append(i)
        
        plt.bar(x, height=y1)
        self.ax.set_title(_data['name'],fontsize=10,color='#000000')
        xlabel = ''
        ylabel = ''
        if 'title_X' in _data.keys():
            xlabel=_data['title_X']
            self.ax.set_xlabel(xlabel,fontsize=8,color='#000000')
        if 'title_Y' in _data.keys():
            ylabel=_data['title_Y']
            self.ax.set_ylabel(ylabel,fontsize=8,color='#000000')
        
    
    def setColorText(self,_color):        
        self.ax.set_title(self.data['name'],fontsize=10,color=_color)
        xlabel = ''
        ylabel = ''
        if 'title_X' in self.data.keys():
            xlabel=self.data['title_X']
            self.ax.set_xlabel(xlabel,fontsize=8,color=_color)
        if 'title_Y' in self.data.keys():
            ylabel=self.data['title_Y']
            self.ax.set_ylabel(ylabel,fontsize=8,color=_color)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        
    def setColorAxes(self,_color):
        self.ax.tick_params(axis='x', colors=_color)    
        self.ax.tick_params(axis='y', colors=_color)
        self.ax.spines['left'].set_color(_color)        
        self.ax.spines['bottom'].set_color(_color)
        self.ax.spines['top'].set_alpha(0)        
        self.ax.spines['right'].set_alpha(0)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        
    def setColorBackground(self,_color):
        self.fig.patch.set_facecolor('#000000FF')
        self.fig.patch.set_alpha(0)
        self.ax.set_facecolor(_color)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        
    
        
        
        

        
        