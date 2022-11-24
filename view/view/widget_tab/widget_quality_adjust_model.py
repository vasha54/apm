from view.view.widget_tab.widget_tab import WidgetTab

class WidgetQualityAdjustModel(WidgetTab):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.createUI()
        self.createWorkspace()
        self.createConnect()    
    
    def createUI(self):
        pass
    
    def createWorkspace(self):
        pass
    
    def createConnect(self):
        super().createConnect()
        
    def update(self):
        pass