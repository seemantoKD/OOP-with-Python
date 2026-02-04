numbers = [12, 45, 68, 98]
numbers.append(56) # push_back
# print(numbers)

numbers.insert(2, 71) # insert at ith index
# print(numbers)

if 98 in numbers:
    numbers.remove(98) # remove value from list
# print(numbers)

last = numbers.pop() # last theke pop
# print(last)
# print(numbers) # 56 remove

index = numbers.index(71) # return index of a value, if value nai, then shown to you: 'value is not in list'
# print(index)

numbers.sort()
# print(numbers)

numbers.reverse()
# print(numbers)