__version__ = '1.0.0'
__author__='OMARI Hamza'
__GITHUB__ ='zamas24'




try: 
    # .sqrt to indicate the module is within the package
    from .sqrt import square
    from .sqrt import StaticClass
except ImportError: 
    from sqrt import square
    from sqrt import StaticClass



if __name__ == '__main__': 
    print('author : ', __author__)
    print('StaticClass Num classes: ', StaticClass.NUM_CLASSES)