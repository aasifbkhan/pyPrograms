#sum of digit number
a = int(input("Enter the numbers : "))
sum = 0
while a>0:
	n = a % 10
	sum = sum + n
	a = a // 10
print("Sum of digits = ",sum)	