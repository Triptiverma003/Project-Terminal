class Vehicle:
    def __init__(self , make , model):
        self.make = make
        self.model = model
    def moves(self):
        print("Moves along..")
    def get_make_model(self):
        print(f"I am {self.make} {self.model}.")
        
my_car = Vehicle('Tesla' , 'Model 3')
#print(my_car.make)
#print(my_car.model)
my_car.get_make_model()
my_car.moves()

class Airplane(Vehicle):
    def moves(self):
        print('Flies along..')
class Truck (Vehicle):
    def moves(self):
        print('Rumbles along...')
class GolfCart(Vehicle):
    pass

indigo = Airplane('Indigo' , 'AirLines')
truck = Truck('Yamaha' , 'mini')
golfstar = GolfCart('cessna' , 'skyhawk')

indigo.get_make_model()
indigo.moves()

truck.get_make_model()
truck.moves()

golfstar.get_make_model()
golfstar.moves()


print('\n\n')

for v in (my_car , indigo , truck , golfstar):
    v.get_make_model()
    v.moves()