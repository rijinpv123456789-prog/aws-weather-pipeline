import json
import os
import time
import urllib.request
from decimal import Decimal

import boto3

# Initialize DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("table_weather")

# Read API key from Lambda environment variable
API_KEY = os.environ["OPENWEATHER_API_KEY"]


def lambda_handler(event, context):

    city = "London"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    # Call OpenWeather API
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())

    # Store data in DynamoDB
    table.put_item(
        Item={
            "city": city,
            "timestamp": int(time.time()),
            "temperature": Decimal(str(data["main"]["temp"])),
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "wind_speed": Decimal(str(data["wind"]["speed"])),
            "country": data["sys"]["country"]
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Weather data stored successfully!")
    }
