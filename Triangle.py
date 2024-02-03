#program to print triangle equilateral,isosceles or a scalene triangle
side1=int(input("Enter the side1:"))
side2=int(input("Enter the side2:"))
side3=int(input("Enter tge side3:"))
if(side1==side2==side3):
	print("It is a Equilateral Triangle")
elif(side1==side2 or side2==side3 or side3==side1):
    print("It is a Isosceles Triangle")
else:
	print("It is a Scalene Triangle")