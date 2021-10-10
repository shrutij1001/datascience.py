"""class being:
    def __init__(self,n,s,r):
        self.name=n
        self.std=s
        self.roll_no=r
    def hello(self):
        if self.name == "shruti":
            print("name  of the person",self.name,"studing in",self.std,"have roll_no",self.roll_no)
        else:
            print("wrong input/error")
#inhertance
class vehicle:
    def general_usage(self):
        print("transportation")
class car(vehicle):
    def __init__(self):
        print("its a car")
        self.wheels=4
        self.seats=4
    def specific_usage(self):
        print("long drive,vaccation")
class bike(vehicle):
    def __init__(self):
        print("its a bike")
        self.wheels=2
        self.seats=2
    def specific_usage(self):
        print("long drive,vaccation")
c=car()
c.specific_usage()
c.general_usage()
print(c.wheels)
b=bike()
b.specific_usage()
b.general_usage()
print(isinstance(c,car))#c is a component of car
print(issubclass(car,vehicle))#car is a class of vehicle a subclass

class employee:
    def __init__(self,n,r,c,s,g):
        self._name=n
        self._rollno=r
        self._clas=c
        self._salary=s
        self._grade=g
    def elmplyee_detail(self):
        print("name:",self._name,"rollno:",self._rollno,"class:",self._clas,"salary:",self._salary)
x=employee("shruti",24,12,"12m",9.7)
(x.elmplyee_detail())
print(x._name)
"""
'''from matplotlib import pyplot as plt
x=[0,1,2,3]
syares=[0,1,4,9]
plt.plot(x,squares,'g',label='enfield',linewidth=5)
plt.title("deere")
plt.grid()
plt.xlabe("xaxis")
plt.show()
'''
'''a=input("")
b=list(a)
b.sort(reverse=True)
letter=[]
count=[]
for i in range(len(a)):
    n=b.count(b[i])
    if b[i] not in letter:
        letter.append(b[i])
        count.append(n)
print(letter)
print(count)
'''
print("\U0001F602")
print("\U0001F92A")


def printinfo(name, age):
    print("Name: ", name, end=', ')
    print("Age: ", age)
    return


printinfo(age=50, name="miki")
print( 2 ** 3 ** 2+20/2)
info={"name":"Sandy", "age":17}
print(list(info.keys()))
def f(l1,l2):
    l1=set(l1)
    l2=set(l2)
    l3=l1.union(l2)
    l4=l1.intersection(l2)
    l5=l3-l4
    l5=list(l5)
    l5.sort()
    return l5
x=[1,2,8,9,3,7,1,66,23,42,81,26,-9,2]
y=[4,8,66,26,-8,2,226,18]
print(f(x,y))
def f1(n):
    flag=0
    for x in range(1,n):
        for y in range(1,n):
            for z in range(1,n):
                if(n==(x**3+y**3+z**3)):
                    flag=1
    if (flag==0):
        return False

    else:
        return True
print(f1(37))
for i in range(0,8,2):
    print(i)


