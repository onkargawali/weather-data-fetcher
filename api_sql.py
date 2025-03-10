import mysql.connector
import requests
import datetime

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",       # Change to your MySQL host
    user="root",   # Replace with your MySQL username
    password="root", # Replace with your MySQL password
    database="onkar"
)


cursor = db.cursor()

# OpenWeatherMap API Configuration
API_KEY = "97c4b1b2ff031de5922d3672817e1b99"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


# Function to fetch weather data
def fetch_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather_desc": data["weather"][0]["description"],
            "date_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return weather_info
    else:
        print(f"Failed to fetch data for {city}: {response.text}")
        return None

# Function to store data into MySQL
def save_to_mysql(data):
    sql = """INSERT INTO weather (city, temperature, humidity, weather_desc, date_time)
             VALUES (%s, %s, %s, %s, %s)"""
    values = (data["city"], data["temperature"], data["humidity"], data["weather_desc"], data["date_time"])
    
    cursor.execute(sql, values)
    db.commit()
    print(f"Weather data for {data['city']} stored in MySQL.")

# Main Execution
if __name__ == "__main__":
    cities = ["New York", "Los Angeles", "Chicago", "Miami", "London"]

    for city in cities:
        weather_data = fetch_weather(city)
        if weather_data:
            save_to_mysql(weather_data)

    print("All weather data saved to MySQL.")
    cursor.close()
    db.close()

