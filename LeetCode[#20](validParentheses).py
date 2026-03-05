a=input()
ans=True
l=[]
for i in range(len(a)):
    if a[i] in "([{":
        l.append(a[i])
    else:
        if l==[]:
            ans=False
        else:
            now=l.pop()
            if now=="(" and a[i]!=")":
                l=[]
                ans=False
                print("False")
                break
            elif now=="[" and a[i]!="]":
                l=[]
                ans=False
                print("False")
                break
            elif now=="{" and a[i]!="}":
                l=[]
                ans=False
                print("False")
                break
if l==[] and ans==True:
    print("True")
elif l!=[] and ans==True:
    print("False")