from PyQt5.QtCore import(
    QAbstractTableModel, QVariant, QAbstractItemModel, 
)

from PyQt5 import QtCore ,Qt

from controller.analysis_data import AnalysisData
from model.modelLMR import ModelLMR

from view.preferences.preferences import PreferenceGUI

class ComparativeModelsModel(QAbstractTableModel):
    
    def __init__(self,_keyModels, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.headersName=['Modelos', 'R-cua', 'R-cua adj','RMSE','AIC', 'BIC']
        self.keyModels = list(_keyModels)
        
    def rowCount(self, parent=None):
        return len(self.keyModels)

    def columnCount(self, parent=None):
        return len(self.headersName)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        placeDecimal = int(PreferenceGUI.instance().getValueSettings(PreferenceGUI.DECIMAL_PLACES))
        formatStr = '.'+str(placeDecimal)+'f'
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                if index.column() == 0:
                    return str(AnalysisData().getDataModel(self.keyModels[index.row()],ModelLMR.NAME))
                elif index.column() == 1:
                    return str(format(AnalysisData().getDataModel(self.keyModels[index.row()],ModelLMR.RCUAD),formatStr))
                elif index.column() == 2:
                    return str(format(AnalysisData().getDataModel(self.keyModels[index.row()],ModelLMR.RCUAD_ADJUST),formatStr))
                elif index.column() == 3:
                    return str(format(AnalysisData().getDataModel(self.keyModels[index.row()],ModelLMR.RMSE_MODEL),formatStr))
                elif index.column() == 4:
                    return str(format(AnalysisData().getDataModel(self.keyModels[index.row()],ModelLMR.AIC),formatStr))
                elif index.column() == 5:
                    return str(format(AnalysisData().getDataModel(self.keyModels[index.row()],ModelLMR.BIC),formatStr))
            elif role == QtCore.Qt.TextAlignmentRole:
                return int(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        # if index.isValid():
        #     if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
        #         varI = self.namesVarI[index.row()]
        #         if index.column() == 0:
        #             return QVariant(varI)
        #         elif index.column() == 1:
        #             limitLower = format(AnalysisData().getDataModel(self.keyModel,ModelLMR.LOWER_LIMIT_THIS_VARI_EXTRAPOLATION_HIDE,nameVar=varI),self.formatStr)
        #             return QVariant(limitLower)
        #         elif index.column() ==2:
        #             limitUpper = format(AnalysisData().getDataModel(self.keyModel,ModelLMR.UPPER_LIMIT_THIS_VARI_EXTRAPOLATION_HIDE,nameVar=varI),self.formatStr)
        #             return QVariant(limitUpper)
        #     elif role == QtCore.Qt.TextAlignmentRole:
        #         return int(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        return QVariant()
    
    def headerData (self, section, direction, role=QtCore.Qt.DisplayRole):
        if role!=QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if direction==QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.headersName[section])
        
    
        
    
   