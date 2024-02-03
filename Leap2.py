#1 program to check leap year
year=int(input("Enter the Year:"))
if(year%4==0):
	print("The Entered year is a leap year")
elif(year%100==0):
	print("The Entered year is not a leap year")
elif(year%400==0):
	print("The Enter year is a leap year")
else:
	print("The Entered year is not a leap year")