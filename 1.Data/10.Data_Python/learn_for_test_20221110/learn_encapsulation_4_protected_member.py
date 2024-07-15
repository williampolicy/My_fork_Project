# illustrating protected members & protected access modifier 
class details:
    _name="Jason"
    _age=35
    _job="Developer"
class pro_mod(details):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._job)
 
# creating object of the class 
obj = pro_mod()
# direct access of protected member
#print("Name:",obj.name)
#print("Age:",obj.age)



# It is quite clear from the output that the class pro_mod was successfully 
# able to inherit the variables from the class details and print them to 
# the console, although they were protected variables. And when we tried to refer to them outside of their parent class and the sub-class, we got an AttributeError for the same.