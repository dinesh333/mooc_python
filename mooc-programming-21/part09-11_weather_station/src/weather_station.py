# Please create a class named WeatherStation which is used to store observations about the weather. The class should have the following public attributes:

# a constructor which takes the name of the station as its argument
# a method named add_observation(observation: str) which adds an observation as the last entry in a list
# a method named latest_observation() which returns the latest observation added to the list. If there are no observations yet, the method should return an empty string.
# a method named number_of_observations() which returns the total number of observations added
# a __str__ method which returns the name of the station and the total number of observations added as per the example below.
# All attributes should be encapsulated, so they can't be directly accessed. It is up to you how you implement the class, as long as the public interface is exactly as described above.

# An example of how the class is used:

# station = WeatherStation("Houston")
# station.add_observation("Rain 10mm")
# station.add_observation("Sunny")
# print(station.latest_observation())

# station.add_observation("Thunderstorm")
# print(station.latest_observation())

# print(station.number_of_observations())
# print(station)
# Sample output
# Sunny
# Thunderstorm
# 3
# Houston, 3 observations

# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name):
        self.__name = name
        self.__observations = []
    
    def add_observation(self, observation: str):
        self.__observations.append(observation)

    def number_of_observations(self):
        return len(self.__observations)

    def latest_observation(self):
        if self.number_of_observations() == 0:
            return ''
        else:
            return self.__observations[-1]
    
    def __str__(self):
        return f'{self.__name}, {len(self.__observations)} observations'