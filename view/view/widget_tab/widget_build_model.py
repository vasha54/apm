from PyQt5.QtWidgets import (
    QAbstractItemView
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
        self.createWorkspace()
        self.createConnect()
        
    def setupUi(self, WidgetDataBuildModel):
        
        WidgetDataBuildModel.setObjectName("WidgetDataBuildModel")
        WidgetDataBuildModel.resize(881, 471)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(WidgetDataBuildModel)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(WidgetDataBuildModel)
        
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        
        self.listViewCandidateVD = ListViewRadioButton(self.groupBox)
        self.listViewCandidateVD.setObjectName("listViewCandidateVD")
        self.verticalLayout_6.addWidget(self.listViewCandidateVD)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        
        self.listViewCandidateVI = ListViewCheckBox(self.groupBox)
        self.listViewCandidateVI.setObjectName("listViewCandidateVI")
        self.verticalLayout_7.addWidget(self.listViewCandidateVI)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        
        self.lineEditNameModel = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditNameModel.setObjectName("lineEditNameModel")
        self.verticalLayout_2.addWidget(self.lineEditNameModel)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        
        self.lineEditVariableDependent = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditVariableDependent.setReadOnly(True)
        self.lineEditVariableDependent.setObjectName("lineEditVariableDependent")
        self.verticalLayout_3.addWidget(self.lineEditVariableDependent)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        
        self.listViewVariablesIndepent = QtWidgets.QListView(self.groupBox)
        self.listViewVariablesIndepent.setObjectName("listViewVariablesIndepent")
        self.verticalLayout_4.addWidget(self.listViewVariablesIndepent)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        
        self.modelVariablesIndepent = VariableIndependtModel()
        self.listViewVariablesIndepent.setModel(self.modelVariablesIndepent)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        spacerItem2 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        
        self.pBAddModel = QtWidgets.QPushButton(self.groupBox)
        self.pBAddModel.setObjectName("pBAddModel")
        self.horizontalLayout_3.addWidget(self.pBAddModel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addWidget(self.groupBox)
        
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label_2 = QtWidgets.QLabel(WidgetDataBuildModel)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        
        self.listViewModel = QtWidgets.QListView(WidgetDataBuildModel)
        self.listViewModel.setMinimumSize(QtCore.QSize(0, 350))
        self.listViewModel.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listViewModel.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.verticalLayout.addWidget(self.listViewModel)
        self.verticalLayout_9.addLayout(self.verticalLayout)
        
        self.modelModelLMR = ModelLMRModel()
        self.listViewModel.setModel(self.modelModelLMR)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.pBEditModel = QtWidgets.QPushButton(WidgetDataBuildModel)
        self.pBEditModel.setObjectName("pBEditModel")
        self.horizontalLayout.addWidget(self.pBEditModel)
        self.pBDetailsModel = QtWidgets.QPushButton(WidgetDataBuildModel)
        self.pBDetailsModel.setObjectName("pBRemoveModel_2")
        self.horizontalLayout.addWidget(self.pBDetailsModel)
        
        self.pBRemoveModel = QtWidgets.QPushButton(WidgetDataBuildModel)
        self.pBRemoveModel.setObjectName("pBRemoveModel")
        self.horizontalLayout.addWidget(self.pBRemoveModel)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        spacerItem4 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        
        self.pushButtonNext = QtWidgets.QPushButton(WidgetDataBuildModel)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_2.addWidget(self.pushButtonNext)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        
        self.groupBox.setTitle("Conformación del modelo")
        self.label_5.setText("Posibles variables  dependientes")
        self.label_6.setText("Posibles variables  independientes")
        self.label_7.setText("El orden en que se selecciona las \n"
                             "variables independientes del modelo\n"
                             "influye de forma significativa en este.")
        self.label.setText("Nombre del modelo")
        self.label_3.setText("Variable dependiente")
        self.label_4.setText("Variables independientes")
        self.pBAddModel.setText("Registrar modelo")
        self.label_2.setText( "Modelos definidos")
        self.pBEditModel.setText("Editar")
        self.pBDetailsModel.setText("Detalles")
        self.pBRemoveModel.setText( "Eliminar")
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
        self.pushButtonNext.clicked.connect(self.clickNextStage)
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
            error = error +"- La variable dependiente no puede formar parte de las variables independientes del modelo"
            
        return [isModelOK,error]          
    
    def clickPBAddModel(self):
        nameModel = self.lineEditNameModel.text().strip()
        nameVariableD = self.lineEditVariableDependent.text().strip()
        namesVariableI = self.modelVariablesIndepent.getElements()
        
        [isModelOK ,error] =self.validModel(nameModel,nameVariableD,namesVariableI)        
        
        if isModelOK == True:
            uidModel = str( uuid.uuid4())
            model = ModelLMR(uidModel,nameModel,nameVariableD,namesVariableI)
            self.modelModelLMR.addElement(model)
            self.clearForm()
            self.enableButtoNext()
        else:
            messageBox=MB.showGenericMessage(self.parent(),MB.MESSAG_CRITICAL,
                                                       "Error",
                                                       "La conformación del modelo presenta problemas.",error)
            messageBox.exec()
    
    def clickPBEditModel(self):
        pass
    
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
        print('Hijo')
        super().clickNextStage()
    
    def update(self):
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
        
        
    