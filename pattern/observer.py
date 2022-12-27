from abc import ABC, abstractmethod

class IObservable(ABC):
    
    @abstractmethod
    def subscribe(self, observer):
        """subscription"""
    
    @abstractmethod
    def unsubscribe(self, observer):
        """unsubscription"""
        
    @abstractmethod
    def update(self):
        """update method"""
        
class IObserver(ABC):
    
    @abstractmethod
    def notifications(self):
        """notifications method"""
        
class IObserverPrefence(ABC):
    
    @abstractmethod
    def changePreference(self,_listPreferenceChange):
        """notifications method"""
    
    
    
    







