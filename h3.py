try:
        def fn(l):
                l.sort()
                for i in range(len(l)):
                        if l[i]==i:
                                print (l[i],end=" ")
        b=input().split()
        a=[int(i) for i in b]
        fn(a)
except:
        print("invalid input")
