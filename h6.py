try:
        def firstRep(l):
                d={}
                for i in l:
                        if i in d.keys():
                                return i
                        else:
                                d[i]=1
        b=input().split()
        a=[int(i) for i in b]
        print(firstRep(a))
except:
        pass
