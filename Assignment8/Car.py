import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\n🏁 {self.name} Status")
        print(f"{'Reg Number':<10} {'Max Speed':<10} {'Speed':<10} {'Distance':<15}")
        print("-" * 50)

        for car in self.cars:
            print(f"{car.registration_number:<10} {car.max_speed:<10} {car.current_speed:<10} {car.travelled_distance:<15.2f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance_km:
                return True
        return False


cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg_number, max_speed))

# Create race
race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

# Race loop
while not race.race_finished():
    hours += 1
    race.hour_passes()

    # Print every 10 hours
    if hours % 10 == 0:
        race.print_status()

# Final status
race.print_status()

print(f"\nRace finished in {hours} hours!")