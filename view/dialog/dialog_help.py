from PyQt5.QtWidgets import (
    QDialog, QColorDialog
)

from PyQt5.QtGui import(
    QPixmap,QIcon
)

from PyQt5 import QtCore, QtGui, QtWidgets,QtHelp

from view.components.help_browser import HelpBrowser
import os

class DialogHelp(QDialog):
    
    def __init__(self,_directoryHelp, _parent):
        super(DialogHelp,self).__init__(_parent)
        self.directoryHelp = _directoryHelp
        self.createWorkSpace()
        self.createConnect()
        
    def createWorkSpace(self):
        self.hLayout = QtWidgets.QHBoxLayout(self)
        self.helpEngine = QtHelp.QHelpEngine( os.path.join(self.directoryHelp, "help","doc", "lin_reg.qhc"),self)
        self.helpEngine.setupData()
        
        self.tWidget = QtWidgets.QTabWidget(self)
        self.tWidget.setMaximumWidth(200)
        self.tWidget.addTab(self.helpEngine.contentWidget(), "Contenidos")
        self.tWidget.addTab(self.helpEngine.indexWidget(), "Índices")
        
        self.textViewer = HelpBrowser(self.helpEngine,self)
        self.textViewer.setSource(QtCore.QUrl("qthelp://lin_reg.umcc.cu/doc/index.html"))
        
        self.helpEngine.setUsesFilterEngine(True)
        self.helpEngine.contentWidget().linkActivated.connect(self.textViewer.setSource)
        self.helpEngine.indexWidget().linkActivated.connect(self.textViewer.setSource)
        
        self.horizSplitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.horizSplitter.insertWidget(0, self.tWidget)
        self.horizSplitter.insertWidget(1, self.textViewer)
        
        self.hLayout.addWidget(self.horizSplitter)
        
        self.setLayout(self.hLayout)
        self.setWindowIcon(QIcon(":/img/ayuda.png"))
        self.setWindowTitle("Ayuda de LinReg")
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
    
    def createConnect(self):
        pass
        
        QtCore.QMetaObject.connectSlotsByName(self)
    
   