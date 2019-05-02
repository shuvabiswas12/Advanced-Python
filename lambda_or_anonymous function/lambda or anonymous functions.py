
# lambda functions or anonymous function

#
# def minus(x, y):
#     return x-y


# lambda functions ...

# the minus function can be written in one line as below using lambda function
minus = lambda x, y: x-y

print(minus(2, 9))


# ...

def a_first(a):
    return a[1]


a = [[1, 14], [5, 6], [8, 23]]
# a.sort(key=a_first)  # this line can be written as bellow
a.sort(key=lambda x: x[1])
print(a)

