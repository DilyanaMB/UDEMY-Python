# *args (or params might be named any way you want) allows sending whatever number of params
def add(*args):
    # we can access any value in args by index, since it's saving it as a tuple
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5,6))
print(add(1,2))

def calculater(n,**kwargs):
    n+=kwargs['add']
    n*=kwargs['multiply']
    return n

print(calculater(2,add=3, multiply=5))


class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        # if at initializing use .get() instead of taking by its key, then in case of missing that argument
        # upon creating the object you want get an error, instead it will be created as None
        self.model = kw.get('model')

my_car = Car(make='Lamborghini', model='Huracane')
print(my_car.make, my_car.model)

my_ferrari = Car(make='Ferrari')
print(my_ferrari.model)