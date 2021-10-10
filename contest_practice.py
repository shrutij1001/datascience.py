'''import sys
T=int(input(""))
D , d , P , Q=0,0,0,0
for i in range(T):
    D , d , P , Q =map(int,sys.stdin.readline().split())
    n=D//d
    rem=D%d
    sum=n*P*d+(n*(n-1))/2*Q*d+(P+n*Q)*rem
    print(int(sum))
#bubble sort'''
'''al=list(input(""))
n=len(al)
for i in range(n):
    print(i)
    for j in range(0,n-i-1):
        print(j)
        if al[j]>al[j+1]:
            al[j],al[j+1]=al[j+1],al[j]
    print(al)
#insertion sort
ar=list(input())
ni=len(ar)
for i in range(1,ni):
   key=ar[i]
    j=i-1
    while j>=0 and key<ar[j]:
        ar[j+1]=ar[j]
        j=j-1
    else:
        ar[j+1]=key
print(ar)
l=input("").split()
sr=""
for i in range(len(l)):
    sr+=l[i].capitalize()+" "
print(sr)
dic={}
dic[1]=1
dic['1']=2
dic[1.0]=4
print(dic)
dic={1: 4, '1': 2,1.0:7 }
sum=0
for k in dic:
    sum+=dic[k]
    print(sum)
print(sum)
box = {}

jars = {}

crates = {}

box['biscuit'] = 1

box['cake'] = 3

jars['jam'] = 4

crates [ 'box'] = box

crates ['jars'] = jars
print (crates[box])'''

import math
import os
import random
import re
import sys


#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sum=(arr[0][1]+arr[1][1]+arr[2][2])-(arr[2][0]+arr[1][1]+arr[2][0])
    return abs(sum)
A
if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)



