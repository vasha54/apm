from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QVBoxLayout, QLayout, QLabel, QSizePolicy, QTableView,
    QSpacerItem, QGroupBox, QHBoxLayout
)

from PyQt5.QtWidgets import (
    QWidget,QHeaderView, QGraphicsEllipseItem
)

from PyQt5.QtCore import (
    QSize
)

from PyQt5.QtGui import(
    QBrush, QColor, QPainter
)


from PyQt5.QtChart import QPolarChart, QChartView, QValueAxis, QScatterSeries

from view.view.widget_tab.widget_tab import WidgetTab

from controller.analysis_data import AnalysisData

from view.components.widget_validation_boot_stropping import  WidgetValidationBootStropping
from view.components.widget_validation_kold import WidgetValidationKold
from view.components.list_view import ListViewCheckBox

from view.preferences.preferences import PreferenceGUI

from view.model.comparative_models_model import ComparativeModelsModel

from view.components import message_box as MB

import pyqtgraph as pg
import math

from model.modelLMR import ModelLMR

from PyQt5 import QtCore, QtGui, QtWidgets
class WidgetComparativeModel(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        self.createConnect() 
        PreferenceGUI.instance().subscribe(self)     
    
    def createUI(self):
        self.gridLayout = QtWidgets.QGridLayout(self.widgetCentral)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.verticalLayout.addWidget(self.label)
        self.listViewModel = ListViewCheckBox(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewModel.sizePolicy().hasHeightForWidth())
        self.listViewModel.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.listViewModel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        spacerItem = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pBCompare = QtWidgets.QPushButton(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBCompare.sizePolicy().hasHeightForWidth())
        self.pBCompare.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.pBCompare)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(488, 5, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.widgetChartComparative = QtWidgets.QWidget(self.widgetCentral)
        self.widgetChartComparative.setStyleSheet("")
        self.vLayoutChartComparative = QtWidgets.QVBoxLayout(self.widgetChartComparative)
        self.gridLayout.addWidget(self.widgetChartComparative, 1, 1, 1, 1)
        self.tableViewModelCom = QtWidgets.QTableView(self.widgetCentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewModelCom.sizePolicy().hasHeightForWidth())
        self.tableViewModelCom.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.tableViewModelCom, 2, 0, 1, 2)
        self.label.setText("Modelos:")
        self.pBCompare.setText("Comparar")
        
        self.tableViewModelCom.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableViewModelCom.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableViewModelCom.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableViewModelCom.verticalHeader().hide()
        
        
    def createWorkspace(self):
        self.tableViewModelCom.setVisible(False)
        self.widgetChartComparative.setVisible(False)
        self.pushButtonNext.setVisible(False)
        self.loadModels()
    
    def createConnect(self):
        self.pBCompare.clicked.connect(self.compareModels)
        self.listViewModel.checked.connect(self.selectModel)
        
    def updateTab(self):
        pass
    
    def compareModels(self):
        keysModelComparative = AnalysisData().getKeyModelCompare()
        
        if len(keysModelComparative) > 0:
            self.modelsComparativeModel = ComparativeModelsModel(keysModelComparative)
            self.tableViewModelCom.setModel(self.modelsComparativeModel)
            self.createChartSpider();
            self.tableViewModelCom.setVisible(True)
            self.widgetChartComparative.setVisible(True)
        else:
            self.tableViewModelCom.setVisible(False)
            self.widgetChartComparative.setVisible(False)
            messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_CRITICAL,
                                                       "Error",
                                                       "Tiene que existir modelos seleccionados para establecer la comparación.")
            messageBox.exec()
        
    def loadModels(self):
        self.modelCandidateModel = QtGui.QStandardItemModel(self.listViewModel)
        
        models = AnalysisData().getKeyNameModels()
        
        for model in models:
            itemModel = QtGui.QStandardItem(model['name'])
            itemModel.setCheckable(True)
            itemModel.setData(model['key'], QtCore.Qt.ItemDataRole.UserRole)
            itemModel.setCheckState(QtCore.Qt.Unchecked)
            self.modelCandidateModel.appendRow(itemModel)
            
        self.listViewModel.setModel(self.modelCandidateModel)
        
    def selectModel(self,_index):
        if _index.data(QtCore.Qt.ItemDataRole.CheckStateRole) == QtCore.Qt.Checked:
            self.addModel(_index)
        elif _index.data(QtCore.Qt.ItemDataRole.CheckStateRole) == QtCore.Qt.Unchecked:
            self.removeModel(_index)
    
    def removeModel(self,_index):
        keyModel = _index.data(QtCore.Qt.ItemDataRole.UserRole)
        AnalysisData().removeKeyModelCompare(keyModel)
    
    def addModel(self,_index):
        keyModel = _index.data(QtCore.Qt.ItemDataRole.UserRole)
        AnalysisData().addKeyModelCompare(keyModel)
        
    def changePreference(self,_listChange):
        pass
    
    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())
    
    def createChartSpider(self):
        
        self.clearLayout(self.vLayoutChartComparative)
        
        keysModelComparative = AnalysisData().getKeyModelCompare()
        
        countModels =len(keysModelComparative)
        
        indicators = ['R-cuadrado', 'R-cuadrado adjustado','AIC', 'BIC', 'RSME', 'Log-likehead']
        indicatorsKEY = [ModelLMR.RCUAD, ModelLMR.RCUAD_ADJUST, ModelLMR.AIC, ModelLMR.BIC, ModelLMR.RMSE_MODEL, ModelLMR.LOG_LIKELI_HEAD]
        
        countIndicators = len(indicators)
        angleRotation = (2.00*math.pi)/countIndicators
        
        xLineSpider=[0 for item in range(0, countModels+1)]
        yLineSpider=[item for item in range(0, countModels+1)]
        
        xLineSpider.append(0)
        yLineSpider.append(yLineSpider[-1]+0.075)
        
        colorText = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_TEXT_CHART)
        colorBackground = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_BACKGROUND_CHART)
        colorAxes = PreferenceGUI.instance().getValueSettings(PreferenceGUI.COLOR_AXES_CHART)
        
        pg.setConfigOption('foreground', colorAxes)
        pg.setConfigOption('background', colorBackground)
        pg.setConfigOptions(antialias=True)
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setRenderHints(QPainter.Antialiasing)
        self.graphWidget.getPlotItem().hideAxis('bottom')
        self.graphWidget.getPlotItem().hideAxis('left')
        self.graphWidget.setMaximumWidth(self.listViewModel.geometry().height())
        self.graphWidget.setMaximumHeight(self.listViewModel.geometry().height())
        
        penLine = pg.mkPen(color=colorAxes, width=1)
        brushLine = QBrush(QColor(colorAxes))
        
        angle = 0
        
        linesPolygonXs ={}
        linesPolygonYs ={}
        
        for i in range(0,countIndicators):
            xLineSpiderRotate = []
            yLineSpiderRotate = []
            
            for j in range(0,len(xLineSpider)-1):
                
                if j != 0 and j not in linesPolygonXs.keys():
                    linesPolygonXs[j] = list()
                    linesPolygonYs[j] = list()
                
                xRotate = xLineSpider[j]*math.cos(angle)-yLineSpider[j]*math.sin(angle)
                yRotate = yLineSpider[j]*math.cos(angle)+xLineSpider[j]*math.sin(angle)
                xLineSpiderRotate.append(xRotate)
                yLineSpiderRotate.append(yRotate)
                
                if j != 0:
                    linesPolygonXs[j].append(xRotate)
                    linesPolygonYs[j].append(yRotate)
            
            self.graphWidget.plot(xLineSpiderRotate, yLineSpiderRotate,pen=penLine ,symbol='o', symbolSize=3, symbolBrush=brushLine)
            
            
            
            xText = xLineSpider[-1]*math.cos(angle)-yLineSpider[-1]*math.sin(angle)
            yText = yLineSpider[-1]*math.cos(angle)+xLineSpider[-1]*math.sin(angle)
            
            labelIndicators = pg.TextItem(text=indicators[i], color=colorAxes, anchor=(0, 1))
            labelIndicators.setPos(xText,yText)
            self.graphWidget.addItem(labelIndicators, ignoreBounds=True)
            
            angle=angleRotation+angle
        
          
        for k in linesPolygonYs.keys():
            linesPolygonXs[k].append(linesPolygonXs[k][0])
            linesPolygonYs[k].append(linesPolygonYs[k][0])
            self.graphWidget.plot(linesPolygonXs[k], linesPolygonYs[k],pen=penLine ,symbol='o', symbolSize=3, symbolBrush=brushLine)
            
        
        self.vLayoutChartComparative.addWidget(self.graphWidget)
    
   