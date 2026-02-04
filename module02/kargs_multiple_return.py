def full_name(first, last):
    name = f'{first} {last}' # first + ' ' + last
    return name

# take parameters in order (serial wise)
# name = full_name('seemanto','dash')
# take parameter without serial
# name = full_name(last='dash', first='seemanto') # first and last diye priority bole deya hoise
# print(name)

def famous_name(first, title, **additional):
    name = f'{first} {title}'
    # print(additional['nickname'])
    # print(additional)
    for key, val in additional.items():
        print(key, val)
    return name

name = famous_name(first='seemanto', title='dash', nickname='shuvro', working_at='student')
print(name)

# def function_name(n1, n2, n3, *args, **kargs):

# multiple return
def a_lot(n1, n2):
    sum = n1 + n2
    sub = n2 - n1
    mul = n1 * n2
    div = n2/ n1
    # return [sum,sub,mul,div] # multiple return as a list
    return sum,sub,mul,div # multiple return as a tupple

everything = a_lot(3, 15)
print(everything)