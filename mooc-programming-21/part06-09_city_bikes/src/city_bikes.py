# In this exercise we will write some functions for working on a file containing location data from the stations for city bikes in Helsinki.
# Each station has a single line in the file. The line contains the coordinates, name, and other identifying information for the station.

# Part 1: Distance between stations
# First, write a function named get_station_data(filename: str). This function should read the names and locations of all the stations in the file, and return them in a dictionary with the following format:
# Dictionary keys are the names of the stations, and the value attached is a tuple containing the location coordinates of the station. The first element in the tuple is the Longitude field, and the second is the Latitude field.

# Next, write a function named distance(stations: dict, station1: str, station2: str), which returns the distance between the two stations given as arguments.

# The distance is calculated using the Pythagorean theorem. The multiplication factors below are approximate values for converting latitudes and longitudes to distances in kilometres in the Helsinki region.

# Part 2: The greatest distance
# Please write a function named greatest_distance(stations: dict), which works out the two stations on the list with the greatest distance from each other. The function should return a tuple, where the first two elements are the names of the two stations, and the third element is the distance between the two.


# Write your solution here
import math

def read_file(filename: str):
    with open(filename) as file:
        lines = []
        for line in file:
            line = line.replace('\n', '')
            line = line.strip()
            if 'longitude' in line.lower():
                continue
            lines.append(line)
        return lines

def get_station_data(filename: str):
    stations_raw = read_file(filename)
    stations = {}
    for station in stations_raw:
        station_data = station.split(';')
        name = station_data[3]
        long = float(station_data[0])
        lat = float(station_data[1])
        stations[name] = (long, lat)
    return stations

def distance(stations: dict, station1: str, station2: str):
    long1, lat1 = stations[station1]
    long2, lat2 = stations[station2]

    x_km = (long1 - long2) * 55.26
    y_km = (lat1 - lat2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance_from_one_station(stations: dict, stations_list: list, station: str):
    start_index = stations_list.index(station)+1
    compare_list = stations_list[start_index:]
    greatest_tuple = None
    greatest = 0
    for compare in compare_list:
        d = distance(stations, station, compare)
        if d > greatest:
            greatest_tuple = (station, compare, d)
            greatest = d
    return greatest_tuple

def greatest_distance(stations: dict):
    stations_list = []
    for key, value in stations.items():
        stations_list.append(key)

    greatest_tuple = None
    greatest = 0
    for index, station in enumerate(stations_list):
        if index < len(stations_list)-1:
            stations_distance = greatest_distance_from_one_station(stations, stations_list, station)
            station1, station2, distance = stations_distance
            if distance > greatest:
                greatest_tuple = stations_distance
                greatest = distance
    
    return greatest_tuple