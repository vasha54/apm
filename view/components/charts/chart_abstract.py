import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from abc import ABC, abstractmethod

class ChartAbstract (FigureCanvas):
    def __init__(self,_fig,_ax,_parent):
        self.fig = _fig
        self.ax = _ax
        super().__init__(self.fig)
        self.data = {}
        self.series = []
        self.setParent(_parent)
    
    def setColorText(self,_color):
        if 'name' in self.data.keys():
            self.ax.set_title(self.data['name'],fontsize=10,color=_color)
            
        xlabel = ''
        ylabel = ''
        
        if 'title_X' in self.data.keys():
            xlabel=self.data['title_X']
            self.ax.set_xlabel(xlabel,fontsize=8,color=_color)
        if 'title_Y' in self.data.keys():
            ylabel=self.data['title_Y']
            self.ax.set_ylabel(ylabel,fontsize=8,color=_color)
            
        if 'xticks' in self.data.keys():
            self.ax.set_xticks(self.data['xticks']) 
            
        if 'xticklabels' in self.data.keys():
            self.ax.set_xticklabels(self.data['xticklabels'])
        
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
        
    def legend(self):
        self.ax.legend()
    
    def setLimitsAxisX(self,limitsX):
        self.ax.set_xlim(limitsX)
        
    def setLimitsAxisY(self,limitsY):
        self.ax.set_ylim(limitsY)
        
    def setXTicks(self,ticksX):
        self.ax.set_xticks(list(ticksX.keys()))
        self.ax.set_xticklabels(list(ticksX.values()))
        
    def setYTicks(self,ticksY):
        self.ax.set_yticks(list(ticksY.keys()))
        self.ax.set_yticklabels(list(ticksY.values()))
        
        
    @abstractmethod
    def makeChart(self):
        "makeChart"