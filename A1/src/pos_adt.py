## @file pos_adt.py
#  @title Pos ADT
#  @author Madhi Nagarajan
#  @brief This file is meant to act as an ADT for a global coordinate and to perform location-related calculations
#  @date January 20, 2020

import math
from date_adt import DateT

## @brief The class, GPosT, represents an ADT of a global coordinate
#  @details This class represents represents an ADT of a global coordinate with the ability
#  to perform location-related calculations, utilizing the latitude and longitude
class GPosT:

    ## @brief Constructor for GPosT
    #  @details Constructor accepts two parameters for the latitude and longitude.
    #  @param y is a double value for the respective latitude.
    #  @param x is a double value for the respective longitude.
    def __init__(self, y, x):
        self.latitude = y
        self.longitude = x

    ## @brief Getter method for returning latitude
    #  @returns The latitude value
    def lat(self):
        return self.latitude

    ## @brief Getter method for returning longitude
    #  @returns The longitude value
    def long(self):
        return self.longitude

    ## @brief The function calculates if the current coordinate is west of the given coordinate
    #  @param p is a given coordinate.
    #  @returns A boolean depending on if the current coordinate is west of the given coordinate
    def west_of(self, p):
        if p.long() > self.long():
            return True
        else:
            return False

    ## @brief The function calculates if the current coordinate is north of the given coordinate
    #  @param p is a given coordinate.
    #  @returns A boolean depending on if the current coordinate is north of the given coordinate
    def north_of(self, p):
        if p.lat() < self.lat():
            return True
        else:
            return False

    ## @brief The function calculates if the current coordinate is equal to the given coordinate
    #  @param p is a given coordinate.
    #  @returns A boolean depending on if the current coordinate is equal to the given coordinate
    def equal(self, p):
        if p.lat() == self.lat() and p.long() == self.long():
            return True
        else:
            return False

    ## @brief The function calculates a resultant coordinate given a certain bearing & distance
    #  @param b is a given bearing (in degrees).
    #  @param d is a given distance (in km).
    def move(self, b, d):
        R = 6371
        rlat = math.radians(self.lat())
        rlong = math.radians(self.long())
        rb = math.radians(b)
        d2 = d / R
        rlat2 = math.asin((math.sin(rlat) * math.cos(d2)) + (math.sin(d2) * math.cos(rlat) * math.cos(rb)))
        rlong2 = rlong + math.atan2(math.sin(rb) * math.sin(d2) * math.cos(rlat),
                                    math.cos(d2) - math.sin(rlat) * math.sin(rlat2))
        self.latitude = math.degrees(rlat2)
        self.longitude = math.degrees(rlong2)

    ## @brief The function calculates the distance between the current point and another point
    #  @param p is a given coordinate.
    #  @returns dist, the resultant distance (in km)
    def distance(self, p):
        R = 6371
        rlat1 = math.radians(self.lat())
        rlat2 = math.radians(p.lat())
        latdiff = math.radians(p.lat() - self.lat())
        longdiff = math.radians(p.long() - self.long())

        a = math.sin(latdiff / 2) * math.sin(latdiff / 2) + math.cos(rlat1) * math.cos(rlat2) * math.sin(
            longdiff / 2) * math.sin(longdiff / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        dist = R * c
        return dist

    ## @brief The function calculates the final date based on the speed, destination point, starting date
    #  @param The parameters passed through is the given destination coordinate, p,
    #  @param d is the starting date, and s is the speed in (km/day)
    #  @returns d2, the resultant date
    def arrival_date(self, p, d, s):
        dist = GPosT.distance(self, p)
        days = round(dist / s)
        d2 = DateT.add_days(d, days)
        return d2
