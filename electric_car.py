class Car():
    """汽车父类"""
    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas = 20

    def get_descriptive_name(self):
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def fill_gas_tank(self,gas):
        self.gas +=gas


class ElectricCar(Car):
    """电动汽车，继承自汽车类"""
    def __init__(self, make,model,year):
        """初始化父类属性"""
        super().__init__(make,model,year)
        """私有的电池属性"""
        self.battery = Battery()

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")

    def fill_gas_tank(self,gas):
        """重写父类方法"""
        print("This car doesn't need a gas tank!")


class Battery():
    """电池类"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
        
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately "+str(range)
        message += " miles on a full charge."
        print(message)


        
my_tesla = ElectricCar('tesla','model s','2016')
print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()
#my_tesla.fill_gas_tank(10)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
        
        