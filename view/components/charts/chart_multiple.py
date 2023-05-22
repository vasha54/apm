import matplotlib.pyplot as plt
from math import pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from view.components.charts.chart_abstract import ChartAbstract

class ChartMultiple(ChartAbstract):
        
    def __init__(self,parent):
        self.fig,self.ax = plt.subplots(1,1,constrained_layout=True)
        super().__init__(self.fig,self.ax,parent)
        
    def addPlot(self,values_x,values_y,**kwargs):
        labelPlot=''
        colorPlot = '#FFFFF'
        lineStyle ='solid'
        markerPlot = None
        markersizePlot = 0
            
        if 'label' in kwargs.keys():
            labelPlot = kwargs['label']
            
        if 'color' in kwargs.keys():
            colorPlot = kwargs['color']
        
        if 'linestyle' in kwargs.keys():
            lineStyle= kwargs['linestyle']
            
        if 'marker' in kwargs.keys():
            markerPlot = kwargs['marker']
            
        if 'markersize' in kwargs.keys():
            markersizePlot = kwargs['markersize']
            
        serie = self.ax.plot(values_x,values_y,color=colorPlot,label=labelPlot,linestyle=lineStyle,marker=markerPlot,markersize=markersizePlot,antialiased=True)
        self.series.append((serie,labelPlot))
        
    def addScatter(self,values_x,values_y,**kwargs):
        
        colorPoint = "#000000"
        
        if 'c' in kwargs.keys():
            colorPoint = kwargs['c']
        
        serie=self.ax.scatter(values_x,values_y,c=colorPoint,s=2)
        self.series.append((serie,""))
    
         
    
    def setTitleY(self,_titley):
        self.data['title_Y']=_titley
        self.ax.set_ylabel(_titley,fontsize=8,color='#000000')
    
    def setTitleX(self,_titlex):
        self.data['title_X']=_titlex
        self.ax.set_xlabel(_titlex,fontsize=8,color='#000000')
    
    def setNameChart(self,nameChart):
        self.data['name']=nameChart
        self.ax.set_title(nameChart,fontsize=10,color='#000000')
    
     
    