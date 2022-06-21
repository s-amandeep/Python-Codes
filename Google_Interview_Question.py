#Google Interview Question

#We are given an array of integers and a particular sum.
#We have to check if there are any two elements in the array that add up to the given sum.
#For example, array = [1,2,4,5] ,sum = 6
#This should return True as 2+4 = 6


# first solution that comes to mind, is to compare each element 

array = [1,3,4,7] 
sum = 8

# def checkArraySum(array, sum):

# 	for i in range(len(array)):
# 		for j in range(i+1, len(array)):
# 			if (array[i] + array[j] == sum):
# 				return True

# 	return False

#print(checkArraySum(array, sum))

# function checkArraySum has a time complexity of O(n^2) so we will try to do better than that
# We'll create Hash Maps (i.e. put the element of the arrays seen in a dictionary and check if compliments of the other elements
# of the array are present in dictionary)

def checkArraySum2(array, sum):

	maps = dict()

	for item in array:
		comp = sum - item

		if comp not in maps:
			maps[item] = 'True'
		else:
			return True

	return False

print(checkArraySum2(array, sum))

# Put Values in dictionary has time complexity of O(1) and for loop has time complexity of O(n) so the total time complexity if O(n)
# which is far better than the one seen before