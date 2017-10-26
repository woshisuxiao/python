#类的学习 巩固

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year 
        self.odometer_reading=0


    def get_descriptive_name(self):
        '''返回长名'''
        long_name=str(self.year)+' '+self.make+'  '+self.model
        return long_name.title()

    def read_odometer(self):
        '''打印公里数'''
        print ("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileage):
        '''update odometer'''
        if mileage >=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print ("you can't roll back an odometer!")
    def increment_odometer(self,miles):
        '''累加'''
        self.odometer_reading +=miles

    def fill_gas_tank(self):
        pass




my_new_car=Car('audi','a4',2016)
print (my_new_car.get_descriptive_name())
#my_new_car.odometer_reading=23
print (my_new_car.year)
print (my_new_car.make)
print (my_new_car.model)

my_new_car.update_odometer(4)
my_new_car.read_odometer()

print ("\n"+"*"*30+"\n")

my_used_car=Car('subaru','outback',2013)
print (my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()


my_used_car.increment_odometer(100)
my_used_car.read_odometer()


print ("\n"+"*"*30+"\n")

suxiao_car=Car('大众','golf','2018')
print (suxiao_car.get_descriptive_name())

suxiao_car.update_odometer(1000)
suxiao_car.read_odometer()

suxiao_car.increment_odometer(50)
suxiao_car.read_odometer()


print ("\n"+"*"*30+"\n")

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print ("this Car has a " +str(self.battery_size)+"-KWH battery.")

    def get_range(self):
        if  self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270

        message="This car can go approximatley "+str(range)
        message+=" miles on a full charge."
        print (message)

class ElectriCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
        #self.battery_size=70

    #def describe_battery(self):
        '''about battery'''
    #    print ("this car has a " +str(self.battery_size)+".KWH battery.")

    def fill_gas_tank(self):
        print ("this car doesn't need a gas tank!")

        



my_tesla=ElectriCar('tesla','model_s',2017)
print (my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#my_tesla.fill_gas_tank()
