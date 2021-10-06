import os
import sys
import datetime
import logging

class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ezLogger(object, metaclass=SingletonType):
    """This is intended to be a simple logger """
    __logger = None

    def __init__(self, dir="./log",name=None):
         if not isinstance(dir,str):
             self.dir = "./log"
         else:
             self.dir = dir    
         if not os.path.isdir(self.dir):
            os.mkdir(self.dir)
         if not isinstance(name,str):
             name = os.path.basename(sys.argv[0]).split('.')[0]
         self.name = name
        
         self._logger = logging.getLogger(self.name)
         self._logger.setLevel(logging.DEBUG)
         formatter = logging.Formatter('%(asctime)s [%(levelname)s|%(filename)s:%(lineno)s] > %(message)s')
         now = datetime.datetime.now()
         fileHandler = logging.FileHandler(self.dir + "/" + self.name + ".log" + now.strftime(".%Y%m%d"))

         streamHandler = logging.StreamHandler()

         fileHandler.setFormatter(formatter)
         streamHandler.setFormatter(formatter)

         self._logger.addHandler(fileHandler)
         self._logger.addHandler(streamHandler)       

    def get_logger(self):
        return self._logger    


if __name__ == "__main__":
    print("ezLogger") 
    log = ezLogger().get_logger()

    log.debug("debug 1")

    log2 = ezLogger().get_logger()
    log.debug("debug 2")
