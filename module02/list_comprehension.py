numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]
odds = []
for val in numbers:
    if val&1 and val%5==0:
        odds.append(val)

print(odds)
# odd_nums = [num for num in numbers if num & 1 if num % 5 == 0] # upore j kaj korsi setai but ektu awkard lagche dekhte
# print(odd_nums)

players = ['Tamim', 'Sakib', 'Mustafiz']
ages = [38, 40, 32, 42, 36]

age_comb = []
for player in players:
    print('player: ', player)
    for age in ages:
        print(player, age)
        age_comb.append([player, age])

print(age_comb)
# age_comb2 = [[player, age] for player in players for age in ages] # uporer kaj tai short kore kora hoise
# print(age_comb2)

# so, comprehension means shortcut of longcut situation