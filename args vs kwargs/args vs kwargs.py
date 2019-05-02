
# args is a tuple and kwargs is a dictionary
# args is also called a variable arguments

# reference link: https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/


# *args

args = ("I", "II", "III")
print(*args)


def func1(*args):
    print(type(args))


func1(args)


#
# **kwargs

def func2(**kwargs):
    print(type(kwargs))


func2(Name='Class', Roll=116, Class='XII')



def test_arguments(args1, args2, args3):
    print("args1: ", args1)
    print("args2: ", args2)
    print("args3: ", args3)


args1, args2, args3 = {"args1": 'Class', "args3": 116, "args2": 'XII'}

args = {"args1": 'Class', "args3": 116, "args2": 'XII'}

test_arguments(**args)

print(args1)
print(args2)
print(args3)






