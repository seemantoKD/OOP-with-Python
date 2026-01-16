# break and continue with while loop
# num = 1
# while num <= 10:
#     if num == 5:
#         num += 1
#         continue # skip 5
#     print(num, end=" ")
#     num += 1
#     if num == 9:
#         break # stop loop

num = 1
while num <= 10:
    if num % 2 == 0:
        print(num, end=" ")
        num += 1
    else:
        num += 1
        continue