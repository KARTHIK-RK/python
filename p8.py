x=input("enter the string : ")
l=x.split(" ")
k=[a[0].upper()+a[1:] for a in l]
print (" ".join(k))
