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