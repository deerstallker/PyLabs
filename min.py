
A = [3,4,2,1,0,8,9,-1,100,0]
min = A.pop()
while A:
    a = A.pop()
    if a < min:
        min = a
print(min)
