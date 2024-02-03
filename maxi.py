#3 program to print maximum of three numbers
a=int(input("Enter Mark1:"))
b=int(input("Enter Mark2:"))
c=int(input("Enter Mark3:"))
if(a>b and a>c):
	print("Mark1 is the maximum number")
elif(b>a and b>c):
	print("Mark2 is the maximum number")
else:
	print("Mark3 is the maximum number")
