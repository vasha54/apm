from PyQt5 import QtCore,QtWidgets

from view.delegate.delegate import DelegateCkeckBoxListView, DelegateRadioButtonsListView

class ListViewCheckBox(QtWidgets.QListView):
    checked = QtCore.pyqtSignal(QtCore.QModelIndex)
    
    def __init__(self,_parent=None, *args, **kwargs):
        super(ListViewCheckBox, self).__init__(_parent ,*args, **kwargs)
        self.setItemDelegate(DelegateCkeckBoxListView(self))
        
class ListViewRadioButton(ListViewCheckBox):
    
    radioButton = QtCore.pyqtSignal(QtCore.QModelIndex)
    
    def __init__(self,_parent=None, *args, **kwargs):
        super(ListViewCheckBox, self).__init__( _parent,*args, **kwargs)
        self.setItemDelegate(DelegateRadioButtonsListView(self))
        self.checked.connect(self.onChecked)
        self.indexCurrent = None
        
    def onChecked(self,_index):
        if _index.data(QtCore.Qt.ItemDataRole.CheckStateRole) == QtCore.Qt.Checked:
            self.indexCurrent = _index
            model = self.indexCurrent.model()
            rows= model.rowCount()
            for i in range(0,rows):
                itemX = model.index(i,0)
                if itemX.row() != self.indexCurrent.row():
                    model.setData(itemX,QtCore.Qt.Unchecked,QtCore.Qt.ItemDataRole.CheckStateRole)
            self.radioButton.emit(self.indexCurrent)
            
    