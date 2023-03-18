class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")
        
    # adding extra value
    def breathe(self):
        super().breathe()
        print("doing this under water")
Fish().breathe()
nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breathe()
