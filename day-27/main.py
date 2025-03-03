def add(*args):
    print(args)
    print(type(args))

add(1,2,3,"h",5)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=2,multiply=5)