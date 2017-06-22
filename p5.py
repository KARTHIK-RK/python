try:
        rom=input("enter the roman number : ")
        num1={"CM":900,"CD":400,"XC":90,"XL":40,"IX":9,"IV":4}
        num2={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        l=len(rom)
        ans=0
        while(l>0):
                if rom[l-2:] in num1.keys():
                        ans=ans+num1[rom[l-2:]]
                        rom=rom[:l-2]
                        l=l-2
                else:
                        ans=ans+num2[rom[l-1:]]
                        rom=rom[:l-1]
                        l=l-1
        print (ans)
except:
        print("entered string is not a roman number")
