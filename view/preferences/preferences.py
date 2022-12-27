from pattern.singleton import SingletonDoubleChecked
from pattern.observer import IObservable

from PyQt5.QtCore import(
    QSettings,QObject
)

class PreferenceGUI(QObject,SingletonDoubleChecked):
    
    organization = "UM"
    application = "LinReg"
    
    DECIMAL_PLACES = 'decimal_places'
    COLOR_BACKGROUND_CHART = 'color_background_chart'
    COLOR_TEXT_CHART = 'color_text_chart'
    COLOR_AXES_CHART = 'color_axes_chart'
    
    LIST_PREFERENCES = [DECIMAL_PLACES,COLOR_BACKGROUND_CHART,COLOR_TEXT_CHART,COLOR_AXES_CHART]
    
    DICT_PREREFRENCE_DEFAULT = {
        DECIMAL_PLACES:4,
        COLOR_AXES_CHART:'#000000',
        COLOR_BACKGROUND_CHART:'#ffffff',
        COLOR_TEXT_CHART:'#000000',
    }
    
    def __init__(self):
        self.settings = QSettings(self.organization,self.application)
        for k,v in self.DICT_PREREFRENCE_DEFAULT.items():
            if self.settings.contains(k) == False:
                self.settings.setValue(k,v)
        self.writeSettings()
        self.observers = []
        
        
    def resetSettings(self):
        for k,v in self.DICT_PREREFRENCE_DEFAULT.items():
            self.settings.setValue(k,v)
        self.writeSettings()
        self.update(self.LIST_PREFERENCES)
        
    
    def writeSettings(self):
        self.settings.sync()
    
    def setValueSettings(self,_key,_value):
        if _key in self.LIST_PREFERENCES and _value != self.settings.value(_key,self.DICT_PREREFRENCE_DEFAULT[_key]):
            self.settings.setValue(_key,_value)
            self.writeSettings()
            self.update([_key])
        
    
    def getValueSettings(self,_key):
        value = None
        if _key in self.LIST_PREFERENCES:
            value = self.settings.value(_key,self.DICT_PREREFRENCE_DEFAULT[_key])
        return value
    
    def updateValueSettings(self,_mapsKeyValue):
        listPreference = []
        for k,v in _mapsKeyValue.items():
            if k in self.LIST_PREFERENCES and v!=None and v!=self.settings.value(k,self.DICT_PREREFRENCE_DEFAULT[k]):
                self.settings.setValue(k,v)
                listPreference.append(k)
        self.writeSettings()
        if len(listPreference) > 0:
            self.update(listPreference)
        
    def subscribe(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        
    
    
    def unsubscribe(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
        
    
    def update(self,_listPreferenceChange):
        for obs in self.observers:
            if hasattr(obs,'changePreference'):
                obs.changePreference(_listPreferenceChange)
        
    
    