from pymongo import MongoClient
import requests
client = MongoClient('mongodb+srv://admin:raichu554@cluster0.iwukc.mongodb.net/weather_climate?retryWrites=true&w=majority')

forecast = f'https://api.openweathermap.org/data/2.5/onecall?lat=49.4883&lon=8.4647&appid=e989c1652907feb4f3b7ce8ade5977b0'
response = requests.get(forecast).json()
print(response)

db = client.weather_climate
coll_daily = db.daily_weather

results = response['daily']
for result in results:
    coll_daily.insert_one(result)

db = client.weather_climate
coll_hourly = db.hourly_weather

results = response['hourly']
for result in results:
    coll_hourly.insert_one(result)

db = client.weather_climate
coll_minutely = db.minutely_weather

results = response['minutely']
for result in results:
    coll_minutely.insert_one(result)





