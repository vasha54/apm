import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pandas as pd
from math import pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class ChartHistogram(FigureCanvas):
        
    def __init__(self,parent):
        # self.fig,self.ax = plt.subplots(subplot_kw={'projection': 'polar'})
        # super().__init__(self.fig)
        self.setParent(parent)
        
    def makeRadarChart(self,config,dataFrame):
        pass