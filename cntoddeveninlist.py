#count the odd & even number in the list
list = input("Enter integer elements : ").split()
print("List : ",list)
list1 = []
list2 = []
for i in list:
	i = int(i)
	if i % 2 != 0:
		list1.append(i)
	else:
		list2.append(i)
print("Total number of odd element in list = {}".format(len(list1)),"\nTotal number of even element in list = {}".format(len(list2)))