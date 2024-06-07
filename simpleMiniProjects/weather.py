import requests
from weatherbit.api import Api
from datetime import datetime

# Define the Telegram bot token and chat ID
TOKEN = "7321529662:AAHrIKGPoblcW2jslKfE6sRYGPP7_JZMLnA"
chat_id = '6613996954'

# Initialize the Weatherbit API client with your API key
weather_api = Api("af478399cee04e35bde994e82bb5ef52")

# Dhaka city's latitude and longitude coordinates
dhaka_latitude = 23.8103
dhaka_longitude = 90.4125

try:
    # Retrieve current weather data for Dhaka city
    weather_data = weather_api.get_current(lat=dhaka_latitude, lon=dhaka_longitude)

    # Extract weather details from the nested structure
    data = weather_data.json['data'][0]
    temperature = data['temp']
    weather_description = data['weather']['description']
    wind_speed = data['wind_spd']
    datetime_str = data['ob_time']  # Observation time

    # Convert observation time to a more readable format
    date_time_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
    formatted_datetime = date_time_obj.strftime('%Y-%m-%d %H:%M')

    # Compose message with real-time weather data
    message = (
        f"Real-time weather forecast for Dhaka City:\n"
        f"Current Location: Dhaka\n"
        f"Date and Time: {formatted_datetime}\n"
        f"Current Temperature: {temperature} °C\n"
        f"Weather Condition: {weather_description}\n"
        f"Wind Speed: {wind_speed} m/s"
    )

    # Send message to the specified Telegram chat
    send_message_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    send_message_response = requests.get(send_message_url).json()
    print(send_message_response)  # Print the response to verify message sent

except Exception as e:
    # Print an error message if something goes wrong
    print("An error occurred:", e)
