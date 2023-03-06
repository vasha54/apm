import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pandas as pd
from math import pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

df = pd.DataFrame({
'models': ['Model 1', 'Modelo 2','Modelo 3', 'Modelo 4', 'Modelo 5', 'Modelo 6'],
'R-Cuadrado': [38, 1.5, 30, 4, 30, 4],
'Log-likehead': [29, 10, 9, 34, 23, 24],
'AIC': [8, 39, 23, 24, 34, 34],
'R-cuadrado adjustado': [7, 31, 33, 14, 12,14],
'RSME': [28, 15, 32, 14, 23, 12],
'BIC': [22, 25, 23, 14, 13, 22]
})



class ChartRadal(FigureCanvas):
    
    def __init__(self,parent):
        self.fig,self.ax = plt.subplots(subplot_kw={'projection': 'polar'})
        super().__init__(self.fig)
        self.setParent(parent)
        
              
    
    def makeRadarChart(self,name):
        
        my_palette = plt.cm.get_cmap("Set2", len(df.index))
        
        for row in range(0, len(df.index)):
            self.make_spider( row=row, color=my_palette(row))
        plt.legend(labels =df['models'])
        plt.title(name, size=11, y=1.1)
            
    def make_spider(self, row, color):
        # number of variable
        categories=list(df)[1:]
        N = len(categories)
        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]
        
        # If you want the first axis to be on top:
        self.ax.set_theta_offset(pi / 2)
        self.ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
        self.ax.set_rlabel_position(0)
        plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
        plt.ylim(0,40)

    # Ind1
        values=df.loc[row].drop('models').values.flatten().tolist()
        values += values[:1]
        self.ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
        self.ax.fill(angles, values, color=color, alpha=0.4)
        #self.ax.legend()

    # Add a title
    
