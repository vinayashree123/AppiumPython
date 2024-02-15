class A:
    def __init__(self,name):
        self.name=name
        print('calss A name',self.name)
class B(A):
    def __init__(self,age):
        self.age=age
        super().__init__(age)
        print("class age is", self.age)
class C(B):
    def __init__(self,name,age,email):
        super().__init__(email)
        print("email is",email)

obj = C('vina',23,'vina@123')
