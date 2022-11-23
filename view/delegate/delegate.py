from PyQt5 import QtCore,QtWidgets

class DelegateCkeckBoxListView(QtWidgets.QStyledItemDelegate):
    
    def editorEvent(self, event, model, option, index):
        checked = index.data(QtCore.Qt.CheckStateRole)
        ret = QtWidgets.QStyledItemDelegate.editorEvent(self, event, model, option, index)
        if checked != index.data(QtCore.Qt.CheckStateRole):
            self.parent().checked.emit(index)
        return ret
    

class DelegateRadioButtonsListView(DelegateCkeckBoxListView):
    
    def __init__(self, *args, **kwargs):
        super(DelegateRadioButtonsListView, self).__init__(*args, **kwargs)
        
    def editorEvent(self, event, model, option, index):
        checked = index.data(QtCore.Qt.CheckStateRole)
        if checked == QtCore.Qt.CheckState.Unchecked:
            ret = QtWidgets.QStyledItemDelegate.editorEvent(self, event, model, option, index)
            self.parent().checked.emit(index)
            return ret
        return True
    
    

    
