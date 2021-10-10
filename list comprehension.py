'''from itertools import combinations_with_replacement
x=1
y=2
z=3
n=3
l=[[i for i in range(x+1)],[a for a in range(y+1)],[w for w in range(z+1)]]
print(l)
comb = combinations_with_replacement(l, 3)
a=[i for i in list(comb)]
print(a)
from sys import stdin
n=int(input())
s=list(map(int,stdin.readline()))
a = s.sort()
l = len(a)
for i in range(l):
    if a[l - (i + 1)] > a[l - (i + 2)]:
        print(a[l - (i + 2)])
n = int(input())
arr = list(map(int, input().split()))
print(arr)
print(len(arr))
arr.sort()
print(arr)
import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    sum1=0
    for i in range(len(ar)):
        sum1+=ar[i]
    print(sum1)
    return sum1

if __name__ == '__main__':
    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
a={'name':[2,3,4],'value':[3,5,6]}
sum=0
for i in a['name']:
    sum+=i;
print(sum)
import sys
sring,k= (sys.stdin.readline().split())
res=''.join(sorted(sring))
from itertools import combinations_with_replacement
a=list(combinations_with_replacement(res,2))
sr=''
for i in a:
    sr=i[0]+i[1]
    print(sr)
#griupby function
import itertools
s=list((input()))
key_func = lambda x: x[0]
tup=[]
for key, group in itertools.groupby(s, key_func):
    a=list(group).count(key)
    print((a,eval(key)))
from itertools import combinations
a=int(input())
b=input().strip().split()
c=int(input())
tc,ac=0,0
d= combinations(b, c)
y = [' '.join(i) for i in d]
for i in y:
    tc+=1
    if 'a'in i:
        ac+=1
w=ac/tc
print("%.3f"%w)
k,m=(input().strip().split())
s=0
for i in range(int(k)):
    c = list(input().strip().split())
    w=max(c)
    print(type(w))
    s+=w*w
print(s)
import itertools
import sys
k, m = map(int, sys.stdin.readline().split())
s=0
for i in range(k):
    c=list(map(int, sys.stdin.readline().split()))
    for i in itertools.product(*c):
        res = sum([int(x) ** 2 for x in tp]) % m
        if res > s:
            mx = res

    print(s)'''
'''K, M = map(int, input().split())
N = []

for _ in range(K):
    N.append(map(int, input().split())[1:]))
    print(N)
MAX = -1
for i in product(*N):
    MAX = max(sum(map(lambda x: x ** 2, i)) % M, MAX)

print(MAX)
import numpy as np
import sys
n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    c = list(map(int, sys.stdin.readline().split()))
    a = np.array(c)
print(a)
a=[2,3,4,5,2,3,4,7]
for i in a:
    b=a.count(i)
    if b==1:
        print(i)
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print(c)
elif b>a and b>=c:
    print(b)
else:
    print(c)
l={1:0.23,2:22,3:21}
s=0
for a in l:
    s=s+l[a]
    print(s)
keylist=list(l.keys())
vallist=list(l.values())
print(keylist,vallist)
print("value=0.23",keylist[vallist.index(0.23)])
d=['anamika','hello',980,098]
for j in range(0,len(d)):
    print(d[j])
def pri(l):
    l=[0,0,0]
    print(l)
    return
l=[2,3,45]
print(pri(l))
password=(input("Enter the password entered by user"))
upper_case=0
lower_case=0
character=0
digits=0
length=len(password)
if password!='\n' and length>=6 and length<=12:
	if(password>='0' and password<='9'):
		digits+=1
	elif(password>='a' and password<='z'):
		lower_case+=1
	elif(password>='A' and password<='Z'):
		upper_case+=1
	elif(password=='$'or password=='#' or password=='@'):
		character+=1
if(digits!=0 and upper_case!=0 and lower_case!=0 and character!=0):
	print("Valid")
else:
    print("Unvalid")
password=eval(input("Enter the password entered by user"))
l=len(password)
if password!='\n' and l>=6 and l<=12:
    if '''
p=input("Enter the password entered by user")
u="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$123456789"

'''l, u, p, d = 0, 0, 0, 0
s = input("enetr the pass")
if (len(s) >= 6 and len(s)<=12):
	for i in s:
		if (i.islower()):
			l += 1
		if (i.isupper()):
			u += 1
		if (i.isdigit()):
			d += 1
		if (i == '@' or i == '$' or i == '#'):
			p += 1
if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s)):
	print("Valid Password")
else:
	print("Invalid Password")

import sys
def sliding_window(packets, n, m):
    packets = sorted(packets)
    i, j = 0, 0
    min_overall = 1000000
    j = m - 1
    start = 0
    end = j
    for i in range(0, n - m + 1):
        mini = 1000000
        mini = min(mini, packets[j] - packets[i])
        if (mini < min_overall):
            min_overall = mini
            start = i
            end = j
        j += 1
    for i in range(start, end + 1):
        print(packets[i], end=" ,")

    return min_overall



n = int(input("Enter the number of elements:- "))
packets=list(map(int,sys.stdin.readline().split()))

m = int(input("enter numner of student to distrubite"))
if m > n:
    print("no distribuition")
else:
    diff = sliding_window(packets, n, m)
print("\n")
print("Minimum Distance", diff)
l=[2,3,4,56]
setr={2,3,4,"a"}
dic={1:3,3:'c',5:'d'}
tuples=("shruti","jain","mits")
str="shrutijain"
print("list[]=,set{}=,dictionary={:},tuple()=,string""=".format(len(l) , len(setr) , len(dic) , len(tuples) , len(str)
'''
x="welcom to the python couse"
y="python prgramming used in the couse "
x_l=x.split(" ")
print(x_l)
y_l=y.split(" ")
r=[x1 for x1 in x_l for y1 in y_l if x1==y1]
print(r)
a="mathematics is essential in many fields"
xo=a.split(" ")
l=[elem[::-1] for elem in xo]
final=''
for elem in l:
    final+=elem+' '
print(final)
s="list is a mutable datatype, typically  used to stored homogenoues items"
x=list(s.lower())
print({char:x.count(char) for char in x if char.isalpha()})
sh="sundar"
st=sh.replace("a","e")
print(st)
import numpy as np
l=[1,2,34]
a=np.array(l)
print(a)
