from PyQt5.QtWidgets import (
    QWidget
)


class StatusBar(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_date = None 
        self.m_currentTime = None
        self.createWorkspace()
        self.createConnect()
        
    def createWorkspace(self):
        pass
    
    def createConnect(self):
        pass
        
    