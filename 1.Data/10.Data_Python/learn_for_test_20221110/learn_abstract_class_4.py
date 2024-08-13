# Python program showing
# abstract properties
 
import abc
from abc import ABC, abstractmethod
 
class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"
class child(parent):
      
    @property
    def geeks(self):
        return "child class"
  
  
try:
    r =parent()
    print( r.geeks)
except Exception as err:
    print (err)
  
r = child()
print (r.geeks)


#In the above example, the Base class cannot be instantiated because it has only an abstract version of the property getter method. 