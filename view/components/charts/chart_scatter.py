import matplotlib.pyplot as plt
from math import pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class ChartScatter(FigureCanvas):
        
    def __init__(self,parent):
        self.fig,self.ax = plt.subplots(1,1,constrained_layout=True)
        super().__init__(self.fig)
        self.data = {}
        self.setParent(parent)
        
    def makeChart(self,_data):
        self.data=_data
        
        valuesX = list()
        valuesY = list()
        sizePoints =2
        
        if 'valuesX' in _data.keys():
            valuesX = _data['valuesX']
        
        if 'valuesY' in _data.keys():
            valuesY = _data['valuesY']
        
        if 'sizePoints' in _data.keys():
            sizePoints = _data['sizePoints']
        
        if len(valuesX) != len(valuesY) :
            valuesX = list()
            valuesY = list()
        
        plt.scatter(valuesX,valuesY,s=sizePoints)
        

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