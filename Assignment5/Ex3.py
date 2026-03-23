cities = []

for i in range(5):
    city = input(f"Enter city {i+1}: ")
    cities.append(city)

print("Cities you entered:")
for city in cities:
    print(city)