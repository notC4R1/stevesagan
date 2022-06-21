import requests
import secrets

key = secrets.key

url = "https://api.openweathermap.org/data/2.5/"
auth = "&appid=" + str(key)

headers = {
    "APPID": str(key)
}

def get_city_choice():
    city_choice = input("Name of City \n")
    return city_choice

def get_weather(city_choice):
    city_choice = city_choice
    response = requests.get(url + "weather?q=" + str(city_choice) + "&units=imperial"+auth)
    r = response.json()
    print("It is " + str(r["main"]["temp"]) + " degrees in " + city_choice)

city = get_city_choice()
get_weather(city)