class SingletonMEta(type):
    _instances={}
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance=super(SingletonMEta,cls).__call__(*args, **kwds)
            cls._instances[cls]=instance
        return cls._instances[cls]
class logger(metaclass=SingletonMEta):
    def __init__(self):
        print("Logger initiated")

logger1=logger()
logger2=logger()
print(logger1 is logger2)