import requests 

def get_weather(city_name, api_key):
    url= "https://api.openweathermap.org/data/2.5/weather?"
    params = {
        "q" : city_name,
        "appid" : api_key,
        "unit" : "metric"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(weather_data):
    """
    Displays formatted weather information to the console.
    """
    if weather_data:
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        print(f"\n--- Current Weather in {city} ---")
        print(f"Temperature: {temperature}°C")
        print(f"Conditions: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Could not retrieve weather information.")

if __name__ == "__main__":
    appid = "f88c295e5c0a7255b6c8b3e45c410ee1"  

    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            break

        if not city:
            print("City name cannot be empty. Please try again.")
            continue

        weather_info = get_weather(city, appid)
        display_weather(weather_info)