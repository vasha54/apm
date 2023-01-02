from PyQt5.QtWidgets import (
    QWidget,QHeaderView
)

from PyQt5 import QtCore, QtWidgets

from view.model.modelVIFAnalysMultiColinualidad_model import ModelVIFAnalysMultiColinualidadModel
from view.ui.widget_analys_multi_colinualidad_ui import Ui_WidgetAnalysMultiColinualidad

from  controller.analysis_data import AnalysisData
from view.preferences.preferences import PreferenceGUI

class WidgetAnalysMultiColinualidad(QWidget,Ui_WidgetAnalysMultiColinualidad):
    def __init__(self,_keyModel,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.relationsPosWidgetKeyModel={}
        self.setupUi(self)
        self.keyModel = _keyModel
        self.createWorkSpace()
        self.preference = PreferenceGUI.instance().subscribe(self)
        
    def createWorkSpace(self):
        self.model = ModelVIFAnalysMultiColinualidadModel(self.keyModel)
        self.tableViewMultiColinealidad.setModel(self.model)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewMultiColinealidad.sizePolicy().hasHeightForWidth())
        
        self.tableViewMultiColinealidad.setSizePolicy(sizePolicy)
        self.tableViewMultiColinealidad.setMinimumSize(QtCore.QSize(0, 0))
        self.tableViewMultiColinealidad.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableViewMultiColinealidad.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableViewMultiColinealidad.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        
    def update(self):
        self.keyModel = AnalysisData().getKeyModelSelect()
        self.createWorkSpace()
        
    def changePreference(self,_listChange):
        if  PreferenceGUI.DECIMAL_PLACES in _listChange:
            self.update()