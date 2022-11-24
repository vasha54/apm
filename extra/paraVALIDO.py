# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:57:40 2022

@author: Jonathan
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 20:19:29 2022

@author: Jonathan
"""

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
##############################################################################
#DESARROLLO DE LOS MODELOS DE REGRESION (NADA DE ESTO SE MUESTRA)

import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as st

datos=pd.DataFrame(df)    #Data frame para w con el excell NOTE QUE SE ESPECIFICA
#ANTES POR LA LINEA 39 el termino df que es el EXCEL

#Ahora viene la estructura para la el modelo: 
#VariableDependiente ~ Variable indep1+.....Variable indep
#Trabaja con unos datos llamados "datos" que corresponde a un data frame con 
#todas las variables del EXcell, ser'ia bueno que se mantuviera ese data frame
#por si incorpora una nueva variable

reg=smf.ols('polRL~Landa+Temp+polJP',datos)   #La estructura se llama reg
#En la linea anterior se define "reg" *********TERMINO MUY IMPORTANTE QUE SE
#EMPLEA LUEGO en multiples pruebas

#Ahora viene una termino muy importante que contiene toda la informacion de salida
#del modelo
resul=reg.fit()    #Calcular ''reg''
###############################################################################

m=len(datos.polRL) #Cantidad de observaciones...en este caso lo hallo por
#la longitud de la variable

#Grados de libertad del modelo       
glresiduales=resul.df_model

#Grados de libertad de los residuales 
glmodelo=resul.df_resid

#COEFICIENTES  
coeff=resul.params   

#bse Los errores standard de los parámetros estimados   
sterr=resul.bse   #De reg dame el bse

# t             
tc=resul.tvalues  

# P-valor        
pvcoeff=resul.pvalues   

#Intervalo de confianza para los coeff     *T5
alfa=0.05#Aclarar valor alfa (que debe estar entre 0 y 1)

#que deberia decir "Nivel de significacion para los intervalos de confianza
#de los coeficientes de regresión¨ 
interconf=resul.conf_int(alfa,)



#"R-cuadrado¨    *T9
rcua=round((resul.rsquared),4)

#"R-cuadrado ajustado¨   *T10
rcuadj=round((resul.rsquared_adj),4)

#"Estadígrafo de Fisher¨    *T11
ffr=round((resul.fvalue),4)

#"P-valor (Prueba de Fisher)"   *T12
Pvfisher=round((resul.f_pvalue),4)


#MSE del modelo
msemodelo=round((resul.mse_model),4)

#MSE de los residuales 
mseresid=round((resul.mse_resid),4)

#MSE total
msetotal=round((resul.mse_total),4)

#RMSE
import numpy as np
RMSE=round(np.sqrt(msetotal),4)

###############################################################################
#Otros parametros que se calcular para cada modelo

#AIC        *T13
aic=round((resul.aic),4)

#BIC
bic=round((resul.bic),4)


#Log-Likelihodd del modelo
like=round((resul.llf),4)

###############################################################################
###############################################################################

#Aqui van las variables deltaAIC,  pesoAIC, deltaBIC y pesoBIC cuyo procedimiento
#de calculo lo muestro en la hoja 3 y otras variables





    
##############################################################################
#Comprobacion de los supuestos
###############################################################################
residuales=(resul.resid)  #Residuales del modelo
rst=resul.outlier_test()
residualesST=rst.student_resid #REsiduales studentizados


#------------------Pruebas de normalidad para los residuales sin escalamiento


#"Coeficiente de Curtosis"      
from scipy.stats import kurtosis
ku=round(kurtosis(residuales),4)  
kuST=round(kurtosis(residualesST),4)

#"Coeficiente de Asimetría¨
from scipy.stats import skew
sk=round(skew(residuales),4)
skST=round(skew(residualesST),4)

#Prueba de Lilliefors
from statsmodels.stats.diagnostic import lilliefors
Li=lilliefors(residuales)
D=round(Li[0],4)
PvalorLi=round(Li[1],4)

LiST=lilliefors(residualesST)
DST=round(LiST[0],4)
PvalorLiST=round(LiST[1],4)


#Prueba de Shapiro-Wilk
from scipy import stats
shap= stats.shapiro(residuales)
W=round(shap[0],4)
PvalorW=round(shap[1],4)

shapST= stats.shapiro(residualesST)
WST=round(shapST[0],4)
PvalorWST=round(shapST[1],4)


#Prueba de Kolmogorov-Smirnov
import numpy as np
from scipy import stats
ks=stats.kstest(residuales,cdf="norm")
KS=round(ks[0],4)
Pvalorks=round(ks[1],4)


ksST=stats.kstest(residualesST,cdf="norm")
KSST=round(ksST[0],4)
PvalorksST=round(ksST[1],4)


#Prueba de Jarque-Bera
import numpy as np
from scipy.stats import stats
jarbera=stats.jarque_bera(residuales)
JB=round(jarbera[0],4)
PvalorJB=round(jarbera[1],4)


jarberaST=stats.jarque_bera(residualesST)
JBST=round(jarberaST[0],4)
PvalorJBST=round(jarberaST[1],4)


#Prueba de Anderson-Darling  
from scipy.stats import anderson
ander=anderson(residuales)
AN=round(ander[0],4)
vc=(ander[1])
VCand=round(vc[2],4)

anderST=anderson(residualesST)
ANST=round(anderST[0],4)
vcST=(anderST[1])
VCandST=round(vcST[2],4)



#Prueba de K-cuad de D'Angostino
from scipy.stats import normaltest
dan=stat, p = normaltest(residuales)
DA=round(dan[0],4)
PvalorDA=round(dan[1],4)


danST=stat, p = normaltest(residualesST)
DAST=round(danST[0],4)
PvalorDAST=round(danST[1],4)



#Prueba de Chi-Cuadrado
from scipy import stats
import numpy as np
chi=stats.chisquare(residuales)
CHI=round(chi[0],4)
PvalorCHI=round(chi[1],4)


chiST=stats.chisquare(residualesST)
CHIST=round(chiST[0],4)
PvalorCHIST=round(chiST[1],4)


#################HISTOGRAMAS DE FRECUENCIA PARA RESIDUALES SIN ESCALAMIENTO

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
mu, std = norm.fit(residuales) 

fig, ax = plt.subplots()
# plot the residuals
sns.histplot(x=residuales, ax=ax, stat="density", linewidth=0, kde=True)
ax.set(title="Distribución de los residuales sin escalamiento", xlabel="Residuales",ylabel="Densidad")

# plot corresponding normal curve
xmin, xmax = plt.xlim() # the maximum x values from the histogram above
x = np.linspace(xmin, xmax, 100) # generate some x values
p = stats.norm.pdf(x, mu, std) # calculate the y values for the normal curve
sns.lineplot(x=x, y=p, color="orange", ax=ax)
plt.show()
###############################################################################

#################HISTOGRAMAS DE FRECUENCIA PARA RESIDUALES ESTUDENTIZADOS

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
mu, std = norm.fit(residualesST)

fig, ax = plt.subplots()
# plot the residuals
sns.histplot(x=residualesST, ax=ax, stat="density", linewidth=0, kde=True)
ax.set(title="Distribución de los residuales estudentizados", xlabel="Residuales estudentizados",ylabel="Densidad")

# plot corresponding normal curve
xmin, xmax = plt.xlim() # the maximum x values from the histogram above
x = np.linspace(xmin, xmax, 100) # generate some x values
p = stats.norm.pdf(x, mu, std) # calculate the y values for the normal curve
sns.lineplot(x=x, y=p, color="orange", ax=ax)
plt.show()
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


#        HOMOCEDASTICIDAD
#############################################################################
#Prueba de Breush-Pagan
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

import statsmodels.stats.api as sms

breushp = sms.het_breuschpagan(residuales, resul.model.exog)
BP=breushp [0]
Pvalor=breushp [1]

#Prueba de Goldfeld-Quandt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
golqua = sms.het_goldfeldquandt(residuales,resul.model.exog)
GQ=golqua[0]
PvalorGQ=golqua[1]

#Prueba de White
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from statsmodels.stats.diagnostic import het_white
white=het_white(residuales,resul.model.exog)
LMw=white[0]
PvalorLMw=white[1]
Fw=white[2]
PvalorFw=white[3]

#Grafica de Residuales vs Valores Ajustados

# fitted values
import matplotlib.pyplot as plt
import seaborn as sns
model_fitted_y = resul.fittedvalues

#  Plot
plot = sns.residplot(x=model_fitted_y, y='polRL', data=datos, lowess=True, 
                     scatter_kws={'alpha': 0.5}, 
                     line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})

# Titel and labels
plot.set_title('Residuales vs Ajustados')
plot.set_xlabel('Valores ajustados')
plot.set_ylabel('Residuales')
plt.show()
#-----------------------------------------------------------------------------

#Supuesto de independencia

#Durbin-Watson
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.stattools import durbin_watson
durbinwat=durbin_watson(residuales)
DW=durbinwat

#Breush-Godfrey 
import statsmodels.stats.diagnostic as dg
bregod=dg.acorr_breusch_godfrey(resul, nlags=3, store=False)
BG=bregod[0]
PvalorBG=bregod[1]



#Grafica de Residuales vs Valores Ajustados
import matplotlib.pyplot as plt
import seaborn as sns

Y_max = datos.polRL.max()
Y_min = datos.polRL.min()
Y=datos.polRL

predicted_value=resul.fittedvalues
true_value=datos.polRL

ax = sns.scatterplot(x=predicted_value, y=Y)
ax.set(ylim=(Y_min, Y_max))
ax.set(xlim=(Y_min, Y_max))
ax.set_xlabel("Valores predichos")
ax.set_ylabel("Valores observados")

X_ref = Y_ref = np.linspace(Y_min, Y_max, 100)
plt.plot(X_ref, Y_ref, color='red', linewidth=1)
plt.show()

#------------------------------------------------------------------------------
#Otras pruebas de adecuacion del modelo

#Media de los errores
from numpy import mean
import statsmodels.api as sm
proerror=mean(resul.resid)
proerrorST=mean(residualesST)

df=pd.read_excel("dataSetA.xlsx")     #Lee excell
datos2=pd.DataFrame([df.Landa,df.Temp,df.polJP,df.polRL]) #TODAS LAS VARIABLES DEL MODELO
X=datos2.transpose()  
X_constant=sm.add_constant(X)
#Valor de inflación de la varianza
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif = [variance_inflation_factor(X_constant.values, i) for i in range(X_constant.shape[1])]

Viftable=pd.DataFrame({'vif': vif[1:]}, index=X.columns).T




#Deteccion de puntos influyentes por la distancia de Cook
# obtain Cook's distance 
import statsmodels.api as sm
from statsmodels.formula.api import ols
lm=ols('polRL~Landa+Temp+polJP',datos).fit()   #La estructura se llama reg
lm_cooksd = lm.get_influence().cooks_distance[0]

#---------------------------------------------------
#NEW INFLUENCE

import statsmodels.api as sm

df=pd.read_excel("dataSetA.xlsx")     #Lee excell
datos5=pd.DataFrame([df.Landa,df.Temp,df.polJP]) #TODAS LAS VARIABLES INDEP
B=datos5.transpose()  
B_constant=sm.add_constant(B)
y=datos.polRL
lin_reg=sm.OLS(y,B_constant).fit()
fig,ax=plt.subplots(figsize=(12,8))
sm.graphics.influence_plot(lin_reg, aplha=0.05,ax=ax,criterion="cooks")

influence = lin_reg.get_influence()
pd.Series(influence.hat_matrix_diag).describe()

influence = lin_reg.get_influence()
inf_sum = influence.summary_frame()

print(inf_sum.head())

student_resid = influence.resid_studentized_external
(cooks, p) = influence.cooks_distance
(dffits, p) = influence.dffits
leverage = influence.hat_matrix_diag

print ('\n')
print ('Leverage vs. Residuales estudentizados')
sns.regplot(leverage, lin_reg.resid_pearson,  fit_reg=False)
plt.title('Leverage vs. Residuales estudentizados')
plt.xlabel('Leverage')
plt.ylabel('Residuales estudentizados')

#--------------Identificar outlayer por los residuales estudientizados
from statsmodels.formula.api import ols

#Plot influential observations
#Use residual squared to restrict the graph but preserve the relative position of observations

from statsmodels.graphics.regressionplots import *
plot_leverage_resid2(lm)
plt.show()


#General influencia con Cook


# Instantiate and fit the visualizer
from yellowbrick.regressor import CooksDistance
visualizer = CooksDistance()

df=pd.read_excel("dataSetA.xlsx")     #Lee excell
datos6=pd.DataFrame([df.Landa,df.Temp,df.polJP]) #TODAS LAS VARIABLES INDEP
X1=datos6.transpose()  


visualizer.fit(X1, y)
visualizer.show()


















#Test de Ramsey
import numpy as np
import pandas as pd
import statsmodels.regression.linear_model as rg
import statsmodels.tools.tools as ct
import statsmodels.stats.diagnostic as dg
lm=ols('polRL~Landa+Temp+polJP',datos).fit()   #La estructura se llama reg
reg1=lm
power=2  #ESPECIFICAR POWER
reset=dg.linear_reset(lm,power,test_type='fitted', use_f=True)


import pandas as pd
import numpy as np
import itertools
from itertools import chain, combinations
import statsmodels.formula.api as sm
import scipy.stats as scipystats
import statsmodels.api as sm
import statsmodels.stats.stattools as stools
import statsmodels.stats as stats 
from statsmodels.graphics.regressionplots import *
import matplotlib.pyplot as plt
import seaborn as sns
import copy
from sklearn.model_selection import train_test_split
import math
import time




#------------------------------------------------------------------------------