#Task 1
class Country:
    def add(self, other_country):
        combined_name = self.name + ' ' + other_country.name
        combined_population = self.population + other_country.population
        new_country = Country()
        new_country.name = combined_name
        new_country.population = combined_population
        return new_country

bosnia = Country()
bosnia.name = 'Bosnia'
bosnia.population = 10_000_000

herzegovina = Country()
herzegovina.name = 'Herzegovina'
herzegovina.population = 5_000_000

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population) 
print(bosnia_herzegovina.name)       


#Task 2
class Country:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __add__(self, other_country):
        combined_name = self.name + ' ' + other_country.name
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)  
print(bosnia_herzegovina.name)        

#Task 3 
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):  
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

try:
    car1 = Car('Tesla', 'X', 2022)
    for i in range(2):
        car1.accelerate()  
    
    for i in range(1):
        car1.brake()  

    current_speed = car1.get_speed()
    
    if current_speed < 0:
        raise ValueError ("Speed should not be negative!")
    else:
        print(f"Car's current speed is: {current_speed}")

except ValueError as e:
    print(e)  



#Task 4
class Robot:
    def __init__(self, orientation='up', position_x=0, position_y=0):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        if self.orientation == 'up':
            self.position_y += steps
        elif self.orientation == 'down':
            self.position_y -= steps
        elif self.orientation == 'left':
            self.position_x -= steps
        elif self.orientation == 'right':
            self.position_x += steps

    def turn(self, direction):
        next_right = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
        next_left = {'up': 'left', 'left': 'down', 'down': 'right', 'right': 'up'}
        
        if direction == 'right':
            self.orientation = next_right[self.orientation]
        elif direction == 'left':
            self.orientation = next_left[self.orientation]

    def display_position(self):
        print(f"Position: ({self.position_x}, {self.position_y})")
        print(f"Orientation: {self.orientation}")

try:
    robot1 = Robot()
    robot1.move(5)
    assert (robot1.position_x, robot1.position_y) == (0, 5)
    print("Test 1 Passed: Correct movement.")
except AssertionError:
    print(f'Test 1 Failed: Robot should be at position {robot1.position_x, robot1.position_y} after moving.')

try:
    robot2 = Robot()
    robot2.turn('right')
    robot2.move(3)
    assert robot2.orientation == 'right'
    assert (robot2.position_x, robot2.position_y) == (3, 1)
    print("Test 2 Passed: Correct turn and movement.")
except AssertionError:
    print(f'Test 2 Failed: Robot should be at position {robot2.position_x, robot2.position_y} after moving {robot2.orientation}.')
