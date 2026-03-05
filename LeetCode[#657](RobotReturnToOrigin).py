moves=input()
c=[0,0]
for i in moves:
    if i=="U":
        c[1]+=1
    elif i=="D":
        c[1]-=1
    elif i=="R":
        c[0]+=1
    elif i=="L":
        c[0]-=1
if c==[0,0]:
    print("True")
else:
    print("False")
