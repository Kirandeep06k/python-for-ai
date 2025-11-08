import requests

# # We need coordinates to get weather data
# latitude = 48.85   # Paris latitude
# longitude = 2.35   # Paris longitude

# # Build the API URL with our parameters
# url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# # Make the request
# response = requests.get(url)
# data = response.json()
# print(data)
# temperature = data['current']['temperature_2m']
# print(f"Temperature in Paris: {temperature}°C")
# data.keys()
# data.values()

#API--------------------------------------
# def get_weather(latitude, longitude):
#     response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
#     data = response.json()
#     return data['current']['temperature_2m']

# # Get temperature for different cities
# paris_temp = get_weather(48.85, 2.35)
# london_temp = get_weather(51.50, -0.12)
# tokyo_temp = get_weather(35.68, 139.69)

# print(f"Paris: {paris_temp}°C")
# print(f"London: {london_temp}°C")
# print(f"Tokyo: {tokyo_temp}°C")

#clean code
# def get_weather(latitude, longitude, fields="temperature_2m"):
#     response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current={fields}")
#     data = response.json()
#     return data['current'][fields]

# print(f"Paris: {paris_temp}°C")
# print(f"London: {london_temp}°C")
# print(f"Tokyo: {tokyo_temp}°C")


#GPT
import pandas as pd

cities = {
    "Paris": (48.85, 2.35),
    "London": (51.50, -0.12),
    "Tokyo": (35.68, 139.69)
}

data_list = []
#.items() gives a list of key-value pairs:
for city, (lat, lon) in cities.items():
    temp = get_weather(lat, lon)
    data_list.append({"city": city, "temperature": temp})

df = pd.DataFrame(data_list)
print(df)


