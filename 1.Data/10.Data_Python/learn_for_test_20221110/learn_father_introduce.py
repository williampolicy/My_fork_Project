class Father():
    name = 'Xiaowen Kang'
class Person(Father):
    def __init__(self, name):
        self.fathername = self.name
        self.name = name
    def introduce(self):
        print("My name is", self.name, "daughter of", self.fathername)

king = Person("Grace")
king.introduce()