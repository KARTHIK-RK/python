t1=input("enter the time in HH:MM format : ")
t2=input("enter the time in HH:MM format : ")
k1=t1.split(":")
k2=t2.split(":")
l1=[int(a) for a in k1]
l2=[int(a) for a in k2]
if(l1[0]>l2[0]):
	pass
elif(l1[0]<l2[0]):
	l1,l2=l2,l1
else:
	if(l1[1]>l2[1]):
		pass
	else:
		l2,l1=l1,l2
if(l1[1]<l2[1]):
	l1[1]+=60
	l1[0]=l1[0]-1
print ((l1[0]-l2[0])*60+(l1[1]-l2[1]))
