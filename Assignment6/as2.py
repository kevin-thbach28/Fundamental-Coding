seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of a month (1-12): "))

if month in (12, 1, 2):
    season = seasons[0]
elif month in (3, 4, 5):
    season = seasons[1]
elif month in (6, 7, 8):
    season = seasons[2]
elif month in (9, 10, 11):
    season = seasons[3]
else:
    season = "Invalid month"

print("Season:", season)