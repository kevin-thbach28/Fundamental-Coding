numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    
    if user_input == "":
        break
    
    numbers.append(float(user_input))  # use float to allow decimals

numbers.sort(reverse=True)

print("Top 5 greatest numbers:")
for num in numbers[:5]:
    print(num)