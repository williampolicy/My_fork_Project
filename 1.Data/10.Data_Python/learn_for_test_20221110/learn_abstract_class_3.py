# Python program invoking a
# method using super()
 
import abc
from abc import ABC, abstractmethod
 
class R(ABC):
    def rk(self):
        print("Abstract Base Class")
 
class K(R):
    def rk(self):
        #super().rk()   
        #The concrete class provides an implementation of abstract methods, the abstract base class can also provide an implementation by invoking the methods via super(). 
        print("I am subclass of R(). subclass ")
 
# Driver code
r = K()
r.rk()