def fact(n):
	if n==0:
		return 1
	else:
		return (fact(n-1)*n)
try:
        x=int(input("enter the number : "))
        print(fact(x))
except:
        print("enter the input as positive integer")
