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
from view.view.widget_data_filter import WidgetDataFilter
from view.view.widget_charts_variables import WidgetChartVariables
from view.resource import resource


class App(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.createWorkSpace()
        self.analysisData = AnalysisData()

    def createWorkSpace(self):
        self.createMenuBar()
        self.createToolsBars()
        self.createCentralWidget()
        self.createStatusBar()
        self.createConnects()
        self.widgetDataFilter = None
        self.widgetChartsVariables = None
        
    def createMenuBar(self):
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)

        self.m_frameMenuBar=QFrame (self);
        self.m_frameMenuBar.setStyleSheet ("background-color:#cecece")

        self.m_frameUserMenuBar=QFrame(self.m_frameMenuBar)
        self.m_frameUserMenuBar.setStyleSheet ("background-color:#cecece")

        self.m_layoutMenuBar=QHBoxLayout()
        self.m_layoutFrameUser= QHBoxLayout()

        self.m_logoMenuBar = QLabel(self.m_frameMenuBar)
        self.m_logoMenuBar.setPixmap(QPixmap(":/img/Barra_superior.png"));

        self.m_helpAction=QAction(QIcon(":/img/falta.png"),"Ayuda de SISCOFI", self)
        self.m_helpAction.setObjectName("helpAction")

        self.m_closeAction = QAction(QIcon(":/img/falta.png"),"Cerrar", self)
        self.m_closeAction.setObjectName("closeAction")


        tSpacerWidget = QWidget(self.m_frameMenuBar)
        tSpacerWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        tSpacerWidget.setVisible(True)

        self.m_toolButtonOptions=QToolButton(self)
        self.m_toolButtonOptions.setText ("Opciones  ")

        self.m_toolButtonOptions.setPopupMode (QToolButton.MenuButtonPopup)
        self.m_toolButtonOptions.addAction (self.m_helpAction)
        self.m_toolButtonOptions.addAction (self.m_closeAction)

        self.m_layoutFrameUser.setSpacing (0)
        self.m_layoutFrameUser.setContentsMargins(5, 5, 5, 5)
       
        self.m_layoutMenuBar.setContentsMargins(0, 0, 0, 0)
        self.m_layoutMenuBar.setSpacing(5)
        self.m_layoutMenuBar.addWidget (self.m_logoMenuBar)
        self.m_layoutMenuBar.addWidget (tSpacerWidget)
        self.m_layoutMenuBar.addWidget(self.m_toolButtonOptions)
        self.m_layoutMenuBar.addWidget (self.m_frameUserMenuBar)
        self.m_frameMenuBar.setLayout (self.m_layoutMenuBar)


        self.setMenuWidget(self.m_frameMenuBar);
    
    def createToolsBars(self):
        self.m_toolBarsGeneral=QToolBar("General")
        self.m_toolBarsGeneral.setObjectName("generalToolBar")
        self.m_toolBarsGeneral.setIconSize(QSize(24,24))
        self.addToolBar(self.m_toolBarsGeneral)
        self.createGeneralToolBar()
 
    def createCentralWidget(self):
        self.m_tabWidget=QTabWidget(self)
        self.m_tabWidget.setTabsClosable(False)
        tWidgetWelcome=QWidget(self.m_tabWidget);
        tWidgetWelcome.setStyleSheet("border-image:url(':/themeBasic/images/fondo_bienvenida.png');");
        index=self.m_tabWidget.addTab(tWidgetWelcome,"Bienvenido");
        #self.m_tabWidget.setTabIcon(index);
        self.setCentralWidget(self.m_tabWidget)
    
    def createStatusBar(self):
        self.m_statusBar=StatusBar()
        self.statusBar().addPermanentWidget(self.m_statusBar)
        self.statusBar().setFixedHeight(28)
    
    def createGeneralToolBar(self):
        self.m_openFileExcelAction = QAction(QIcon(":/img/falta.png"),"Cargar Archivo",self)
        self.m_toolBarsGeneral.addAction(self.m_openFileExcelAction)


    def createConnects(self):
        self.m_closeAction.triggered.connect(self.close)
        self.m_openFileExcelAction.triggered.connect(self.selectFileData)
        
    def selectFileData(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Abrir archivo ...", QDir.homePath(),
                                                  "Excel Files(*.xls);Excel Files(*.xlsx)", 
                                                  options=options)
        if fileName:
            self.analysisData.readFileExcel(fileName)
            self.addOrUpdateTabFilterData()
            
    def addOrUpdateTabFilterData(self):
        if self.widgetDataFilter == None:
            self.widgetDataFilter = WidgetDataFilter(self)
            self.widgetDataFilter.next.connect(self.addOrUpdateTabChartVariables)
            
        index = self.m_tabWidget.indexOf(self.widgetDataFilter);
        
        if index ==-1:
            index=self.m_tabWidget.addTab(self.widgetDataFilter,"Datos filtrados");
        self.m_tabWidget.setCurrentIndex(index)
        self.widgetDataFilter.update()
        
    def addOrUpdateTabChartVariables(self):
        if self.widgetChartsVariables == None:
            self.widgetChartsVariables = WidgetChartVariables(self)
            self.widgetChartsVariables.next.connect(self.addOrUpdateTabBuildModels)
            
        index = self.m_tabWidget.indexOf(self.widgetChartsVariables);
        
        if index ==-1:
            index=self.m_tabWidget.addTab(self.widgetChartsVariables,"Gráficas de correlación de la variables");
        self.m_tabWidget.setCurrentIndex(index)
        self.widgetChartsVariables.update()
        
        
    def addOrUpdateTabBuildModels(self):
        pass
        
    def nextVersion(self):
        QMessageBox.about(self,"About Sample Editor",
                          "<p>A sample text editor app built with:</p>"
                          "<p>- PyQt</p>"
                          "<p>- Qt Designer</p>"
                          "<p>- Python</p>",)