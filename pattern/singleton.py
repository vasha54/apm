import threading


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class SingletonDoubleChecked(object):
 
    # resources shared by each and every
    # instance
 
    __singleton_lock = threading.Lock()
    __singleton_instance = None
 
    # define the classmethod
    @classmethod
    def instance(cls):
 
        # check for the singleton instance
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
 
        # return the singleton instance
        return cls.__singleton_instance
 