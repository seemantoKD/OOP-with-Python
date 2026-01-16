# +=, -=, *=, /=
# a = 7
# a = a + 5
# a += 5
# print(a)

# in, not, not in, is, is not
# and, or
# a = 5
# if a>8:
#     print('5 er beshi')
#     print('koto beshi k jane')
# elif a == 5:
#     print('5 er soman')
# else:
#     print('5 er kom')
#     print('koto kom k jane')

# boss = False
# if boss is not True:
#     print('tel niye astesi boss')
# else:
#     print('lunch pore asen')

# nested conditions
coin = 'head'
boss = True
if boss == True:
    print('You are joss')
    if coin == 'tail':
        print('batting')
    else:
        print('bowling')
        if 5 > 2 or boss != True:
            print('do something')
            if 8%2==0 and 5%2==1:
                print('Even 8 is an even number')
else:
    print('You are loss not a boss')