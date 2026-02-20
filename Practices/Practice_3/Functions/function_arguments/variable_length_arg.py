def add(*numbers): #*args
    print(sum(numbers))

add(1, 2, 3, 4)

def info(**data): #**kwargs
    print(data)

info(name="Ali", age=20)