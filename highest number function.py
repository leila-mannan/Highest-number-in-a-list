def find_highest(list):
	if len(list) == 1:
		return list[0]
	else:
		if list[0] < list[1]:
			list.pop(0)
		else:
			list.pop(1)
		return find_highest(list)
#example of calling the function
numList = [1,2,20,90,40,3,1,7,4]
print(find_highest(numList))
