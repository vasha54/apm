from PyQt5.QtWidgets import (
    QApplication, QFileDialog, QMainWindow, QMessageBox, QFrame, 
    QHBoxLayout,QAction, QLabel,QWidget, QSizePolicy,QToolButton,
    QToolBar,QTabWidget,
)

from PyQt5.QtGui import(
    QPixmap,QIcon
)

from PyQt5.QtCore import QSize,QDir

from PyQt5.uic import loadUi
from PyQt5 import QtCore
from view.ui.mainwindow_ui import Ui_MainWindow
from controller.analysis_data import AnalysisData
from view.view.status_bar import StatusBar
from view.preferences.preferences import PreferenceGUI

from view.view.widget_tab.widget_data_filter import WidgetDataFilter
from view.view.widget_tab.widget_charts_variables import WidgetChartVariables
from view.view.widget_tab.widget_build_model import WidgetBuildModel
from view.view.widget_tab.widget_analys_models import WidgetAnalysModels
from view.view.widget_tab.widget_details_model_select import WidgetDetailsModelSelect
from view.view.widget_tab.widget_information_extrapolacion import WidgetInformationExtrapolacion
from view.view.widget_tab.widget_quality_adjust_model import WidgetQualityAdjustModel
from view.view.widget_tab.widget_validate import WidgetValidate
from view.view.widget_tab.widget_tab import WidgetTab
from view.ui.presentation_ui import Ui_WidgetPresentacion
from view.dialog.dialog_preference import DialogPreference

from view.resource import resource


class App(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.createWorkSpace()
        self.analysisData = AnalysisData()
        self.preference = PreferenceGUI.instance().subscribe(self)

    def createWorkSpace(self):
        self.createMenuBar()
        self.createToolsBars()
        self.createCentralWidget()
        self.createStatusBar()
        self.createConnects()
        self.createTabWidget()
        
        
    def createTabWidget(self):
        self.widgetDataFilter = WidgetDataFilter(self)
        self.widgetChartsVariables = WidgetChartVariables(self)
        self.widgetBuildModel = WidgetBuildModel(self)
        self.widgetAnalysModels= WidgetAnalysModels(self)
        self.widgetDetailsModelSelect = WidgetDetailsModelSelect(self)
        self.widgetInformationExtrapolacion = WidgetInformationExtrapolacion(self)
        self.widgetQualityAdjustModel = WidgetQualityAdjustModel(self)
        self.widgetValidate = WidgetValidate(self)
        
        self.widgetDataFilter.next.connect(self.addOrUpdateTabChartVariables)
        self.widgetChartsVariables.next.connect(self.addOrUpdateTabBuildModels)
        self.widgetBuildModel.next.connect(self.addOrUpdateAnalysModels)
        self.widgetAnalysModels.next.connect(self.addOrUpdateDetailsModelSelect)
        self.widgetDetailsModelSelect.next.connect(self.addOrUpdateQualityAdjustModel)
        self.widgetQualityAdjustModel.next.connect(self.addOrUpdateInformationExtrapolacion)
        self.widgetInformationExtrapolacion.next.connect(self.addOrUpdateValidate)
        
        
        self.m_tabWidget.addTab(self.widgetDataFilter,"Datos filtrados")
        self.m_tabWidget.addTab(self.widgetChartsVariables,"Gráficas de correlación de la variables");
        self.m_tabWidget.addTab(self.widgetBuildModel,"Conformación de los modelos");
        self.m_tabWidget.addTab(self.widgetAnalysModels,"Análisis de los modelos");
        self.m_tabWidget.addTab(self.widgetDetailsModelSelect,"Detalles del modelo seleccionado");
        self.m_tabWidget.addTab(self.widgetQualityAdjustModel,"Calidad de ajuste");
        self.m_tabWidget.addTab(self.widgetInformationExtrapolacion,"Análisis de extrapolación oculta");
        self.m_tabWidget.addTab(self.widgetValidate,"Validación");
        
        self.m_tabWidget.setTabEnabled(1,False)
        self.m_tabWidget.setTabEnabled(2,False)
        self.m_tabWidget.setTabEnabled(3,False)
        self.m_tabWidget.setTabEnabled(4,False)
        self.m_tabWidget.setTabEnabled(5,False)
        self.m_tabWidget.setTabEnabled(6,False)
        self.m_tabWidget.setTabEnabled(7,False)
        self.m_tabWidget.setTabEnabled(8,False)
            
    def createMenuBar(self):
        #self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)

        self.m_frameMenuBar=QFrame (self);
        self.m_frameMenuBar.setStyleSheet ("background-color:#e0e0e0")

        self.m_frameUserMenuBar=QFrame(self.m_frameMenuBar)
        self.m_frameUserMenuBar.setStyleSheet ("background-color:#e0e0e0")

        self.m_layoutMenuBar=QHBoxLayout()
        self.m_layoutFrameUser= QHBoxLayout()

        self.m_logoMenuBar = QLabel(self.m_frameMenuBar)
        self.m_logoMenuBar.setPixmap(QPixmap(":/img/Barra_superior.png"));

        tSpacerWidget = QWidget(self.m_frameMenuBar)
        tSpacerWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        tSpacerWidget.setVisible(True)

        self.m_layoutFrameUser.setSpacing (0)
        self.m_layoutFrameUser.setContentsMargins(5, 5, 5, 5)
       
        self.m_layoutMenuBar.setContentsMargins(0, 0, 0, 0)
        self.m_layoutMenuBar.setSpacing(5)
        self.m_layoutMenuBar.addWidget (self.m_logoMenuBar)
        self.m_layoutMenuBar.addWidget (tSpacerWidget)
        self.m_layoutMenuBar.addWidget (self.m_frameUserMenuBar)
        self.m_frameMenuBar.setLayout (self.m_layoutMenuBar)


        self.setMenuWidget(self.m_frameMenuBar);
    
    def createToolsBars(self):
        self.m_toolBarsGeneral=QToolBar("General")
        self.m_toolBarsGeneral.setObjectName("generalToolBar")
        self.m_toolBarsGeneral.setIconSize(QSize(24,24))
        #self.m_toolBarsGeneral.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.addToolBar(self.m_toolBarsGeneral)
        self.createGeneralToolBar()
 
    def createCentralWidget(self):
        self.m_tabWidget=QTabWidget(self)
        self.m_tabWidget.setTabsClosable(False)
        tWidgetWelcome=Ui_WidgetPresentacion(self.m_tabWidget)
        index=self.m_tabWidget.addTab(tWidgetWelcome,"Bienvenido")
        #self.m_tabWidget.setTabIcon(index);
        self.setCentralWidget(self.m_tabWidget)
    
    def createStatusBar(self):
        self.m_statusBar=StatusBar()
        self.statusBar().addPermanentWidget(self.m_statusBar)
        self.statusBar().setFixedHeight(28)
    
    def createGeneralToolBar(self):
        self.m_openFileExcelAction = QAction(QIcon(":/img/folder-open.png"),"Cargar Archivo",self)
        self.m_helpAction=QAction(QIcon(":/img/ayuda.png"),"Ayuda de LinReg", self)
        self.m_closeAction = QAction(QIcon(":/img/Salir.png"),"Cerrar", self)
        self.m_preferenceAction = QAction(QIcon(":/img/config.png") ,"Preferencias", self)

        
        tSpacerWidget = QWidget(self.m_toolBarsGeneral)
        tSpacerWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tSpacerWidget.setVisible(True)
        
        self.m_toolBarsGeneral.addAction(self.m_openFileExcelAction)
        self.m_toolBarsGeneral.addWidget(tSpacerWidget)
        self.m_toolBarsGeneral.addAction(self.m_preferenceAction)
        self.m_toolBarsGeneral.addAction(self.m_helpAction)
        self.m_toolBarsGeneral.addAction(self.m_closeAction)

    def createConnects(self):
        self.m_closeAction.triggered.connect(self.close)
        self.m_openFileExcelAction.triggered.connect(self.selectFileData)
        self.m_helpAction.triggered.connect(self.showHelp)
        self.m_preferenceAction.triggered.connect(self.showPreference)
        self.m_tabWidget.currentChanged.connect(self.changeTabActive)
        
    def selectFileData(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Abrir archivo ...", QDir.homePath(),
                                                  "Excel Files(*.xls);Excel Files(*.xlsx)", 
                                                  options=options)
        if fileName:
            self.analysisData.readFileExcel(fileName)
            self.addOrUpdateTabBuildModels()
            self.addOrUpdateTabFilterData()
            
            
    def addOrUpdateTabFilterData(self):
        if self.widgetDataFilter == None:
            self.widgetDataFilter = WidgetDataFilter(self)
            self.widgetDataFilter.next.connect(self.addOrUpdateTabChartVariables)
            
        index = self.m_tabWidget.indexOf(self.widgetDataFilter);
        
        if index ==-1:
            index=self.m_tabWidget.addTab(self.widgetDataFilter,"Datos filtrados")
        self.m_tabWidget.setCurrentIndex(index)
        self.m_tabWidget.setTabEnabled(index,True)
        self.widgetDataFilter.updateTab()
        
    def addOrUpdateTabChartVariables(self):
        if self.widgetChartsVariables == None:
            self.widgetChartsVariables = WidgetChartVariables(self)
            self.widgetChartsVariables.next.connect(self.addOrUpdateTabBuildModels)
            
        index = self.m_tabWidget.indexOf(self.widgetChartsVariables);
        
        if index ==-1:
            index=self.m_tabWidget.addTab(self.widgetChartsVariables,"Gráficas de correlación de la variables");
        self.m_tabWidget.setCurrentIndex(index)
        self.m_tabWidget.setTabEnabled(index,True)
        self.widgetChartsVariables.updateTab()
        
    def addOrUpdateTabBuildModels(self):
        if self.widgetBuildModel == None:
            self.widgetBuildModel = WidgetBuildModel(self)
            self.widgetBuildModel.next.connect(self.addOrUpdateComparativeModel)
            
        index = self.m_tabWidget.indexOf(self.widgetBuildModel);
        
        if index ==-1:
            index=self.m_tabWidget.addTab(self.widgetBuildModel,"Conformación de los modelos");
        self.m_tabWidget.setCurrentIndex(index)
        self.m_tabWidget.setTabEnabled(index,True)
        self.widgetBuildModel.updateTab()
        
    def addOrUpdateAnalysModels(self):
        if self.widgetAnalysModels == None:
            self.widgetAnalysModels = WidgetAnalysModels(self)
            self.widgetAnalysModels.next.connect(self.addOrUpdateDetailsModelSelect)
            
        index = self.m_tabWidget.indexOf(self.widgetAnalysModels);
        
        if index ==-1:
            index=self.m_tabWidget.addTab(self.widgetAnalysModels,"Análisis de los modelos");
        self.m_tabWidget.setCurrentIndex(index)
        self.m_tabWidget.setTabEnabled(index,True)
        self.widgetAnalysModels.updateTab()
        
    def addOrUpdateDetailsModelSelect(self):
        if self.widgetDetailsModelSelect == None:
            self.widgetDetailsModelSelect = WidgetAnalysModels(self)
            self.widgetDetailsModelSelect.next.connect(self.addOrUpdateQualityAdjustModel)
            
        index = self.m_tabWidget.indexOf(self.widgetDetailsModelSelect);
        
        if index ==-1:
            index=self.m_tabWidget.addTab(self.widgetDetailsModelSelect,"Detalles del modelo seleccionado");
        self.m_tabWidget.setCurrentIndex(index)
        self.m_tabWidget.setTabEnabled(index,True)
        self.widgetDetailsModelSelect.updateTab()
    
    def addOrUpdateQualityAdjustModel(self):
        if self.widgetQualityAdjustModel == None:
            self.widgetQualityAdjustModel = WidgetAnalysModels(self)
            self.widgetQualityAdjustModel.next.connect(self.addOrUpdateInformationExtrapolacion)
            
        index = self.m_tabWidget.indexOf(self.widgetQualityAdjustModel);
        
        if index ==-1:
            index=self.m_tabWidget.addTab(self.widgetQualityAdjustModel,"Calidad de ajuste al modelo");
        self.m_tabWidget.setCurrentIndex(index)
        self.m_tabWidget.setTabEnabled(index,True)
        self.widgetQualityAdjustModel.updateTab()
    
    def addOrUpdateInformationExtrapolacion(self):
        if self.widgetInformationExtrapolacion == None:
            self.widgetInformationExtrapolacion = WidgetInformationExtrapolacion(self)
            self.widgetInformationExtrapolacion.next.connect(self.addOrUpdateValidate)
            
        index = self.m_tabWidget.indexOf(self.widgetInformationExtrapolacion);
        
        if index ==-1:
            index=self.m_tabWidget.addTab(self.widgetInformationExtrapolacion,"Información de Extrapolación");
        self.m_tabWidget.setCurrentIndex(index)
        self.m_tabWidget.setTabEnabled(index,True)
        self.widgetInformationExtrapolacion.updateTab()
    
    def addOrUpdateValidate(self):
        if self.widgetValidate == None:
            self.widgetValidate = WidgetValidate(self)
            
        index = self.m_tabWidget.indexOf(self.widgetValidate);
        
        if index ==-1:
            index=self.m_tabWidget.addTab(self.widgetValidate,"Validación");
        self.m_tabWidget.setCurrentIndex(index)
        self.m_tabWidget.setTabEnabled(index,True)
        self.widgetValidate.updateTab()
        
    def changeTabActive(self,_index):
        widget = self.m_tabWidget.currentWidget()
        if hasattr(widget, 'updateTab'):
            widget.updateTab()
        
    def nextVersion(self):
        QMessageBox.about(self,"About Sample Editor",
                          "<p>A sample text editor app built with:</p>"
                          "<p>- PyQt</p>"
                          "<p>- Qt Designer</p>"
                          "<p>- Python</p>",)
        
    def showHelp(self):
        pass
        #helpEngine = QHelpEngine('help/index.qch')
        
    def showPreference(self):
        preferencesDialog = DialogPreference(self)
        preferencesDialog.exec()