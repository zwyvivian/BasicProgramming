class Person:
    def __init__(self,name,age,sex,rel):
        self.name=name
        self.age=age
        self.sex=sex
        self.relation=rel

    def do_private_stuff(self):
        pass


#p1.partner=p2
#p2.partner=p1

class RelationShip:
    '''save relationship'''
    def __init__(self):
        #self.couple=[]
        pass

    def make_couple(self,obj1,obj2):
        self.couple=[obj1,obj2]
        print("couple done" , self.couple[0],obj2.name)

    def get_my_partner(self,obj):
        for i in self.couple:
            if i !=obj:
                return i
            else:
                print("no couple")
    def break_up(self):
        self.couple.clear()

relation_obj=RelationShip()
p1= Person("Mjj",23,'M',relation_obj)
p2=Person("vivian",22,'F',relation_obj)
relation_obj.make_couple(p1,p2)
print(relation_obj.couple)
print(p1.relation.couple[0])
