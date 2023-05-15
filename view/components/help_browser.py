from PyQt5 import QtCore,QtWidgets

class HelpBrowser(QtWidgets.QTextBrowser):
    
    def __init__(self, _helpEngine, _parent):
        super(HelpBrowser,self).__init__(_parent)
        self.helpEngine = _helpEngine
        self.setStyleSheet("color:#000000;")
        
    
    def loadResource (self,_type, _nameUrl):
        if _nameUrl.scheme() == "qthelp":
            return self.helpEngine.fileData(_nameUrl)
        else:
            return super(HelpBrowser,self).loadResource(_type, _nameUrl)
    