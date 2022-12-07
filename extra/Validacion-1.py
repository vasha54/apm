# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:57:46 2022

@author: Jonathan
"""

import numpy as np
import pandas as pd
import statsmodels.stats.diagnostic as dg
import os
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as st
import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as st
import statsmodels.api as sm  

import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as st
import seaborn as sns
import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as st
import matplotlib.pyplot as plt

##############################################################################
#Esta es la matriz de correlacion que le comenté que sería bueno incluirla 
#en la pestana de los graficos de dispersion que usted hizo

#TAL VEZ EN ESA PESTANA PUEDA PONER UN BOTON QUE DIGA "Ver correlación entre las variables¨
#Y que lo permita ver
os.chdir('E:\Tesis mias de azúcar\TESIS 2022')
df=pd.read_excel("dataSetB.xlsx")     #Lee excell

datos2=pd.DataFrame([df.Landa,df.Temp,df.polJP]) #TODAS LAS VARIABLES INDEPENDIENTES DEL MODELO
DatFrINDEP=datos2.transpose() 

Vobs=df.polRLobs

Vpre=df.polRLpred

Residuales=Vobs-Vpre


import numpy
from statistics import median
a=np.mean(Residuales)
f=np.std(Residuales)

ResidualesST=[]
m=len(Residuales)

for i in range(0,m):
    residSt=(Residuales[i]-a)/f
    ResidualesST.append(residSt)
    
###############################################################################

errorcua=residcua=pow(Residuales, 2)
Sumerrcua=sum(errorcua)

RMSE=round(np.sqrt(Sumerrcua/len(Residuales)),4)


R2pred=round(1-sum((errorcua))/sum(pow((Vobs-np.mean(Vobs)),2)),4)

n=len(Residuales)
m=2 ##############OJOJOJOJOJ CANTIDAD DE VARIABLES INDEPENDIENTES 
p=m+1 
R2adjpred=round(1-(1-R2pred)*(n-1)/(n-p),4)

#-------------------------------------------------------------------------------