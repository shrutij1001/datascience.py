'''SUMMER INTERNSHIP PROGRAMME
ASSIGNMENT-2
SHRUTI JAIN
0901ET201054
ELCTRONIC AND TELECOMMUNICATION
#LIST PROPERTIES
l=["SHRUTI","JAIN","0901ET201054","1STYEAR","ET"]
"LENGTH OF THE LIST"
A=len(l)
print("length of the list",A)
"Traverse the list"
for i in l:
  print(i)
"using append function"
b=l.append(12)
print("using append function",b)
"extend the list"
r=["bhopal","delhi","gwalior"]
print("extention of the list",l.extend(r))
"reverse the list"
c=len(l)
for i in range(0,c-1):
  print(l[c-1-i])
"another way to reverse the list"
print("Revert of the list",l[::-1])
"list indices"
print(l[0])
print(l[2:])
print(l[::1])
"type conversion"
a=tuple(l)
print("tuple conversion of the list",a)
"sorting of the list"
list1=[90,86,6,45,80,80]
print(list1.sort())
"delete the last element"
print(l.pop())
"REMOVE FUNCTION"
list1.remove(80)
print("list after removing 80",l)
print(list1.index(90))
print("clearing the list",l.clear())
print(list1.index(80))'''
#DICTIONARY PROPRERTIES
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#get the values of the keys
print("values of the list")
x = car.values()
print(x)
#make tha copy of the dic
print("copy of the dictionary")
x = car.copy()
print(x)
#return the value of model
print("return the values of the dictonary")
x = car.get("model")
print(x)
#return utems
print("this fuction give the items in the dictionary")
x = car.items()
print(x)
#return the keys
print("return the keys")
x = car.keys()
print(x)
#chnage the value of any key
print("to change the values of the keys")
x = car.setdefault("model", "Bronco")
print(x)
#upadte the dictionary
print("Update the dictionry")
car.update({"color": "White"})
print(car)
#delete all the itmes of the list
print("clear delete all the items in the list")
car.clear()
print(car)
#from key method
print("creating the dictionay")
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
print("delete the elment in the dic")
mark= {1:30,2:30,3:40,4:45}
print ("Dictionary         -->", mark)
del mark
print("find the sum average of the elements in the list")
mark = {1:8.9, 2:5.6, 4:6.7, 7:9.1, 8:5.3}
print ("Dictionary -->", mark)
s = 0
for i in mark:
    s = s + mark[i]
print ("\nSum        -->", s)
print ("Average    -->", s/len(mark))
print ("Average    -->", s//len(mark))
print("Minimum and maximum value of the dictionary")
mark= {1:30,2:30,3:40,4:45}
print ("Dictionary -->", mark)

print ("\nMin value  -->", min(mark.values()))
print ("Max value  -->", max(mark.values()))

mark= {1:30,2:30,3:40,4:45}
print ("Dictionary       -->", mark)

# List out keys and values separately
keyList = list(mark.keys())
valList = list(mark.values())

print ("\nValue = 30; Key -->", keyList[valList.index(30)])
print ("Value = 40; Key -->", keyList[valList.index(40)])

# one-liner
print ("\nValue = 40; Key -->",list(mark.keys())[list(mark.values()).index(40)])
print ("Value = 45; Key -->",list(mark.keys())[list(mark.values()).index(45)])