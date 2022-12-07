# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:22:52 2022

@author: Jonathan
"""
#Test de Ramsey
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
df=pd.read_excel("dataSetA.xlsx")     #Lee excell
#NOTE QUE AHORA HAGO UN DATAFRAME CON TODAS LAS VARIABLES TANTO LA DEPENDIENTE
#CON LAS INDEPENDIENTES
datos2=pd.DataFrame([df.Landa,df.Temp,df.polJP,df.polRL]) #TODAS LAS VARIABLES DEL MODELO
#LE HAGO LA TRASPUESTA Y ESA ES LA QUE SE COJE PA EL GRAFICO QUE CORRESPONDE A LA SECCION
X=datos2.transpose() 
#COrrelacion entre las variables
sns.heatmap(X.corr(),annot=True) #**********GRAIFCO*************
plt.show()
import numpy as np
corr=np.corrcoef(datos2)  #OJO ES CON LA TRASPUESTA DEL DE VALIDO
##############################################################################
#DESARROLLO DE LOS MODELOS DE REGRESION (NADA DE ESTO SE MUESTRA)

import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as st
import pandas as pd                        
import statsmodels.api as sm                
import statsmodels.formula.api as smf       

datos=pd.DataFrame(df)    #Data frame para w con el excell NOTE QUE SE ESPECIFICA
#ANTES POR LA LINEA 39 el termino df que es el EXCEL

#Ahora viene la estructura para la el modelo: 
#VariableDependiente ~ Variable indep1+.....Variable indep
#Trabaja con unos datos llamados "datos" que corresponde a un data frame con 
#todas las variables del EXcell, ser'ia bueno que se mantuviera ese data frame
#por si incorpora una nueva variable

reg=smf.ols('polRL~Landa+Temp+polJP',datos)   #La estructura se llama reg
resul=reg.fit() 

#TEST RAMSEY 
import statsmodels.formula.api as smf  
from statsmodels.stats.diagnostic import linear_reset

power=2  #ESPECIFICAR POWER
#Ramsey's RESET test for neglected nonlinearity
ramsey=dg.linear_reset(resul,power,test_type='fitted', use_f=True)

#Rainbow test for linearity
rainbow=dg.linear_rainbow(resul, frac=0.5, order_by=None, use_distance=False,center=None)
F=round(rainbow[0],4)
PvF=round(rainbow[1],4)

#Harvey Collier test for linearity
harvey=dg.linear_harvey_collier(resul, order_by=None, skip=None)
HC=round(harvey[0],4)
PvHC=round(harvey[1],4)

#Lagrange multiplier test for linearity against functional alternative
residuales=(resul.resid)
Lagrange=dg.linear_lm(residuales, resul.model.exog, func=None)
Lagrange[2]

# # White's Two-Moment Specification Test
whitespec=dg.spec_white(residuales, resul.model.exog)
WE=round(whitespec[0],4)
PvWE=round(whitespec[1],4)


#Media de los errores
from numpy import mean
import statsmodels.api as sm
residuales=(resul.resid)  
proerror=mean(resul.resid)
rst=resul.outlier_test()
residualesST=rst.student_resid 
proerrorST=mean(residualesST)

#------------------------------------------------------------------------------

#GRAFICOS 

import statsmodels.api as sm
from scipy.stats import norm
mu, std = norm.fit(residuales) 


xH3=residuales  
kde = sm.nonparametric.KDEUnivariate(xH3)
kde.fit()  # Estimate the densities
xlineaAZ=kde.support  #KDE (univariante)
ylineaAZ=kde.density

plt.plot(xlineaAZ, ylineaAZ, color='red', linewidth=1)
plt.show()
g=len(xlineaAZ)

XH3min=min(xH3)
XH3max=max(xH3)
x = np.linspace(XH3min, XH3max, g) # generate some x values


p = norm.pdf(x, mu, std)
plt.plot(xlineaAZ,p, color='red', linewidth=1)
plt.show()

#IMPORTANTEESTABLECER EL MXM DE LA GRAFICA APARTIR DEL MXM DE LAS DOS CURVAS
#COSA  Q NOO VAYA A QUEDAR UNA TRUUNCADA


#------------------------------------------------------------------------------
#LO MISMO PERO PA RESIDUALES ESTUDENTIZADOS
import statsmodels.api as sm
from scipy.stats import norm
mu1, std1 = norm.fit(residualesST) 


xH4=residualesST
kde1 = sm.nonparametric.KDEUnivariate(xH4)
kde1.fit()  # Estimate the densities
xlineaAZ1=kde1.support  #KDE (univariante)
ylineaAZ1=kde1.density

plt.plot(xlineaAZ, ylineaAZ, color='red', linewidth=1)
plt.show()
g=len(xlineaAZ)

XH4min=min(xH4)
XH4max=max(xH4)
x1 = np.linspace(XH4min, XH4max, g) # generate some x values


p1 = norm.pdf(x1, mu1, std1)
plt.plot(xlineaAZ,p1, color='red', linewidth=1)
plt.show()

#IMPORTANTEESTABLECER EL MXM DE LA GRAFICA APARTIR DEL MXM DE LAS DOS CURVAS
#COSA  Q NOO VAYA A QUEDAR UNA TRUUNCADA

#------------------------------------------------------------------------------



###############################################################################


#Grafico QQ Residuales sin escalamiento
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
qqplot(residuales, line='s',xlabel = "Probabilidades teóricas",ylabel = "Cuartiles de la muestra ")
h = plt.title("Q-Q para residuales sin escalamiento")

plt.show()
###############################################################################
#Grafico QQ Residuales estudentizados
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
qqplot(residualesST, line='s',xlabel = "Probabilidades teóricas",ylabel = "Cuartiles de la muestra ")
h = plt.title("Q-Q para residuales estudentizados")

plt.show()

###############################################################################

#******************************************GRAFICO H1
yH1=residuales=(resul.resid)  #VARIABLE Y DEL GRAFICO
xH1=resul.fittedvalues #VARIABLE X DEL GRÁFICO

from statsmodels.nonparametric.smoothers_lowess import lowess
grid, yhat=lowess(yH1, xH1).T

xline1=grid   #Variable x de la linea roja

yline1=yhat   #Variable y de la linea roja

###############################################################################

# #Grafica de Residuales vs Valores Ajustados
# import matplotlib.pyplot as plt
# import seaborn as sns

# Y_max = datos.polRL.max()
# Y_min = datos.polRL.min()
# Y=datos.polRL

predicted_value=resul.fittedvalues
# true_value=datos.polRL

###############################################################################

import statsmodels.api as sm
import numpy

df=pd.read_excel("dataSetA.xlsx")     #Lee excell
datos5=pd.DataFrame([df.Landa,df.Temp,df.polJP]) #TODAS LAS VARIABLES INDEP
B=datos5.transpose()  
B_constant=sm.add_constant(B)
y=datos.polRL
lin_reg=sm.OLS(y,B_constant).fit()


influence = lin_reg.get_influence()
leverage = influence.hat_matrix_diag #Leverage
cooks= influence.cooks_distance  #Distancia de Coock
residualesST
residuales

t=len(datos.polRL)
obs=np.linspace(1,t,t)
k=4   #Cantidad de par'ametros del modelo incluido el intercepto
ddfitCrit=2*np.sqrt(k/t)   #
covCrit=3*np.sqrt(k/t) #*******************
levgCrit1=2*k/t
levgCrit2=6/t
cookCrit1=1
cookCrit2=4/t

dffits=influence.dffits[0]
# dfbetas=influence.dfbetas
hat=influence.hat_matrix_diag
cov_ratio=influence.cov_ratio
#------------------------------------------------------------------------------
#Para extraer la dfbetas de un coeficiente
dfbetas=influence.dfbetas
n=0  #numero del coeficicente (en este caso intercepto)
g=len(datos.polRL) #Cantidad de obsservaciones MENOS 1

betascoeff=list()

for i in range(g):
    betascoeff.append(dfbetas[i][n]) #DA LOS VALORES
betascoeff

dbetaCrit=2/np.sqrt(t)    #betacritico


#------------------------------------------------------------------------------
#Validacion Cruzada
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from matplotlib import pyplot as plt
from sklearn.model_selection import cross_validate
from sklearn.metrics import mean_squared_error
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

datos2=pd.DataFrame([df.polRL,df.Landa,df.Temp,df.polJP]) #TODAS LAS VARIABLES DEL MODELO
datos3=datos2.transpose() #Trasouesta


y=datos3.polRL #VARIABLE DEPENDIENTE

x=pd.DataFrame([df.Landa,df.Temp,df.polJP]) #VARIABLES INDEPENDIENTES

X=x.transpose()
clf = LinearRegression()
model=clf.fit(X, y) #Regresion x esta libreria

k=5   #INFORMACION QUE SE ESPECIFICA*******SON LOS FOLDS (tiene que ser mayor que 2)
kfolds=np.linspace(1,k,k)

scores = cross_validate(model, X, y, cv=k,scoring=('r2', 'neg_mean_squared_error'), return_train_score=True)
a=scores['test_neg_mean_squared_error']
b=scores['train_neg_mean_squared_error']
c=scores['test_r2']
d=scores['train_r2']

predictions=cross_val_predict(clf,X,y,cv=k)

e=metrics.r2_score(y,predictions)

f=metrics.mean_squared_error(y,predictions)

g=np.sqrt(f)


plt.scatter(predictions,y)  #Predichos por k-Folds vs observados
plt.scatter(predicted_value,predictions) #Valores predichos por el modelo completo
                                         #predicciones por k-folds
#######PONER LUEGO LOS RESUMENES
amenan=np.mean(a)      #MEDIA
bmenan=np.mean(b)
cmenan=np.mean(c)
dmenan=np.mean(d)

cvar = lambda x: np. std (x, ddof = 1 ) / np. mean (x) * 100

acv=cvar(a)            #CV
bcv=cvar(b)
ccv=cvar(c)
dcv=cvar(d)

###############################################################################
import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#let's select the number of bootstraps we want

Datosboot1=pd.DataFrame([df.Landa,df.Temp,df.polJP,df.polRL]) #TODAS LAS VARIABLES DEL MODELO
#LE HAGO LA TRASPUESTA Y ESA ES LA QUE SE COJE PA EL GRAFICO QUE CORRESPONDE A LA SECCION
data_df=Datosboot1.transpose() 
boots=1000

boot_coeff = []
boot_rcuadj = []
boot_RMSE = []
coeffs=[]

k=len(data_df.polRL)
for _ in range(boots):
 # sample the rows, same size, with replacement
 sample_df = data_df.sample(n=k, replace=True)
 regbst=smf.ols('polRL~Landa+Temp+polJP',sample_df) 
 resulbst=regbst.fit()   
 coeffbst=resulbst.params   
 rcuadjbst=resulbst.rsquared_adj
 RMSEbst=np.sqrt(resulbst.mse_total) 
  
 # append coefficients
 
 boot_rcuadj.append(rcuadjbst)
 boot_RMSE.append(RMSEbst) 
 boot_coeff.append(coeffbst)
 
RMSEbtmean=np.mean(boot_RMSE)
Rcuadjbtmean=np.mean(boot_rcuadj)

cvar = lambda x: np. std (x, ddof = 1 ) / np. mean (x) * 100
RMSEcv=cvar(boot_RMSE)
Rcuacv=cvar(boot_rcuadj)

#------------------------------------------------------------------------------
Coeffs=[]
ab=boots

n=0  #numero del coeficicente (en este caso intercepto)
for i in range(0,ab):    
    Coeffs.append(boot_coeff[i][n])
  
Coeffs  #Valores del coeficiente segun n    
Coeffmean=round(np.mean(Coeffs),4)
CoeffCv=round(cvar(Coeffs),4)
medianaCoff=round(np.percentile(Coeffs,50),4)
#------------------------------------------------------------------------------
#SIn escalamiento
from scipy import stats
from scipy import stats
import matplotlib.pyplot 
from scipy import stats

[u1,u2]=stats.probplot(residuales, sparams=(), dist='norm', fit=False, plot=None, rvalue=False)

[u3,u4]=stats.probplot(residuales, sparams=(), dist='norm', fit=True, plot=None, rvalue=False)

slope=u4[0]
intercept=u4[1]
u1 #las x
u2 #las y

matplotlib.pyplot.scatter(u1,u2)
plt.show()

#Con escalamiento

from scipy import stats
from scipy import stats
import matplotlib.pyplot 
from scipy import stats

[u5,u6]=stats.probplot(residualesST, sparams=(), dist='norm', fit=False, plot=None, rvalue=False)

[u7,u8]=stats.probplot(residualesST, sparams=(), dist='norm', fit=True, plot=None, rvalue=False)


u5 #las x
u6 #las y


slope1=u8[0]
intercept1=u8[1]
matplotlib.pyplot.scatter(u5,u6)
plt.show()

#------------------------------------------------------------------------------
import numpy
from statistics import median
x=[2,5,4,9,8,10]
a=round(np.mean(x),4)
b=max(x)
c=min(x)

cvar = lambda x: np. std (x, ddof = 1 ) / np. mean (x) * 100
d=round(cvar(x),4)

e=round(np.var(x),4)
f=round(np.std(x),4)

g=round(median(x),4)

h=len(x)