from django.shortcuts import render
import json
from django.http import HttpResponse
from pathlib import Path

bikes_path = Path(__file__).with_name("bikes.json")

with bikes_path.open(encoding="utf-8") as file:
    data_bikes = json.load(file)
    print(data_bikes)

class Bike:
    def __init__(self, name, available):
        self.name = name
        self.available = available

class BikeCatalog:
    def __init__(self):
        self.bike=[]

    def add_bike(self, bike):
        self.bike.append(bike)

    def available_bikes(self):
        result = []
        for bike in self.bike:
            if bike.available == True:
                result.append(bike.name)
        return result 

    def find_bike(self, name):
        for bike in self.bike:
            if bike.name == name:
                return bike
        return None

catalog = BikeCatalog()

for data_bike in data_bikes:
    bike = Bike(data_bike["name"], data_bike["available"])
    catalog.add_bike(bike)
    print(bike.name)

def bike_list(request):
    names = catalog.available_bikes()

    if not names:
        return HttpResponse("Brak dostępnych rowerów")
    
    count= len(names)
    bike_names = ", ".join(names)
    return HttpResponse(f"Available bikes {count}: {bike_names}")

found_bikes = catalog.find_bike("Mountain Bike")
print(found_bikes.name, found_bikes.available)
print(catalog.available_bikes())
