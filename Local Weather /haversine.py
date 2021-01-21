"""
    This program based on the Haversine Formula to calculate the distance between two point on a sphere
    using longitudes and latitudes.

"""

#Defining Imports
from math import radians, cos, sin, asin, sqrt

"""Function which will return the distance"""
def haversine(lon1, lat1, lon2, lat2):
    # convert degrees to radians
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)

    # Find the difference between the two longitudes and latitudes
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance = 2 * asin(sqrt(a)) * 6371 # radius of the Earth

    return distance
