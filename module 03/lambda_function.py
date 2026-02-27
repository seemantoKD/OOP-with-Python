# def doubled(x):
#     return x*2

# function_name = lambda parameter1, parameter2 : returning_value
doubled = lambda num : num * 2
# squared = lambda num : num * num
# add = lambda n1, n2 : n1 + n2

# result = doubled(5)
# print(result)

# result = squared(5)
# print(result)

# result = add(5,4)
# print(result)

numbers = [12, 56, 98, 78, 56, 12, 6, 98]
# print(numbers)
# doubled_nums = map(doubled, numbers)
# doubled_nums = map(lambda x : x * 2, numbers)
squared_nums = map(lambda x : x * x, numbers)
# print(list(doubled_nums))
# print(list(squared_nums))


actors = [
    {'name': 'sabana', 'age': 55},
    {'name': 'sabnur', 'age': 46},
    {'name': 'purnima', 'age': 38},
    {'name': 'shrabonty', 'age': 28},
]

juniors = filter(lambda actor : actor['age'] < 40, actors)
print(list(juniors))