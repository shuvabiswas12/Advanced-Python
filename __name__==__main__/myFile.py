def func():
    print("func() From myFile.py")


print("top level execution on myFile.py")

if __name__ == "__main__":
    print("Direct execution from myFile.py")
else:
    print("imported into another file")
