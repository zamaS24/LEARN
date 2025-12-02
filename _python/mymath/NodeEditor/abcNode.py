from abc import ABC, abstractmethod


class NodeABC(ABC): 

    def __init__(self): 
        pass 

    @abstractmethod
    def add(self, a,b): 
        pass

    @abstractmethod
    def sub(self, a, b): 
        pass 
 