
# Python program showing
# implementation of abstract
# class through subclassing
 
import abc
 
class parent:      
    def geeks(self):
        pass
 
class child(parent):
    def geeks(self):
        print("i am a child class, a  subclass of Parent.child class")
 
# Driver code
print( issubclass(child, parent))
print( isinstance(child(), parent))

K = child()
K.geeks()
