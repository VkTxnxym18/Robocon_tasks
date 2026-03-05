n=int(input())
l=[0,1,0]
result=[]
for i in range(n):
    g=[]
    for i in range(len(l)-1):
        g.append(l[i]+l[i+1])
    l=g.copy()
    l.insert(0,0)
    l.insert(-1,0)
    g.pop()
    result.append(g)
print(result)