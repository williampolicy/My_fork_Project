#Python program showing
# abstract class cannot
# be an instantiation
from abc import ABC,abstractmethod
 
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
 
class Snake(Animal):
    def move(self):
        print("I can crawl")
 
class Dog(Animal):
    def move(self):
        print("I can bark")
 
class Lion(Animal):
    def move(self):
        print("I can roar")
 


# Driver code
try:
    C =Human()
    C.move()
    #print(C.move)
except Exception as err:
    print (err)
  



K=Human()
K.move()