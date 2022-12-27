from PyQt5.QtCore import(
  QVariant,QAbstractTableModel
)

from PyQt5 import QtCore

from view.preferences.preferences import PreferenceGUI


class TableCorrelationModel(QAbstractTableModel):
    
    def __init__(self,_headersVar,_data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.headersVar = _headersVar
        self.data =_data 
        self.decimalPlaces = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        self.formatStr = '.'+str(self.decimalPlaces)+'f'

    def rowCount(self, parent=None):
        return len(self.headersVar)

    def columnCount(self, parent=None):
        return len(self.headersVar)
    
    def headerData (self, section, direction, role=QtCore.Qt.DisplayRole):
        if role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if direction==QtCore.Qt.Horizontal or direction == QtCore.Qt.Vertical:
            return QtCore.QVariant(self.headersVar[section])
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole :
                return QVariant(str( format(self.data[index.row()][index.column()],self.formatStr) ))
            elif role == QtCore.Qt.TextAlignmentRole:
                return int(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        return QVariant()
    
    
    