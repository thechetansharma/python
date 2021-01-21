"""
    Assignment 5 - Fetching the Weather

    This program will fetch a Weather Station accroding to latitude and longitude,
    and then get the latest weather updates from that station.

"""

# Defining Imports
from requests import get
from pprint import pprint
from haversine import haversine

# Home Location latitude and Longtitude
my_lat = 49.9652800
my_lon = -97.1623346

# RESTful Api service to getch the weather station data
stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

# Fetching the data from stations url and formatting it in json object"""
all_stations = get(stations).json()['items']

"""This function will return the closest station id to my home location"""
def find_closest_station():
    # The longest possible distance between two points on the Earth’s surface
    smallest = 20036

    # Looping through all station and finding the smallest distance between home location and weather station"""
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        # Calling haversine function
        distance = haversine(my_lon, my_lat, station_lon, station_lat)

        # If the distance returned by haversine formula is less than the smallest variable
        # then we are setting the smallest as the distance variable and storing the weather station id
        # in closest_station variable.
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']

    return closest_station

# Calling the find_closest_station function
closest_stn = find_closest_station()

# Appending the cloeset station id to the weather url
weather = weather + str(closest_stn)

# Fetching the weather data as per station id
my_weather = get(weather).json()['items']

# printing closest station data
print("Local Weather Station Data : ")
pprint(my_weather)
