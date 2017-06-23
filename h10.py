try:
        b=input().split()
        l1=[int(a) for a in b]
        b=input().split()
        l2=[int(a) for a in b]
        if (set(l1).issubset(l2)):
                print (True)
        else:
                print (False)
except:
        pass
