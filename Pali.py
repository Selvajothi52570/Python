#program to check palindrome
string=input("Enter the Name:")
if (string==string[::-1] ):
	print("The String is Palindrome")
else:
	print("The String is not Palindrome")