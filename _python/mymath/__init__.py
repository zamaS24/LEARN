# this file serves as 



__version__ ='0.1.0'

try:
    # export the functions
    # from .add import add
    from .div import division
    from .mult import multiply
    from .sub import subtract

    # also export what is exported from the package of adv 
    from .adv import square
    # from .adv import square 
    
except ImportError:
    from add import add 
    from div import division 
    from mult import multiply
    from sub import subtract
    from adv import square


# You can also start importing withotu using relative paths, just like this : 
from mymath.add import add



if __name__=='__main__':
    print('package version is :', __version__)