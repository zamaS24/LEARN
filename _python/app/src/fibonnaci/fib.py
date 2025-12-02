# this server like a fibonnaci function 
from numpy import zeros

def fibonacci(num:int) -> int: 

    arr = zeros((num+1,))     
    arr[0] = 0 
    arr[1] = 1 

    for i in range(1,num): 
        arr[i+1] = arr[i] + arr[i-1]

    return arr[num]