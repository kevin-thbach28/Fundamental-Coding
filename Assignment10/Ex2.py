import requests

api_key = "572c311629417758b856ebeac87104a1"
city = input("Enter municipality name: ")

geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"

geo_response = requests.get(geo_url)
geo_data = geo_response.json()

if len(geo_data) > 0:
    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]

    print("Weather:", description)
    print("Temperature:", temperature, "°C")
else:
    print("City not found")