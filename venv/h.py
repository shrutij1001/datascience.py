'''from sys import stdin
vo="aeiouaeiouaeiou"
con="bcdfghjklmnpqrstvwxyz"
v=list(vo)
c=list(con)
nw=""
s=list(map(str,stdin.readline()))
w=len(s)-1
i=0
while i<=w:
    if s[i] in v:
        for j in range(4):
            if s[i]==v[j]:
                nw+=c[j]
            j+=1
    else:
        for j in range(21):
            if s[i]==c[j]:
                nw+=v[j]
            j+=1
    i+=1
print(nw)'''
inp=" "
while len(inp)<=4:
    if inp[-1]=="z":
        inp=inp[0:3]+"c"
    elif 'a' in inp:
        inp=inp[0]+"bb"
    elif not int(inp[0]):
        inp="1"+inp[1:]+"z"
    else:
        inp=inp+"*"
print(inp)













