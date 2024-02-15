class India:
    def lang(self):
        #self.lang=lang
        print("hindi")
    def capital(self):
        #self.cap=cap
        print("delhi")
    def type(self):
        #self.type=type
        print("developing")

class USA:
    def lang(self):
        #self.lang=lang
        print("english")
    def capital(self):
        #self.cap=cap
        print("washington")
    def type(self):
        #self.type=type
        print("developed")

"""obj_ind = India()
obj_usa = USA()
for i in (obj_ind,obj_usa):
    i.capital()
    i.lang()
    i.type()"""

obj_ind=India()
obj_usa = USA()
def func(obj):
    obj.capital()
    obj.lang()
    obj.type()

func(obj_ind)
func(obj_usa)


list1 = [x*x if x%2==0 else x*x*x for x in range(1,5)]
print(list1)