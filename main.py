import requests
import os
import json

# Load weathercode data for weather icons
with open("weathercode.json") as file:
    weathercode_data = file.read()
weathercode_data = json.loads(weathercode_data)

# OpenMeteo API call for weather data in Danville, CA
om_params = {
    "latitude": "37.822578",
    "longitude": "-122.000839",
    "hourly": "temperature_2m,precipitation,weathercode",
    "daily": "weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,showers_sum,precipitation_hours,precipitation_probability_max,windspeed_10m_max",
    "temperature_unit": "fahrenheit",
    "windspeed_unit": "mph",
    "precipitation_unit": "inch",
    "timezone": "PST",
    "forecast_days": "1"
}

# OpenMeteo API call for weather data in Fort Lauderdale, FL
test_om_params = {
    "latitude": "26.1224",
    "longitude": "-80.1373",
    "hourly": "temperature_2m,precipitation,weathercode",
    "daily": "weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum,rain_sum,showers_sum,precipitation_hours,precipitation_probability_max,windspeed_10m_max",
    "temperature_unit": "fahrenheit",
    "windspeed_unit": "mph",
    "precipitation_unit": "inch",
    "timezone": "PST",
    "forecast_days": "1"
}

OM_ENDPOINT = "https://api.open-meteo.com/v1/forecast?"

# Request weather data from OpenMeteo
response = requests.get(OM_ENDPOINT, params=om_params)
# response = requests.get(OM_ENDPOINT, params=test_om_params)
response.raise_for_status()
weather_data = response.json()

# print(weather_data)

# Slice weather data to get hourly weathercode
weathercode_slice = weather_data["hourly"]["weathercode"][6:18]

# Slice weather data to get daily weathercode
daily_weathercode = weather_data["daily"]["weathercode"][0]

# Slice weather data to get daily max temp
daily_max = weather_data["daily"]["temperature_2m_max"][0]

# Slice weather data to get daily min temp
daily_min = weather_data["daily"]["temperature_2m_min"][0]

# Slice weather data to get daily precipitation probability
daily_precip_prob = weather_data["daily"]["precipitation_probability_max"][0]

# Slice weather data to get daily wind speed
daily_wind = weather_data["daily"]["windspeed_10m_max"][0]

# Get weathercode image
weathercode_image = weathercode_data[str(daily_weathercode)]["day"]["image"]

# Print weather data
daily_weather = {
    "weathercode": daily_weathercode,
    "image": weathercode_image,
    "max": daily_max,
    "min": daily_min,
    "precip_prob": daily_precip_prob,
    "wind": daily_wind
}

print(daily_weather)


hourly_code = []
will_rain = False
for code in range(len(weathercode_slice)):
    each_weathercode = weathercode_slice[code]
    # print(each_weathercode)
    hourly_code.append(each_weathercode)
    if each_weathercode >= 79:
        will_rain = True

# if will_rain:
#     # print("Bring an umbrella.")
