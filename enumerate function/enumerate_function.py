
lst = [100, 200, 400]

i = 0
for item in lst:
    if i%2 == 0:
        print(i, '', item)
    i = i + 1


for index, item in enumerate(lst):
    if index%2 == 0:
        print(index, item)


# note:- enumerate() function returns index as well as items at a time
