class vehicle:

    def __init__(self):
        self.brand = ""
        self.speed = 0
        self.mileage = 0

    def reset(self):
        self.mileage = 0

    def move(self,time):
        self.mileage = self.mileage + (self.speed * time)

class bus(vehicle):
    
    def __init__(self):
        vehicle.__init__(self)

        self.bus_number = ''
        self.seating_capacity = 0


if __name__ == '__main__':

    car = bus()
    car.bus_number = 'A01X'
    car.seating_capacity = 15
    car.speed = 30
    car.move(2)

    print('Bus Number ',car.bus_number)
    print('Mileage ',car.mileage)

    print()
    input('PRESS ANY KEY TO EXIT')
