class Dog():
    d_type ="jingba"
    sss='sss'
    def __init__(self,name,age): #私有信息
        print("hahahaha",name,age)
        self.name=name
        self.age=age

    def say_hi(self):
        print("hello, i am  a dog ", self.d_type,self.name)


d= Dog("vi",3)
d1=Dog("do",8)

d.say_hi()

Dog.d_type='buou'
print(id(d.d_type),id(Dog.d_type))

class People:
    nationality='zN'
    def __init__(self,name,sex,age):
        self.name=name
        self.age=age
        self.sex=sex
        #self.nationality=nationality


p=People('XT',12,'M')
p2=People('xe',31,'F')

p.nationality='JP'

print(p.nationality)
print(p2.nationality)
People.nationality='CN'
print(p.nationality)
print(p2.nationality)

