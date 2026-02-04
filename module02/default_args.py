# function call er parameter a mismatch hoile evabe n3 = 0 dile error dey na python
# python egulare optional dore ney, thakle o kichu na, na thakle o kichu na... 
# tobe call parameter jotota toto ta parameter er kom thakle error dibe
# def sum (n1, n2, n3 = 0, n4 = 0, n5 = 0):
#     result = n1 + n2
#     return result

# total = sum(99, 11) # function call kora hoice duita diye
# print('total: ',total)

# args
def all_sum(n1, n2, *numbers):
    print(numbers)
    sum = 0
    for val in numbers:
        print(val, end=' ')
        sum += val
    return sum

total = all_sum(45, 56, 86, 89)
print()
print('all sum: ', total)