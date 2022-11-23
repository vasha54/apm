from PyQt5.QtWidgets import (
    QWidget
)

from PyQt5 import QtCore


class WidgetTab(QWidget):
    
    next = QtCore.pyqtSignal()
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    def clickNextStage(self):
        print('Padre')
        self.next.emit()