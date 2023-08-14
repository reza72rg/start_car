class Car:
    cars_number = 0  # Class attribute to keep track of the number of cars created

    def __init__(self, name):
        self.name = name  # Instance attribute to store the name of the car
        self._status = False  # Private attribute to store the status of the car (on/off)
        self._moving = False  # Private attribute to store the moving status of the car
        Car.cars_number += 1  # Increment the cars_number attribute each time a car is created

    @property
    def status(self):
        return self._status  # Property to access the private _status attribute

    @property
    def moving(self):
        return self._moving  # Property to access the private _moving attribute

    def start(self):
        if not self.status:  # If the car is not already started
            print(f'{self.name} is starting')
            self._status = True  # Set the status of the car to True (started)
        elif self.moving:  # If the car is already moving
            print('The car is moving, do not start!')
        else:
            print(f'{self.name} is already started, do not start again')

    def off(self):
        if self.status and not self.moving:  # If the car is started and not moving
            print(f'{self.name} is off')
            self._status = False  # Set the status of the car to False (off)
        elif self.moving:  # If the car is moving
            print('Your car is moving, cannot turn off')
        else:
            print(f'{self.name} is already off, please start first')

    def move(self):
        if self.status and not self.moving:  # If the car is started and not moving
            print(f'{self.name} is moving')
            self._moving = True  # Set the moving status of the car to True
        elif self.moving:  # If the car is already moving
            print('Your car is already moving')
        else:
            print(f'{self.name} is off, please start first and then move')

    def stop(self):
        if self.moving:  # If the car is moving
            print('Your car has stopped, please be careful')
            self._moving = False  # Set the moving status of the car to False
        elif not self.status:  # If the car is off
            print('Your car is off, what do you mean?')
        else:
            print('You must start moving first')


car1 = Car('bmw')  # Create a new instance of the Car class with name 'bmw'
car2 = Car('benz')  # Create another instance of the Car class with name 'benz'
