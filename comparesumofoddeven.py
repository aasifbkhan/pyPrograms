#Comparison between sum of odd and even number.
list = input("Enter List Element : ").split()
list1= []
list2 = []
sum = 0
sum1 = 0
for i in list:
	i = int(i)
	if i % 2 == 0:
		list1.append(i)
		sum = sum + i
	else:
		list2.append(i)
		sum1 = sum1 + i
print("Odd list = ",list1,"and Sum = ",sum,"\nEven list = ",list2,"and Sum = ",sum1)
if sum > sum1:
	print("The Odd number {} is greater than Even number {}".format(sum,sum1))
elif sum == sum1:
	print("The Odd number {} and Even number {} are equal".format(sum,sum1))
else:
	print("The Odd number {} is smaller than Even number {}".format(sum,sum1))