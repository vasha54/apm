from PyQt5 import QtCore, QtGui, QtWidgets

class Delegate(QtWidgets.QStyledItemDelegate):
    def editorEvent(self, event, model, option, index):
        checked = index.data(QtCore.Qt.CheckStateRole)
        ret = QtWidgets.QStyledItemDelegate.editorEvent(self, event, model, option, index)
        if checked != index.data(QtCore.Qt.CheckStateRole):
            self.parent().checked.emit(index)
        return ret
    

    
class ListView(QtWidgets.QListView):
    checked = QtCore.pyqtSignal(QtCore.QModelIndex)
    
    def __init__(self, *args, **kwargs):
        super(ListView, self).__init__(*args, **kwargs)
        self.setItemDelegate(Delegate(self))