class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, miles):
        self.mileage += miles

    def print(self):
        print(f"{self.year} {self.make} {self.model} with {self.mileage} miles")



v1 = Vehicle("Honda", "Accord", 2007, 100000)
v2 = Vehicle("Toyota", "Camry", 2008, 5000)
print(v1.make)
print(v1.model)
print(v1.year)
print(v1.mileage)

v1.drive(50)
print(v1.mileage)

v1.print()