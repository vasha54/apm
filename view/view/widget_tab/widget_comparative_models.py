from PyQt5.QtWidgets import (
    QWidget, QGridLayout, QVBoxLayout, QLayout, QLabel, QSizePolicy, QTableView,
    QSpacerItem, QGroupBox, QHBoxLayout
)

from PyQt5.QtWidgets import (
    QWidget,QHeaderView
)

from PyQt5.QtCore import (
    QSize
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
        # self.polar = QPolarChart()
        # chartView = QChartView(self.polar)
        
        # axisy = QValueAxis()
        # axisx = QValueAxis()
        
        # axisy.setRange(0,500)
        # axisy.setTickCount(4)
        # self.polar.setAxisY(axisy)
        # axisx.setRange(0,360)
        # axisx.setTickCount(5)
        # self.polar.setAxisX(axisx)
        
        # #Let's draw scatter series
        # self.polar_series = QScatterSeries()
        # self.polar_series.setMarkerSize(5.0)        
        
        # self.polar_series.append(0, 0)
        # self.polar_series.append(360, 500) 
        # #Why not draw archimedes spiral
        # for i in range(0,360,10): 
        #     self.polar_series.append(i, i)
        # self.polar.addSeries(self.polar_series)
        
        # self.clearLayout(self.vLayoutChartComparative)
        
        plot = pg.plot()
        plot.setAspectLocked()
        
        # Add polar grid lines
        plot.addLine(x=0, pen=0.2)
        plot.addLine(y=0, pen=0.2)
        
        for r in range(2, 20, 2):
            circle = QGraphicsEllipseItem(-r, -r, r * 2, r * 2)
            circle.setPen(pg.mkPen(0.2))
            plot.addItem(circle)
        
        # make polar data
        theta = np.linspace(0, 2 * np.pi, 100)
        radius = np.random.normal(loc=10, size=100)
        
        # Transform to cartesian and plot
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        #plot.plot(x, y)
        
        self.vLayoutChartComparative.addWidget(plot.plot(x, y))
    
   