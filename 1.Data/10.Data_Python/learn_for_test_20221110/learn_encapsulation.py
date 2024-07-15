# illustrating public members & public access modifier 
class pub_mod:
    # constructor
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
 
    def Age(self): 
        # accessing public data member 
        print("Age: ", self.age)
# creating object 
obj = pub_mod("Jason", 35);
# accessing public data member 
print("Name: ", obj.name)  
# calling public member function of the class 
obj.Age()