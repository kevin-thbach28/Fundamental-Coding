class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moving up: now at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moving down: now at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        print(f"\nGoing to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
            
class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for i in range(num_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, target_floor):
        print(f"\nRunning elevator {elevator_number} to floor {target_floor}")
        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\nFIRE ALARM! All elevators going to bottom floor")
        for i, elevator in enumerate(self.elevators):
            print(f"\nElevator {i} returning to bottom floor")
            elevator.go_to_floor(self.bottom_floor)
            
building = Building(0, 10, 3)

building.run_elevator(0, 5)
building.run_elevator(1, 7)
building.run_elevator(2, 3)

building.run_elevator(0, 0)

building.fire_alarm()