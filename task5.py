import requests

def get_weather(api_key, user_input):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    if user_input.isdigit():
        params = {"zip": user_input}
    else:
        params = {"q": user_input}
    params["units"] = "metric"
    params["appid"] = api_key


    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(weather_data):
    if weather_data is None:
        return

    temperature = weather_data.get("main", {}).get("temp")
    humidity = weather_data.get("main", {}).get("humidity")
    wind_speed = weather_data.get("wind", {}).get("speed")
    description = weather_data.get("weather", [])[0].get("description")

    print("Current Weather:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {description}")

def main():
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    user_input = input("Enter the name of a city or a zip code: ")

    # Pass base_url as an argument to the get_weather function
    weather_data = get_weather(api_key, user_input)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
