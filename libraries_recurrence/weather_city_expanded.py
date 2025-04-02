import requests

def get_coordinates(user_city):

    city_url = f"https://nominatim.openstreetmap.org/search?q={user_city}&format=json&limit=1"
    useragent = {
        "User-Agent": "weather-city-conn-project"
    }

    response = requests.get(city_url, headers=useragent)
    
    if response.status_code == 200:
        coordinates_data = response.json()
        if coordinates_data:
            latitude, longitude = coordinates_data[0]["lat"], coordinates_data[0]["lon"]
            return latitude, longitude
        else:
            return "Nie znaleziono wyników dla danego miasta!"
    else:
        return f"Error: {response.status_code}"
    
    
def get_temperature(latitude, longitude):
    temp_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(temp_url)

    if response.status_code == 200:
        temp_data = response.json()

        if "current" in temp_data:
            cur_temp = temp_data.get("current").get("temperature_2m")
            return cur_temp
        else:
            return "Wystąpił błąd z pobraniem temperatury"
    else:
        return f"Error: {response.status_code}"
user_city = input("Wpisz nazwę miasta (wpisz q lub koniec aby zakończyć): ")
while user_city != "q" and user_city != "koniec":
    coordinates = get_coordinates(user_city)
    if len(user_city.strip()) != 0:
        if isinstance(coordinates, tuple):
            latitude, longitude = coordinates
            temperature = get_temperature(latitude, longitude)
            print(f"Aktualna temperatura w mieście {user_city} to {temperature}°C")
            user_city = input("Wpisz nazwę miasta (wpisz q lub koniec aby zakończyć): ")
        else:
            print(coordinates)
            user_city = input("Wpisz nazwę miasta (wpisz q lub koniec aby zakończyć): ")
    else:
        print("Nazwa miasta nie może być pusta!")
        user_city = input("Wpisz nazwę miasta (wpisz q lub koniec aby zakończyć): ")
else:
    print("Zakończono!")


