import requests

API_KEY = "42b1d7aaadcc0df3d3afbe0fc13d6bc2"  # Replace with your actual API key from OpenWeatherMap
city = input("Enter city name: ")

# Correct URL formatting
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Fetch data from OpenWeatherMap API
response = requests.get(url).json()

# Check if the request was successful
if response.get("cod") == 200:
    print(f"City: {response['name']}")
    print(f"Temperature: {response['main']['temp']}°C")
    print(f"Weather: {response['weather'][0]['description'].capitalize()}")
else:
    print("City not found!")
