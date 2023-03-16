import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pandas as pd
from math import pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

df = pd.DataFrame({
'models': ['Model 1', 'Modelo 2','Modelo 3', 'Modelo 4', 'Modelo 5', 'Modelo 6'],
'R-Cuadrado': [3, 1, 0, 4, 3, 4],
'AIC': [2, 1, 6, 3, 2, 2],
'Log-likehead': [0, 3, 2, 4, 4, 4],
'R-cuadrado adjustado': [2, 1, 3, 4, 2,1],
'RSME': [2, 5, 3, 4, 3, 1],
'BIC': [2, 2, 3, 4, 3, 2]
})

confiBasic = {
   'minY':0,
   'maxY':5,
   'yticks': [1,2,3,4],
   'yticksStr':["1","2","3","4"],
   'title':'Comparativa grafica entre los diferentes modelos',
   'showLegend':True
}



class ChartRadal(FigureCanvas):
    
    def __init__(self,parent):
        self.fig,self.ax = plt.subplots(subplot_kw={'projection': 'polar'})
        super().__init__(self.fig)
        self.setParent(parent)
        
              
    
    def makeRadarChart(self,config,dataFrame):
        
        my_palette = plt.cm.get_cmap("Set2", len(dataFrame.index))
        
        for row in range(0, len(dataFrame.index)):
            #print("dgdg",row)
            self.make_spider(dataFrame, row, my_palette(row))
        
        # Draw ylabels
        self.ax.set_rlabel_position(0)
        if 'minY' in config.keys() and 'maxY' in config.keys() :
            plt.ylim(float(config['minY']),float(config['maxY']))
        
        if 'yticks' in config.keys() and 'yticksStr' in config.keys():
            plt.yticks(config['yticks'], config['yticksStr'], color="grey", size=7)
        
        
        # Draw title and legend
        if 'showLegend' in config.keys() and config['showLegend'] == True:
            plt.legend(labels =dataFrame['models'],loc='center left', bbox_to_anchor=(1, 0.5))
        
        # if 'title' in config.keys():
        #     plt.title(config['title'], size=11, y=1.1)
            
    def make_spider(self,_dataFrame, row, color):
        # number of variable
        categories=list(_dataFrame)[1:]
        N = len(categories)
        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]
        
        # If you want the first axis to be on top:
        self.ax.set_theta_offset(pi / 2)
        self.ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories, color='grey', size=8)

    

    # Ind1
        values=_dataFrame.loc[row].drop('models').values.flatten().tolist()
        values += values[:1]
        self.ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
        #self.ax.fill(angles, values, color=color, alpha=0.4)
        #self.ax.legend()

    # Add a title
    
