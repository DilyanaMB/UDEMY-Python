from animal import Animal

class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("move in water")

    def breathe(self):
        super().breathe()
        print("doing this under water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)