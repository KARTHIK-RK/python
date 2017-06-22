def isomorphic(a,b):
        d={}
        flag=0
        l=len(a)
        for i in range(l):
                if a[i] not in d.keys():
                        d[a[i]]=b[i]
                else:
                        if(d[a[i]]!=b[i]):
                                flag=1
        if flag==0:
                return True
        else:
                return False		
a=input("enter the first word : ")
b=input("enter the second word : ")
print(isomorphic(a,b))
