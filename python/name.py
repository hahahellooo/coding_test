def func1():
    print("myfunc1")

if __name__ == "__main__":
    print("name.py has run directly")
else:
    func1()
    print("name.py has imported")