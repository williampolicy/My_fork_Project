# illustrating private members & private access modifier 
class Rectangle:
  __length = 0 #private variable
  __breadth = 0#private variable
  def __init__(self): 
    #constructor
    self.__length = 5
    self.__breadth = 3
    #printing values of the private variable within the class
    print(self.__length)
    print(self.__breadth)
 
rect = Rectangle() #object created 
#printing values of the private variable outside the class 

print(rect.length)
print(rect.breadth)



# 可以内部访问，不能外部访问。
#Since len is a private member and we have tried to access it outside the class, that is why we received the above error.
