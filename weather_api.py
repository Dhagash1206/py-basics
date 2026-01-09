import requests

API_KEY = # add API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        print(f"Error: {data.get('message', 'Failed to fetch weather data')}")
        return

    city_name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"\n🌍 City: {city_name}")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁️ Condition: {description}\n")

if __name__ == "__main__":
    while True:
        city = input("Enter a city name ").strip()
        get_weather(city)
        break
