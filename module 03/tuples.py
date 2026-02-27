# tuple -> first bracket ()
# list -> third bracket []
def multiple():
    return 3,4
# print(multiple())

things = 'pen', 'tripod', 'water bottle', 'charger', 'phone', 'web cam', 'calculator', 'sunglass'
# print(type(things))
# print(things[0])
# print(things[-2])
# print(things[3:6])

# if 'phone' in things:
#     print('exist')

# for item in things:
#     print(item)

# things[0] = 'notepad' # immutable -> you can not change it, but tuple jodi mutable jinis contain kore tahole change hoy... like tuple with array
# print(things)

# print(len(things))

mega = ([2,3,4,5], [6,8,9])
# print(type(mega))

# mega[0] = 3 # not change cz directly tuple is immutable
# but you can it
mega[0][1] = [1,2,3,4] # megar vitore thaka mutable array ke change kora jay
# print(mega)

# // visit documentation for better learning about tuple in python

# // what thing you cannot forget:
# tuple declare
# tuple print
# direct tuple not changeable but mutable with tuple is changeable