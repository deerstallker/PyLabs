s=input()
s1=""
i=0
for c in s:
    if c=='x':
        c='y'
        i+=1
    if c=='X':
        c='Y'
        i+=1
    s1+=c
print(s1)
print(i)

