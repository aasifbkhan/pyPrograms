#Find the Element in the list
list = []
n = int(input("How Many Elements You Want To Enter In The List : "))
print("Enter Element in the list : ")
for i in range(n):
	a = int(input())
	list.append(a)
print("List = ",list)
l = int(input("Enter Number to search : "))
for i in list:
	if i == l:
		print("The Element is found at index",list.index(i))
		break
	else:
		print("Sorry Element not found...!!!")
		break