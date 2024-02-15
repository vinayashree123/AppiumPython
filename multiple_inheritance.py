"""class base1:
    def __init__(self):
        self.str='hi'
        print("base1")
class base2:
    def __init__(self):
        self.str2='hello'
        print("base2")
class derived(base1,base2):
    def __init__(self):
        base1.__init__(self)
        base2.__init__(self)
        print("derived")
    def print(self):
        print(self.str,self.str2)

obj = derived()
obj.print()"""

class Mammal:
    def __init__(self,name):
        print(name,'is a mammal')
class canfly(Mammal):
    def __init__(self,fly):
        print(fly,'cant fly')
        super().__init__(fly)
class canswim(canfly):
    def __init__(self,swim):
        print(swim,'cant swim')
        super().__init__(swim)
class Animal(canswim):
    def __init__(self,name):
        super().__init__(name)
obj = Animal('Dog')

class Mammal:
    def __init__(self,name):
        print(name,'is mammal')

class canfly(Mammal):
    def __init__(self,fly):
        print(fly,'cant fly')
        super().__init__(fly)

class canswim(Mammal):
    def __init__(self,swim):
        print(swim,'cant swim')
        super().__init__(swim)
class Animal(canswim):
    def __init__(self,name):
        super().__init__(name)
obj = Animal('Dog')