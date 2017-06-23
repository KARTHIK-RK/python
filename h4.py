try:
        def findUnique(l):
                d={}
                for i in l:
                        if i in d.keys():
                                d[i]=d[i]+1
                        else:
                                d[i]=1
                for i in d.keys():
                        if d[i]==1:
                                return i
        b=input().split()
        a=[int(i) for i in b]
        print(findUnique(a))
except:
        pass
