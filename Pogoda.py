import requests
import json

while True:
    #Pobieranie klucza api
    api_key = "d504f333822c844ef5e59562a0940bd6"

    #Pobieranie nazwy miasta
    city_name = input("Podaj nazwę miasta: ")

    print("1. Aktualna pogoda")
    print("2. Pogoda na jutro")

    wyb = input()

    #Tworzenie adresów URL zapytania z nazwą miasta i kluczem API

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=pl"
    url2 = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&cnt=2&appid={api_key}&units=metric&lang=pl"

    #Wyświetlenie informacji o pogodzie
    if wyb=='1':
        response = requests.get(url)
        weather_data = response.json()
        try:
            print(f"Aktualna pogoda w mieście {city_name}:")
            print(f"Temperatura: {weather_data['main']['temp']}°C")
            print(f"Ciśnienie: {weather_data['main']['pressure']} hPa")
            print(f"Wilgotność: {weather_data['main']['humidity']}%")
            print(f"Prędkość wiatru: {weather_data['wind']['speed']} km/h")
            print(f"Opis: {weather_data['weather'][0]['description']}")
        except:
                print("Podana nazwa miasta nie istnieje")    
    elif wyb=='2':
        response = requests.get(url2)
        weather_data = response.json()
        try:
            print(f"Pogoda na jutro w mieście {city_name}:")
            print(f"Temperatura: {weather_data['list'][1]['main']['temp']}°C")
            print(f"Ciśnienie: {weather_data['list'][1]['main']['pressure']} hPa")
            print(f"Wilgotność: {weather_data['list'][1]['main']['humidity']}%")
            print(f"Prędkość wiatru: {weather_data['list'][1]['wind']['speed']} km/h")
            print(f"Opis: {weather_data['list'][1]['weather'][0]['description']}")
        except:
                print("Podana nazwa miasta nie istnieje")
    else:
        print("Jest tylko pogoda aktualna oraz na jutro")
