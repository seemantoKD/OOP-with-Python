# list --> []
# tuple --> ()
# set --> {}

# set means collection of an uniqueness but not maintain order
numbers = [12, 56, 98, 78, 56, 12, 6, 98]
numbers_set = set(numbers)
# print(numbers_set)
numbers_set.add(55)
# print(numbers_set)
numbers_set.remove(6)
# print(numbers_set)

# add remove possible in set but positioning is not possible
# numbers_set[1] = 5 # not possible

# for item in numbers_set:
#     print(item)

# if 9 in numbers_set:
#     print('9 exists')
# else:
#     print('not exists')

# set method --> please check official documentation

A = {1, 3, 5}
B = {1, 2, 3, 4, 5}
# print(A & B) # common between A and B set
# print(A | B) # sob gula but not duplicate

# notes:
# i. mutable & unique
# ii. add remove possible
# iii. position is not indexable