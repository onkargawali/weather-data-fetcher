import requests
import csv
import datetime



# Set up your API key and base URL (Use OpenWeatherMap as an example)
API_KEY = "97c4b1b2ff031de5922d3672817e1b99"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
# BASE_URL = "https://home.openweathermap.org/api_keys"



# Function to fetch weather data
def fetch_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "City": city,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"],
            "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return weather_info
    else:
        print("Failed to fetch data:", response.json())
        return None



# Function to save data to CSV
def save_to_csv(data, filename="weather_data.csv"):
    file_exists = False
    try:
        with open(filename, "r") as f:
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()  # Write headers if file is new
        writer.writerow(data)




# Main execution
# if __name__ == "__main__":
#     cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami","London", "Paris", "Berlin", "Madrid", "Rome","Tokyo", "Beijing", "Seoul", "Bangkok", "Mumbai","Sydney", "Toronto", "Dubai", "Moscow", "Cape Town"]

# # city = input("Enter city name: ")
#     for city in cities:
#         weather_data = fetch_weather(city)
#         if weather_data:
#             save_to_csv(weather_data)
#             print("Weather data saved successfully!")

#     print("All weather data saved successfully!")

    
if __name__ == "__main__":
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami","London", "Paris", "Berlin", "Madrid", "Rome","Tokyo", "Beijing", "Seoul", "Bangkok", "Mumbai","Sydney", "Toronto", "Dubai", "Moscow", "Cape Town"]

    for city in cities:
        weather_data = fetch_weather(city)  # Pass a single city
        if weather_data:
            save_to_csv(weather_data)
            print(f"Weather data for {city} saved successfully!")

    print("All weather data saved successfully!")



