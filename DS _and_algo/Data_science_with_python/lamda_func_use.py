# Uses of Lambda function for higher order function

# 1. Sorting :-  points based on second element of each tuple
points = [(4,5),(3,4),(4,6),(0,2),(6,7),(8,9)]
sorted_points = sorted(points,key= lambda x:x[1])
print(sorted_points)

# 2. Filter:- odd numbers out of list
numbers = [2,5,6,3,5,22,4,56,7,8,43,545,665,20,12,14,16,18,24,26,45,65,66]
even_numbers = list(filter(lambda x:x%2 != 0, numbers))
print(even_numbers)

# 3. Mapping :- Applying a function to all items e.g - calculating squares of all numbers in list
nums = [5, 6, 7, 8, 9 , 10]
squares = list(map(lambda x:x**2,nums))
print(squares)