a = int(input("Enter starting point : "))
b = int(input("Enter ending point : "))

print("Prime numbers in between {} to {}".format(a,b))
for n in range(a,b+1):
	if n>1:
		for i in range(2,n):
			if n % i == 0:
				break
		else:
			print(n)