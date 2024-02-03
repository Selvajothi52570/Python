#4 program to print ticket price
age=int(input("Enter the age:"))
if(age<=5):
	print("The ticket is free")
elif(age>=6 and age<=12):
	print("The ticket price is $10")
elif(age>=13 and age<=18):
	print("The ticket price is $15")
elif(age>=19 and age<=60):
	print("The ticket price is $20")
else:
	print("The ticket price is $30")