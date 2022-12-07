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


##############################################################################
# Cargar el Excell y los datos
import statsmodels.stats as stats
from matplotlib.patches import Patch
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_validate
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score, cross_val_predict
import scipy.stats
import time
import math
from sklearn.model_selection import train_test_split
import copy
import statsmodels.stats.stattools as stools
import scipy.stats as scipystats
import statsmodels.formula.api as sm
from itertools import chain, combinations
import itertools
from statsmodels.stats.diagnostic import linear_reset
from yellowbrick.regressor import CooksDistance
from statsmodels.graphics.regressionplots import *
from numpy import mean
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.stats.diagnostic as dg
from statsmodels.stats.stattools import durbin_watson
from statsmodels.formula.api import ols
from statsmodels.nonparametric.smoothers_lowess import lowess
from statsmodels.stats.diagnostic import het_white
import statsmodels.stats.api as sms
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import norm
from scipy.stats import normaltest
from scipy.stats import anderson
from scipy.stats import stats
from scipy import stats
from statsmodels.stats.diagnostic import lilliefors
from scipy.stats import skew
from scipy.stats import kurtosis
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
os.chdir('E:\Tesis mias de azúcar\TESIS 2022')
df = pd.read_excel("dataSetA.xlsx")  # Lee excell

# TODAS LAS VARIABLES DEL MODELO
datos2 = pd.DataFrame([df.Landa, df.Temp, df.polJP, df.polRL])
# LE HAGO LA TRASPUESTA Y ESA ES LA QUE SE COJE PA EL GRAFICO QUE CORRESPONDE A LA SECCION
X = datos2.transpose()
# Correlacion entre las variables
sns.heatmap(X.corr(), annot=True)  # **********GRAIFCO*************
plt.show()
##############################################################################
# DESARROLLO DE LOS MODELOS DE REGRESION


datos = pd.DataFrame(df)

reg = smf.ols('polRL~Temp+Landa+polJP', datos)  # La estructura se llama reg

resul = reg.fit()  # Calcular ''reg''
###############################################################################

m = len(datos.polRL)  # Cantidad de observaciones...en este caso lo hallo por
# la longitud de la variable

# Grados de libertad del modelo
glresiduales = resul.df_model

# Grados de libertad de los residuales
glmodelo = resul.df_resid

# COEFICIENTES
coeff = resul.params

# bse Los errores standard de los parámetros estimados
sterr = resul.bse  # De reg dame el bse

# t
tc = resul.tvalues

# P-valor
pvcoeff = resul.pvalues

# Intervalo de confianza para los coeff     *T5
alfa = 0.05  # Aclarar valor alfa (que debe estar entre 0 y 1)

# que deberia decir "Nivel de significacion para los intervalos de confianza
# de los coeficientes de regresión¨
interconf = resul.conf_int(alfa,)


# "R-cuadrado¨    *T9
rcua = round((resul.rsquared), 4)

# "R-cuadrado ajustado¨   *T10
rcuadj = round((resul.rsquared_adj), 4)

# "Estadígrafo de Fisher¨    *T11
ffr = round((resul.fvalue), 4)

#"P-valor (Prueba de Fisher)"   *T12
Pvfisher = round((resul.f_pvalue), 4)


# MSE del modelo
msemodelo = round((resul.mse_model), 4)

# MSE de los residuales
mseresid = round((resul.mse_resid), 4)

# MSE total
msetotal = round((resul.mse_total), 4)

# RMSE
RMSE = round(np.sqrt(msetotal), 4)

###############################################################################
# Otros parametros que se calculan para cada modelo

#AIC        *T13
aic = round((resul.aic), 4)

# BIC
bic = round((resul.bic), 4)


# Log-Likelihodd del modelo
like = round((resul.llf), 4)


##############################################################################
# Comprobacion de los supuestos
###############################################################################
residuales = (resul.resid)  # Residuales del modelo
rst = resul.outlier_test()
residualesST = rst.student_resid  # Residuales studentizados

# ------------------Pruebas de normalidad para los residuales sin escalamiento

#"Coeficiente de Curtosis"
ku = round(kurtosis(residuales), 4)
kuST = round(kurtosis(residualesST), 4)

# "Coeficiente de Asimetría¨
sk = round(skew(residuales), 4)
skST = round(skew(residualesST), 4)

# Prueba de Lilliefors
Li = lilliefors(residuales)
D = round(Li[0], 4)
PvalorLi = round(Li[1], 4)

LiST = lilliefors(residualesST)
DST = round(LiST[0], 4)
PvalorLiST = round(LiST[1], 4)


# Prueba de Shapiro-Wilk
shap = stats.shapiro(residuales)
W = round(shap[0], 4)
PvalorW = round(shap[1], 4)

shapST = stats.shapiro(residualesST)
WST = round(shapST[0], 4)
PvalorWST = round(shapST[1], 4)


# Prueba de Kolmogorov-Smirnov
ks = stats.kstest(residuales, cdf="norm")
KS = round(ks[0], 4)
Pvalorks = round(ks[1], 4)


ksST = stats.kstest(residualesST, cdf="norm")
KSST = round(ksST[0], 4)
PvalorksST = round(ksST[1], 4)


# Prueba de Jarque-Bera
jarbera = stats.jarque_bera(residuales)
JB = round(jarbera[0], 4)
PvalorJB = round(jarbera[1], 4)


jarberaST = stats.jarque_bera(residualesST)
JBST = round(jarberaST[0], 4)
PvalorJBST = round(jarberaST[1], 4)


# Prueba de Anderson-Darling
ander = anderson(residuales)
AN = round(ander[0], 4)
vc = (ander[1])
VCand = round(vc[2], 4)

anderST = anderson(residualesST)
ANST = round(anderST[0], 4)
vcST = (anderST[1])
VCandST = round(vcST[2], 4)


# Prueba de K-cuad de D'Angostino
dan = stat, p = normaltest(residuales)
DA = round(dan[0], 4)
PvalorDA = round(dan[1], 4)


danST = stat, p = normaltest(residualesST)
DAST = round(danST[0], 4)
PvalorDAST = round(danST[1], 4)


# Prueba de Chi-Cuadrado
chi = stats.chisquare(residuales)
CHI = round(chi[0], 4)
PvalorCHI = round(chi[1], 4)


chiST = stats.chisquare(residualesST)
CHIST = round(chiST[0], 4)
PvalorCHIST = round(chiST[1], 4)


# HISTOGRAMAS DE FRECUENCIA PARA RESIDUALES SIN ESCALAMIENTO

mu, std = norm.fit(residuales)

fig, ax = plt.subplots()
# plot the residuals
sns.histplot(x=residuales, ax=ax, stat="density", linewidth=0, kde=True)
ax.set(title="Distribución de los residuales sin escalamiento",
       xlabel="Residuales", ylabel="Densidad")

# plot corresponding normal curve
xmin, xmax = plt.xlim()  # the maximum x values from the histogram above
x = np.linspace(xmin, xmax, 100)  # generate some x values
p = stats.norm.pdf(x, mu, std)  # calculate the y values for the normal curve
sns.lineplot(x=x, y=p, color="orange", ax=ax)
plt.show()
###############################################################################

# HISTOGRAMAS DE FRECUENCIA PARA RESIDUALES ESTUDENTIZADOS
# import cv2
mu, std = norm.fit(residualesST)

fig, ax = plt.subplots()
# plot the residuals
sns.histplot(x=residualesST, ax=ax, stat="density", linewidth=0, kde=True)
ax.set(title="Distribución de los residuales estudentizados",
       xlabel="Residuales estudentizados", ylabel="Densidad")

# plot corresponding normal curve
xmin, xmax = plt.xlim()  # the maximum x values from the histogram above
x = np.linspace(xmin, xmax, 100)  # generate some x values
p = stats.norm.pdf(x, mu, std)  # calculate the y values for the normal curve
sns.lineplot(x=x, y=p, color="orange", ax=ax)
plt.show()
# cv2.imwrite("E:/Tesis mias de azúcar/TESIS 2022/lena,jpg",im)
# Histograma normal H3

xH3 = residuales
kde = sm.nonparametric.KDEUnivariate(xH3)
kde.fit()  # Estimate the densities
xlineaAZ = kde.support
ylineaAZ = kde.density

plt.plot(xlineaAZ, ylineaAZ, color='red', linewidth=1)
plt.show()
g = len(xlineaAZ)
x = np.linspace(xmin, xmax, g)  # generate some x values
p = stats.norm.pdf(x, mu, std)  # calculate the y values for the normal curve

plt.plot(xlineaAZ, p, color='red', linewidth=1)
plt.show()


###############################################################################

# Grafico QQ Residuales sin escalamiento
qqplot(residuales)
plt.show()
###############################################################################
# Grafico QQ Residuales estudentizados
qqplot(residualesST, line='s', xlabel="Probabilidades teóricas",
       ylabel="Cuartiles de la muestra ")
h = plt.title("Q-Q para residuales estudentizados")

plt.show()


#        HOMOCEDASTICIDAD
#############################################################################
# Prueba de Breush-Pagan


breushp = sms.het_breuschpagan(residuales, resul.model.exog)
BP = round(breushp[0], 4)
PvalorBP = round(breushp[1], 4)

# Prueba de Goldfeld-Quandt
golqua = sms.het_goldfeldquandt(residuales, resul.model.exog)
GQ = round(golqua[0], 4)
PvalorGQ = round(golqua[1], 4)

# Prueba de White
white = het_white(residuales, resul.model.exog)
LMw = round(white[0], 4)
PvalorLMw = round(white[1], 4)
Fw = round(white[2], 4)
PvalorFw = round(white[3], 4)

# Grafica de Residuales vs Valores Ajustados

# fitted values
model_fitted_y = resul.fittedvalues

# ******************************************GRAFICO H1
yH1 = residuales = (resul.resid)  # VARIABLE Y DEL GRAFICO
xH1 = predicted_value = resul.fittedvalues  # VARIABLE X DEL GRÁFICO

grid, yhat = lowess(yH1, xH1).T

xline = grid  # Variable x de la linea roja

yline = yhat  # Variable y de la linea roja

# ******************************************************************************
#  Plot
plot = sns.residplot(x=model_fitted_y, y='polRL', data=datos, lowess=True,
                     scatter_kws={'alpha': 0.5},
                     line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})

# Titel and labels
plot.set_title('Residuales vs Ajustados')
plot.set_xlabel('Valores ajustados')
plot.set_ylabel('Residuales')
plt.show()
# -----------------------------------------------------------------------------

# Supuesto de independencia

# Durbin-Watson
durbinwat = durbin_watson(residuales)
DW = round(durbinwat, 4)

# Breush-Godfrey
bregod = dg.acorr_breusch_godfrey(resul, nlags=3, store=False)
BG = round(bregod[0], 4)
PvalorBG = round(bregod[1], 4)


# Grafica de Residuales vs Valores Ajustados

Y_max = datos.polRL.max()
Y_min = datos.polRL.min()
Y = datos.polRL

predicted_value = resul.fittedvalues
true_value = datos.polRL

ax = sns.scatterplot(x=predicted_value, y=Y)
ax.set(ylim=(Y_min, Y_max))
ax.set(xlim=(Y_min, Y_max))
ax.set_xlabel("Valores predichos")
ax.set_ylabel("Valores observados")

X_ref = Y_ref = np.linspace(Y_min, Y_max, 100)
plt.plot(X_ref, Y_ref, color='red', linewidth=1)
plt.show()

# ------------------------------------------------------------------------------
# Otras pruebas de adecuacion del modelo


df = pd.read_excel("dataSetA.xlsx")  # Lee excell
# TODAS LAS VARIABLES DEL
datos2 = pd.DataFrame([df.Landa, df.Temp, df.polJP, df.polRL])
# MODELO incluyendo tanto la independiente como la independiente
X = datos2.transpose()
X_constant = sm.add_constant(X)
# Valor de inflación de la varianza
vif = [variance_inflation_factor(X_constant.values, i)
       for i in range(X_constant.shape[1])]

Viftable = pd.DataFrame({'vif': vif[1:]}, index=X.columns).T


# Media de los errores
proerror = mean(resul.resid)
proerrorST = mean(residualesST)


# -----------------------------------------------------------------------------


# Deteccion de puntos influyentes por la distancia de Cook
# obtain Cook's distance
lm = ols('polRL~Landa+Temp+polJP', datos).fit()  # La estructura se llama reg
lm_cooksd = lm.get_influence().cooks_distance[0]

# ---------------------------------------------------
# NEW INFLUENCE


df = pd.read_excel("dataSetA.xlsx")  # Lee excell
datos5 = pd.DataFrame([df.Landa, df.Temp, df.polJP]
                      )  # TODAS LAS VARIABLES INDEP
B = datos5.transpose()
B_constant = sm.add_constant(B)
y = datos.polRL
lin_reg = sm.OLS(y, B_constant).fit()
fig, ax = plt.subplots(figsize=(12, 8))
sm.graphics.influence_plot(lin_reg, aplha=0.05, ax=ax, criterion="cooks")


influence = lin_reg.get_influence()
pd.Series(influence.hat_matrix_diag).describe()

influence = lin_reg.get_influence()
inf_sum = influence.summary_frame()

print(inf_sum.head())

student_resid = influence.resid_studentized_external
(cooks, p) = influence.cooks_distance
(dffits, p) = influence.dffits
leverage = influence.hat_matrix_diag

print('\n')
print('Leverage vs. Residuales estudentizados')
sns.regplot(leverage, lin_reg.resid_pearson,  fit_reg=False)
plt.title('Leverage vs. Residuales estudentizados')
plt.xlabel('Leverage')
plt.ylabel('Residuales estudentizados')

# --------------Identificar outlayer por los residuales estudientizados

# Plot influential observations
# Use residual squared to restrict the graph but preserve the relative position of observations

plot_leverage_resid2(lm)
plt.show()


# General influencia con Cook


# Instantiate and fit the visualizer
visualizer = CooksDistance()

df = pd.read_excel("dataSetA.xlsx")  # Lee excell
datos6 = pd.DataFrame([df.Landa, df.Temp, df.polJP]
                      )  # TODAS LAS VARIABLES INDEP
X1 = datos6.transpose()
visualizer.fit(X1, y)
visualizer.show()


# TEST RAMSEY

power = 2  # ESPECIFICAR POWER
# Ramsey's RESET test for neglected nonlinearity
ramsey = dg.linear_reset(resul, power, test_type='fitted', use_f=True)

# Rainbow test for linearity
rainbow = dg.linear_rainbow(
    resul, frac=0.5, order_by=None, use_distance=False, center=None)
F = round(rainbow[0], 4)
PvF = round(rainbow[1], 4)

# Harvey Collier test for linearity
harvey = dg.linear_harvey_collier(resul, order_by=None, skip=None)
HC = round(harvey[0], 4)
PvHC = round(harvey[1], 4)

# Lagrange multiplier test for linearity against functional alternative
residuales = (resul.resid)
Lagrange = dg.linear_lm(residuales, resul.model.exog, func=None)
Lagrange[2]

# # White's Two-Moment Specification Test
whitespec = dg.spec_white(residuales, resul.model.exog)
WE = round(whitespec[0], 4)
PvWE = round(whitespec[1], 4)


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# Extrapolacion oculta

df = pd.read_excel("dataSetA.xlsx")  # Lee excell
datos5 = pd.DataFrame([df.Landa, df.Temp, df.polJP]
                      )  # VARIABLES INDEPENDIENTES
B = datos5.transpose()  # TRASPUESTA QUE DA el DATAFRAME DE LAS VARIABLES INDEPENDIENTES


B_constant = sm.add_constant(B)  # Seria X en la formula de Montgomery
# Seria X' en la formula de Montgomery
B_constantTrans = B_constant.transpose()

A = B_constantTrans
BC = B_constant

D = np.matmul(A, BC)  # Seria X'X
Dinv = np.linalg.inv(D)  # Seria (X'X)^-1


y = datos.polRL  # VARIABLE DEPENDIENTE
linreg = sm.OLS(y, B_constant).fit()
influence = linreg.get_influence()
# Elementos de la diagonal de la matriz sombrero
hatdiag = influence.hat_matrix_diag
hmxm = max(hatdiag)  # hmxm


esp = 3  # Cantidad de niveles de la variable

# Limites superior e inferior por variables
Infland = -5
Supland = 80

Supt = 86
Inft = 32

Supjp = 20
Infjp = 15
# ------------------------


land = np.linspace(Infland, Supland, esp)
temp = np.linspace(Inft, Supt, esp)
jp = np.linspace(Infjp, Supjp, esp)
# ------------------------


P = np.meshgrid(land, temp, jp)

[L, T, JP] = np.meshgrid(land, temp, jp)
c = np.linspace(1, 1, esp)


tt = np.ravel(T)  # Convertir todo en una sola lista
ll = np.ravel(L)
jp = np.ravel(JP)


# cantidad de variables barajadas en P (O sea cantidad de variables independientes)
n = 3
dim = np.size(P)
dimf = dim/n
dimfor = dimf-1
end = int(dimfor)  # convertir de float a int

ho = list()
lands = list()
temps = list()
poljs = list()

for i in range(0, end):
    # Vendria siendo xi' por el dataframe
    xi = pd.DataFrame([1, ll[i], tt[i], jp[i]])
    xit = xi.transpose()
    hy = np.matmul(xit, Dinv)
    hooi = np.matmul(hy, xi)
    hooc = hooi[0][0]

    if hooc > hmxm:
        ho.append(hooi)
        lands.append(ll[i])
        temps.append(tt[i])
        poljs.append(jp[i])

jk = len(ho)

if jk == 0:
    print('No hay evidencias de extrapolación oculta')
else:
    print('Hay evidencias de extrapolación oculta')
    pto = pd.DataFrame([lands, temps, poljs])
    ptos = pto.transpose()
    print(ptos)

# ------------------------------------------------------------------------------
# ------Prueba de bondad de ajuste de Fisher

n = resul.nobs  # (Cantidad de observaciones)
datos8 = pd.DataFrame([df.Landa, df.Temp, df.polJP]
                      )  # TODAS LAS VARIABLES INDEP
datos9 = datos8.transpose()
u = datos9.drop_duplicates()  # Elimina los duplicados del data framae
m = len(u)  # Niveles de x

# TODAS LAS VARIABLES
datos10 = pd.DataFrame([df.polRL, df.Landa, df.Temp, df.polJP])
datos11 = datos10.transpose()


residcua = pow(residuales, 2)  # Valores cuadrados de cada residual
# Suma de cuadrados de los residuales (con y sin replicas)
sumresidcua = sum(residcua)
k = df.Landa-df.Temp-df.polJP
datos14 = pd.DataFrame([k, df.polRL])
datos15 = datos14.transpose()

listaColA = list(k)  # k
listaColB = list(df.polRL)  # observada

cCount = len(listaColA)


storage = []

for i in range(0, cCount):
    if listaColA.count(listaColA[i]) > 1:
        storage.append(listaColA[i])


Storage = pd.DataFrame(storage)

leve = (Storage[0].unique())  # valores clases de k
level = pd.DataFrame(leve)
r = len(level)

SUMATORIA = list()
for i in range(0, r):
    clase = level[0][i]
    fil = datos15.loc[datos15['Unnamed 0'] == clase]
    filtrado = pd.DataFrame(fil)
    observada = filtrado.iloc[:, 1]
    media = np.mean(observada)
    nobs = len(observada)
    ers = list()
    for k in range(0, nobs):
        er = pow((observada-media), 2)
        suma = sum(er)
    SUMATORIA.append(suma)

sumaVecinos = sum(SUMATORIA)


#          sumaVecinos = sumaVecinos+listaColB[i] #SSPE

# print('sumaVecions=',sumaVecinos)

SSlof = sumresidcua-sumaVecinos  # Suma de cuadrados del error por falta de ajuste
SSLAF = round(SSlof, 4)
SSPE = round(sumaVecinos, 4)
Fo = (SSlof/(m-2))/(sumaVecinos/(n-m))  # Valor de la F-Fisher observada
Forr = round(Fo, 4)

a1 = m-2
a2 = n-m
alpha = 0.05

# Valor de la F-Fisher tabulada
Ft = scipy.stats.f.ppf(q=1-alpha, dfn=a1, dfd=a2)
Ftr = round(Ft, 4)

relafisher = Ft/Fo  # Relacion entre la F obs y calculada
Relar = round(relafisher, 4)

# Otras medidas de calidad de ajuste
# PONER RMSE

predicted_value = resul.fittedvalues
rang = max(predicted_value)-min(predicted_value)

p = len(resul.params)-1  # No de parametros del modelo sin contar el intercepto


espg = np.sqrt(p*sumaVecinos/n)
espgr = round(espg, 4)

rel = rang/espg
relr = round(rel, 4)
###############################################################################

# Validacion Cruzada

# TODAS LAS VARIABLES DEL MODELO
datos2 = pd.DataFrame([df.polRL, df.Landa, df.Temp, df.polJP])
datos3 = datos2.transpose()  # Trasouesta


y = datos3.polRL  # VARIABLE DEPENDIENTE

x = pd.DataFrame([df.Landa, df.Temp, df.polJP])  # VARIABLES INDEPENDIENTES

X = x.transpose()
clf = LinearRegression()
model = clf.fit(X, y)  # Regresion x esta libreria

# INFORMACION QUE SE ESPECIFICA*******SON LOS FOLDS (tiene que ser mayor que 2)
k = 5


scores = cross_validate(model, X, y, cv=k, scoring=(
    'r2', 'neg_mean_squared_error'), return_train_score=True)
a = scores['test_neg_mean_squared_error']
b = scores['train_neg_mean_squared_error']
c = scores['test_r2']
d = scores['train_r2']

predictions = cross_val_predict(clf, X, y, cv=k)

e = metrics.r2_score(y, predictions)

f = metrics.mean_squared_error(y, predictions)

g = np.sqrt(f)


plt.scatter(predictions, y)  # Predichos por k-Folds vs observados
# Valores predichos por el modelo completo
plt.scatter(predicted_value, predictions)
# predicciones por k-folds
# PONER LUEGO LOS RESUMENES
amenan = np.mean(a)  # MEDIA
bmenan = np.mean(b)
cmenan = np.mean(c)
dmenan = np.mean(d)


def cvar(x): return np. std(x, ddof=1) / np. mean(x) * 100


acv = cvar(a)  # CV
bcv = cvar(b)
ccv = cvar(c)
dcv = cvar(d)


###############################################################################
# let's select the number of bootstraps we want

# TODAS LAS VARIABLES DEL MODELO
Datosboot1 = pd.DataFrame([df.Landa, df.Temp, df.polJP, df.polRL])
# LE HAGO LA TRASPUESTA Y ESA ES LA QUE SE COJE PA EL GRAFICO QUE CORRESPONDE A LA SECCION
data_df = Datosboot1.transpose()
boots = 6

boot_coeff = []
boot_rcuadj = []
boot_RMSE = []
coeffs = []

k = len(data_df.polRL)
for _ in range(boots):
    # sample the rows, same size, with replacement
    sample_df = data_df.sample(n=k, replace=True)
    regbst = smf.ols('polRL~Landa+Temp+polJP', sample_df)
    resulbst = regbst.fit()
    coeffbst = resulbst.params
    rcuadjbst = resulbst.rsquared_adj
    RMSEbst = np.sqrt(resulbst.mse_total)

    # append coefficients

    boot_rcuadj.append(rcuadjbst)
    boot_RMSE.append(RMSEbst)
    boot_coeff.append(coeffbst)

RMSEbtmean = np.mean(boot_RMSE)
Rcuadjbtmean = np.mean(boot_rcuadj)


def cvar(x): return np. std(x, ddof=1) / np. mean(x) * 100


RMSEcv = cvar(boot_RMSE)
Rcuacv = cvar(boot_rcuadj)
# ----------------------------------------------------------------------------------
# Para extraer cada coeficente en cada caso se modifica el valor de su índice
InterCoeffbts = []
ab = boots-1
for i in range(0, ab):
    InterCoeffbts.append(boot_coeff[i][0])

Intbtsmean = np.mean(InterCoeffbts)
IntbtsCv = cvar(InterCoeffbts)


###########################################333333333###########################
