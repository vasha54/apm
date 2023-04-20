import matplotlib.pyplot as plt
from math import pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from view.components.charts.chart_abstract import ChartAbstract

class ChartHistogram(ChartAbstract):
        
    def __init__(self,parent):
        self.fig,self.ax = plt.subplots(1,1,constrained_layout=True)
        super().__init__(self.fig,self.ax,parent)
        
    def makeChart(self,_data):
        self.data=_data
        
        bars = list()
        heights = list()
        
        if 'heights' in _data.keys():
            heights = _data['heights']
        
        if 'bars' in _data.keys():
            bars = _data['bars']
        
        if len(bars) ==0 and len(heights) >0:
            for i in range(0,len(heights)):
                bars.append(i)
        
        plt.bar(bars, height=heights)
        

        if 'name' in _data.keys():
            self.ax.set_title(_data['name'],fontsize=10,color='#000000')
        
        xlabel = ''
        ylabel = ''
        if 'title_X' in _data.keys():
            xlabel=_data['title_X']
            self.ax.set_xlabel(xlabel,fontsize=8,color='#000000')
        if 'title_Y' in _data.keys():
            ylabel=_data['title_Y']
            self.ax.set_ylabel(ylabel,fontsize=8,color='#000000')
        
        if 'xticks' in _data.keys():
            self.ax.set_xticks(_data['xticks']) 
            
        if 'xticklabels' in _data.keys():
            self.ax.set_xticklabels(_data['xticklabels'])
        
    
    
        
    
        
        
        

        
        