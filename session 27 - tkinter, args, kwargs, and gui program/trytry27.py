def add(*args):
    # total = 0
    total = sum(args)
    print(total)

add(2, 3, 4, 5)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(3, add=3, multiply=5)

class Car():
    def __init__(self, **kw):
        # self.make = kw['make']
        # self.model = kw['model']
        self.make = kw.get('make')
        self.model = kw.get('model')

my_car = Car(make='nissan', model='gt-r')
print(my_car.model)

def test(*args):
    print(args)

print(test(1, 2, 3))