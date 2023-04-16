MAX_FULL = 100
class Car:
    def __init__(self, car_model, horse_power, hybrid):
        self.car_model = car_model
        self.horse_power = horse_power
        self.hybrid = hybrid
        self.fuel = MAX_FULL
        print('done')

# 1)
    def drive(self, c_km):
        if c_km * 5 <= self.fuel:
            self.fuel = self.fuel - c_km * 5
            print(f'drive was {c_km} no gas was needed and can go a nother {self.fuel / 5} KM')
        else:
            print(f'drive was {c_km} and gas is needed')
# 2)
    def refuel(self):
        self.fuel = 100


c = Car('Kia', 10000, False)
c.drive(3)
c.drive(5)
c.drive(5)

c.refuel()
c.drive(2)
c.drive(5)
c.drive(12)
