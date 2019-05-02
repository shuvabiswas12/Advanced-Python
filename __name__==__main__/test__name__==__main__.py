import myFile


def func():
    print("func() From test__name__==__main__.py")


print("top level execution on test__name__==__main__.py")
myFile.func()

if __name__ == "__main__":
    print("Direct execution from test__name__==__main__.py")
else:
    print("imported into another file")
