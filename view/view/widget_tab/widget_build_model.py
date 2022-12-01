from PyQt5.QtWidgets import (
    QAbstractItemView, QGridLayout,QHBoxLayout, QVBoxLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem, QDoubleSpinBox, QListView,
    QPushButton
)

from PyQt5.QtGui import (
    QFont, 
)

from PyQt5.QtCore import(
    QSize
)

from PyQt5 import QtCore, QtGui, QtWidgets

from view.view.widget_tab.widget_tab import WidgetTab

from view.model.variable_independt_model import VariableIndependtModel
from view.model.modelLMR_model import ModelLMRModel

from view.components.list_view import ListViewCheckBox,ListViewRadioButton
from view.components import message_box as MB

from controller.analysis_data import AnalysisData

from model.modelLMR import ModelLMR
import uuid 

class WidgetBuildModel(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUi()
        self.createWorkspace()
        self.createConnect()
        
    def createUi(self):
        self.horizontalLayout_5 = QHBoxLayout(self.widgetCentral)
        
        self.groupBox = QGroupBox(self.widgetCentral)
        
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        
        self.verticalLayout_8 = QVBoxLayout()
        
        self.verticalLayout_6 = QVBoxLayout()
        
        self.label_5 = QLabel(self.groupBox)        
        self.verticalLayout_6.addWidget(self.label_5)

        self.listViewCandidateVD = ListViewRadioButton(self.groupBox)
              
        self.verticalLayout_6.addWidget(self.listViewCandidateVD)    
        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.label_6 = QLabel(self.groupBox)
        
        self.verticalLayout_7.addWidget(self.label_6)
        self.listViewCandidateVI = ListViewCheckBox(self.groupBox)
        self.verticalLayout_7.addWidget(self.listViewCandidateVI)

        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.label_7 = QLabel(self.groupBox)
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setKerning(True)
        self.label_7.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_7)


        self.gridLayout.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_2 = QVBoxLayout()
        self.label = QLabel(self.groupBox)

        self.verticalLayout_2.addWidget(self.label)

        self.lineEditNameModel = QLineEdit(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditNameModel.sizePolicy().hasHeightForWidth())
        self.lineEditNameModel.setSizePolicy(sizePolicy)
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.lineEditNameModel)


        self.verticalLayout_11.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setText("Intervalo de confianza")
        self.verticalLayout_5.addWidget(self.label_8)

        self.doubleSBIntervalConfidence = QDoubleSpinBox(self.groupBox)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.doubleSBIntervalConfidence.sizePolicy().hasHeightForWidth())
        self.doubleSBIntervalConfidence.setSizePolicy(sizePolicy1)
        self.doubleSBIntervalConfidence.setMaximum(1.000000000000000)
        self.doubleSBIntervalConfidence.setSingleStep(0.010000000000000)
        self.doubleSBIntervalConfidence.setValue(0.050000000000000)

        self.verticalLayout_5.addWidget(self.doubleSBIntervalConfidence)


        self.verticalLayout_11.addLayout(self.verticalLayout_5)

        self.verticalSpacer_4 = QSpacerItem(118, 13, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.label_3 = QLabel(self.groupBox)

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEditVariableDependent = QLineEdit(self.groupBox)
        sizePolicy.setHeightForWidth(self.lineEditVariableDependent.sizePolicy().hasHeightForWidth())
        self.lineEditVariableDependent.setSizePolicy(sizePolicy)
        self.lineEditVariableDependent.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.lineEditVariableDependent)


        self.verticalLayout_11.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(118, 13, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.label_4 = QLabel(self.groupBox)

        self.verticalLayout_4.addWidget(self.label_4)

        self.listViewVariablesIndepent = QListView(self.groupBox)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listViewVariablesIndepent.sizePolicy().hasHeightForWidth())
        self.listViewVariablesIndepent.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.listViewVariablesIndepent)


        self.verticalLayout_11.addLayout(self.verticalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalSpacer_3 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pBAddModel = QPushButton(self.groupBox)
        self.horizontalLayout_3.addWidget(self.pBAddModel)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_11, 0, 1, 1, 1)


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout = QVBoxLayout()
        self.label_2 = QLabel(self.widgetCentral)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2)

        self.listViewModel = QListView(self.widgetCentral)
        self.listViewModel.setMinimumSize(QSize(0, 350))

        self.verticalLayout.addWidget(self.listViewModel)


        self.verticalLayout_9.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.pBEditModel = QPushButton(self.widgetCentral)

        self.horizontalLayout.addWidget(self.pBEditModel)

        self.pBDetailsModel = QPushButton(self.widgetCentral)

        self.horizontalLayout.addWidget(self.pBDetailsModel)

        self.pBRemoveModel = QPushButton(self.widgetCentral)
        self.horizontalLayout.addWidget(self.pBRemoveModel)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(self.verticalSpacer)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        ##############################################################
        self.modelVariablesIndepent = VariableIndependtModel()
        self.listViewVariablesIndepent.setModel(self.modelVariablesIndepent)
        self.listViewModel.setMinimumSize(QtCore.QSize(0, 350))
        self.listViewModel.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listViewModel.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        
        self.modelModelLMR = ModelLMRModel()
        self.listViewModel.setModel(self.modelModelLMR)
        self.groupBox.setTitle("Conformación del modelo")
        self.label_5.setText("Posibles variables  dependientes")
        self.label_6.setText("Posibles variables  independientes")
        self.label_7.setText("El orden en que se selecciona las \n"
                             "variables independientes del modelo\n"
                             "influye de forma significativa en este.")
        self.label.setText("Nombre del modelo")
        self.label_3.setText("Variable dependiente")
        self.label_3.setSizePolicy(sizePolicy)
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setText("Variables independientes")
        self.pBAddModel.setText("Registrar modelo")
        self.label_2.setText( "Modelos definidos")
        self.pBEditModel.setText("Editar")
        self.pBDetailsModel.setText("Detalles")
        self.pBRemoveModel.setText( "Eliminar")
        self.label_7.setVisible(False)
        self.pushButtonNext.setText("Siguiente paso")
        
        if self.modelModelLMR.rowCount() == 0:
            self.pushButtonNext.setEnabled(False)
        
    def createWorkspace(self):
        self.modelCandidateVD = QtGui.QStandardItemModel(self.listViewCandidateVD)
        self.modelCandidateVI = QtGui.QStandardItemModel(self.listViewCandidateVI)
        variablesSelect = AnalysisData().getVariablesSelect()
        for line in variablesSelect:
            itemVD = QtGui.QStandardItem(line)
            itemVI = QtGui.QStandardItem(line)
            itemVD.setCheckable(True)
            itemVI.setCheckable(True)
            itemVD.setCheckState(QtCore.Qt.Unchecked)
            itemVI.setCheckState(QtCore.Qt.Unchecked)
            self.modelCandidateVD.appendRow(itemVD)
            self.modelCandidateVI.appendRow(itemVI)

        self.listViewCandidateVD.setModel(self.modelCandidateVD)
        self.listViewCandidateVI.setModel(self.modelCandidateVI)
    
    def createConnect(self):
        super().createConnect()
        self.pBAddModel.clicked.connect(self.clickPBAddModel)
        self.pBEditModel.clicked.connect(self.clickPBEditModel)
        self.pBDetailsModel.clicked.connect(self.clickPBDetails)
        self.pBRemoveModel.clicked.connect(self.clickPBRemoveModel)
        self.listViewCandidateVD.radioButton.connect(self.addVariableD)
        self.listViewCandidateVI.checked.connect(self.selectVariableI)
             
    def validModel(self,_nameModel,_nameVD,_namesVI):
        isModelOK = True
        error = ""
        
        if len(_nameModel) == 0:
            isModelOK = False
            error = "- El nombre del modelo no puede ser vacio.\n"
            
        if len(_nameVD) == 0:
            isModelOK = False 
            error = error+"- El modelo debe tener una variable dependiente\n"
            
        if len(_namesVI) == 0:
            isModelOK = False
            error = error+"- El modelo debe tener al menos una variable independiente\n"
            
        if _nameVD in _namesVI:
            isModelOK = False
            error = error +"- La variable dependiente no puede formar parte de las variables independientes del modelo\n"
            
        modelTes =ModelLMR('test',_nameModel,_nameVD,_namesVI)
        
        if self.modelModelLMR.existThisModel(modelTes) == True:
            isModelOK = False
            error = error +"- El modelo conformado quiza su nombre no sea igual pero su estructura (Variable Dependiente y las Variables Inpendientes en su orden) es identica a otro ya definido\n"    
            
        return [isModelOK,error]          
    
    def clickPBAddModel(self):
        nameModel = self.lineEditNameModel.text().strip()
        nameVariableD = self.lineEditVariableDependent.text().strip()
        intervalConfidence = self.doubleSBIntervalConfidence.value()
        namesVariableI = self.modelVariablesIndepent.getElements()
        
        [isModelOK ,error] =self.validModel(nameModel,nameVariableD,namesVariableI)        
        
        if isModelOK == True:
            uidModel = str( uuid.uuid4())
            model = ModelLMR(uidModel,nameModel,nameVariableD,namesVariableI,intervalConfidence)
            self.modelModelLMR.addElement(model)
            self.clearForm()
            self.enableButtoNext()
        else:
            messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_CRITICAL,
                                                       "Error",
                                                       "La conformación del modelo presenta problemas.",error)
            messageBox.exec()
    
    def clickPBEditModel(self):
        indexes = self.listViewModel.selectedIndexes()
        if len(indexes) == 1:
            index=indexes[0]
            model = self.modelModelLMR.getThisModel(index)
            self.updateFormRegister(model)
            self.modelModelLMR.revomeElement(index)
            self.listViewModel.clearSelection()
            self.enableButtoNext()
        else:
            messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_WARNING,
                                                       "Advertencia",
                                                       "Seleccione el modelo que desea eliminar.")
            messageBox.exec()
    
    def clickPBRemoveModel(self):
        indexes = self.listViewModel.selectedIndexes()
        if len(indexes)==1:
            index=indexes[0]
            self.modelModelLMR.revomeElement(index)
            self.listViewModel.clearSelection()
            self.enableButtoNext()
        else:
            messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_WARNING,
                                                       "Advertencia",
                                                       "Seleccione el modelo que desea eliminar.")
            messageBox.exec() 
    
    def clickPBDetails(self):
        indexes = self.listViewModel.selectedIndexes()
        messageBox = None
        if len(indexes)==1:
            index=indexes[0]
            model = self.modelModelLMR.getThisModel(index)
            if model != None:
                messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_INFORMATION,
                                                       "Información - Detalles del modelo",
                                                       model.detailsModelForMessageBox())
            else:
                messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_CRITICAL,
                                                       "Error",
                                                       "No se encontró el modelo para mostrar sus detalles")
            self.listViewModel.clearSelection()
        else:
            messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_WARNING,
                                                       "Advertencia",
                                                       "Seleccione el modelo que desea ver los detalles.")
        if messageBox !=None:
            messageBox.exec()
    
    def enableButtoNext(self):
        if self.modelModelLMR.rowCount() >=1:
            self.pushButtonNext.setEnabled(True)
        else:
            self.pushButtonNext.setEnabled(False)
    
    def clearForm(self):
        self.lineEditNameModel.clear()
        self.lineEditVariableDependent.clear()
        self.modelVariablesIndepent.clear()
        self.listViewVariablesIndepent.setModel(self.modelVariablesIndepent)
        self.listViewVariablesIndepent.repaint()
        
        rowsVCI = self.modelCandidateVI.rowCount()
        for i in range(0,rowsVCI):
            index = self.modelCandidateVI.index(i,0)
            self.modelCandidateVI.setData(index,False,QtCore.Qt.CheckStateRole)
            
        rowsVCD = self.modelCandidateVD.rowCount()
        for i in range(0,rowsVCD):
            index = self.modelCandidateVD.index(i,0)
            self.modelCandidateVD.setData(index,False,QtCore.Qt.CheckStateRole)
            
        self.doubleSBIntervalConfidence.setValue(0.05)
    
    def addVariableD(self,_index):
        nameVariable = _index.data(QtCore.Qt.ItemDataRole.DisplayRole)
        self.lineEditVariableDependent.setText(nameVariable)
    
    def selectVariableI(self,_index):
        if _index.data(QtCore.Qt.ItemDataRole.CheckStateRole) == QtCore.Qt.Checked:
            self.addVariableI(_index)
        elif _index.data(QtCore.Qt.ItemDataRole.CheckStateRole) == QtCore.Qt.Unchecked:
            self.removeVariableI(_index)
    
    def removeVariableI(self,_index):
        nameVariable = _index.data(QtCore.Qt.ItemDataRole.DisplayRole)
        self.modelVariablesIndepent.revomeElement(nameVariable)
    
    def addVariableI(self,_index):
        nameVariable = _index.data(QtCore.Qt.ItemDataRole.DisplayRole)
        self.modelVariablesIndepent.addElement(nameVariable)
        
    def clickNextStage(self):
        tModelCreate = self.modelModelLMR.getElements()
        for k,v in tModelCreate.items():
            AnalysisData().addModel(v)
        self.modelModelLMR.clear()
        self.modelModelLMR.clearElements()  
        super().clickNextStage()
        
        
        
    def updateFormRegister(self,_model):
        self.lineEditNameModel.setText(_model.getNameModel())
        self.lineEditVariableDependent.setText(_model.getNameVariableD())
        self.doubleSBIntervalConfidence.setValue(_model.getIntervalConfidence())
        
        self.modelVariablesIndepent.clear()
        for var in _model.getNamesVariableI():
            self.modelVariablesIndepent.addElement(var)
            
        rowsVCI = self.modelCandidateVI.rowCount()
        for i in range(0,rowsVCI):
            index = self.modelCandidateVI.index(i,0)
            if self.modelCandidateVI.data(index,QtCore.Qt.DisplayRole) in _model.getNamesVariableI():
                self.modelCandidateVI.setData(index,QtCore.Qt.Checked,QtCore.Qt.CheckStateRole)
            else:
                self.modelCandidateVI.setData(index,QtCore.Qt.Unchecked,QtCore.Qt.CheckStateRole)
        
        rowsVCD = self.modelCandidateVD.rowCount()
        for i in range(0,rowsVCD):
            index = self.modelCandidateVD.index(i,0)
            if self.modelCandidateVD.data(index,QtCore.Qt.DisplayRole) == _model.getNameVariableD():
                self.modelCandidateVD.setData(index,QtCore.Qt.Checked,QtCore.Qt.CheckStateRole)
            else:
                self.modelCandidateVD.setData(index,QtCore.Qt.Unchecked,QtCore.Qt.CheckStateRole)
                
        
    
    def updateTab(self):
        self.modelCandidateVD = QtGui.QStandardItemModel(self.listViewCandidateVD)
        self.modelCandidateVI = QtGui.QStandardItemModel(self.listViewCandidateVI)
        variablesSelect = AnalysisData().getVariablesSelect()
        for line in variablesSelect:
            itemVD = QtGui.QStandardItem(line)
            itemVI = QtGui.QStandardItem(line)
            itemVD.setCheckable(True)
            itemVI.setCheckable(True)
            itemVD.setCheckState(QtCore.Qt.Unchecked)
            itemVI.setCheckState(QtCore.Qt.Unchecked)
            self.modelCandidateVD.appendRow(itemVD)
            self.modelCandidateVI.appendRow(itemVI)

        self.listViewCandidateVD.setModel(self.modelCandidateVD)
        self.listViewCandidateVI.setModel(self.modelCandidateVI)
        
        
        
        
    