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



cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = 150 + i * 5   
    cars.append(Car(reg_number, max_speed))



acceleration_pattern = [10, 15, -5, 20, -10]

race_finished = False
hours_passed = 0

while not race_finished:
    hours_passed += 1

    for i, car in enumerate(cars):
        change = acceleration_pattern[hours_passed % len(acceleration_pattern)]
        car.accelerate(change)

        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True


print("\nRace finished!\n")
print(f"Total hours: {hours_passed}\n")

print(f"{'Reg Number':<10} {'Max Speed':<10} {'Speed':<10} {'Distance':<15}")
print("-" * 50)

for car in cars:
    print(f"{car.registration_number:<10} {car.max_speed:<10} {car.current_speed:<10} {car.travelled_distance:<15.2f}")