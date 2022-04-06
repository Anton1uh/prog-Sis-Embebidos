class Vehicle:
    Color = None
    Wheels = None

    def __init__(self, color, wheels):
        self.Color = color
        self.Wheels = wheels

    def __str__(self): ## \n salto de linea --> alt+92 = \
        return f'Color: {self.Color}  \nLlantas: {self.Wheels} \n'

    def travel(self):
        print("Ha viajado el auto")

Vehicle1 = Vehicle('Blanco','5 Repuesto')
print(Vehicle1)
Vehicle1.travel()


class Bicycle(Vehicle):
    saddles = None
    chain_drive = None

    def __init__(self, color,wheels,saddles,chain):
        Vehicle.__init__(self, color, wheels)
        self.saddles = saddles
        self.chain_drive = chain

    def __str__(self): ## \n salto de linea --> alt+92 = \
        return f'Saddles: {self.saddles}  \nChainDrive: {self.chain_drive} \n'

    def Start(self):
        print("Ha iniciado marcha")

    def Accerelate(self):
        print("Comenzó a acelerar")



Bicycle1 = Bicycle('Rojo','2','BMX','BMXPRO')
print(Bicycle1)
Bicycle1.Start()
Bicycle1.Accerelate()


class Car(Vehicle):
    seats = None
    engine = None

    def __init__(self, color, wheels, seats, engine):
        Vehicle.__init__(self, color, wheels)
        self.seats = seats
        self.engine = engine

    def __str__(self):  ## \n salto de linea --> alt+92 = \
        return f'Seats: {self.seats}  \nEngine: {self.engine} \n'

    def Start(self):
        print("Ha iniciado marcha (auto)")

    def Accerelate(self):
        print("Comenzó a acelerar (auto)")

Car1 = Car('Verde','6','SPARCO','Twin-turbo V6')
print(Car1)
Car1.Start()
Car1.Accerelate()