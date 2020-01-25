## @file pos_adt.py
#  @author Almen Ng
#  @brief Provides the GPosT ADT class for representing position using latitude and longitude
#  @date January 20, 2020

from math import asin, sin, cos, radians, atan2, sqrt, degrees, ceil

## @brief An ADT that represents a position
class GPosT:

    ## @brief GPosT constructor
    #  @details Initializes a GPosT object with latitude and longitude of a position
    #  @param y The latitude of the position (assuming that the latitude does not exceed +- 90 degrees)
    #           North is positive, South is negative
    #  @param x The longitude of the position (assuming that the longitude does not exceed +-180 degrees)
    #           East is positive, West is negative
    def __init__(self, y, x):
        self.__x = x
        self.__y = y

    ## @brief Gets the latitude of the position
    #  @return The latitude of the position
    def lat(self):
        return self.__y

    ## @brief Gets the longitude of the position
    #  @return The longitude of the position
    def long(self):
        return self.__x

    ## @brief Checks to see if the current position is to the west of another position
    #  @param p Position of object of type GPosT to compare the current position with
    #  @return True if the current position is to the west of p. False otherwise.
    def west_of(self, p):
        if self.__x < p.__x:
            return True
        else:
            return False

    ## @brief Checks to see if the current position is to the north of another position
    #  @param p Position of object of type GPosT to compare the current position with
    #  @return True if the current position is to the north of p. False otherwise.
    def north_of(self, p):
        if self.__y > p.__y:
            return True
        else:
            return False

    ## @brief Checks to see if the current position is "equal" to another position
    #         Has to be to within 1 km from the current position to be considered "equal"
    #  @param p Position of object of type GPosT to compare the current position with
    #  @return True if the current position is to "equal" to p. False otherwise.
    def equal(self, p):
        if (self.distance(p)) < 1:
            return True
        else:
            return False

    ## @brief Changes the position of the current object (longitude and latitude by starting from the current position and
    #         moving at bearing b for a distance of d
    #  @param b Signed decimal degree of type real representing bearing
    #  @param d The distance travelled in units of km
    def move(self, b, d):
        R = 6371
        angular_distance = d/R
        latitude_original = self.__y
        longitude_orignal = self.__x

        self.__y =  degrees(asin(sin(radians(latitude_original)) * cos(angular_distance) + cos(radians(latitude_original)) * sin(angular_distance) * cos(radians(b))))
        self.__x = degrees(radians(longitude_orignal) + atan2(sin(radians(b)) * sin(angular_distance) * cos(radians(latitude_original)), cos(angular_distance) - sin(radians(latitude_original)) * sin(radians(self.__y))))

    ## @brief Calculates the distance between the current position and p
    #  @param p Position of object of type GPosT to find the distance from
    #  @return Distance (in km) between the current position and p
    def distance(self, p):
        delta_lat = radians(p.__y) - radians(self.__y)
        delta_long = radians(p.__x) - radians(self.__x)
        R = 6371

        a = (sin(delta_lat/2))**2 + cos(radians(self.__y)) * cos(radians(p.__y)) * (sin(delta_long/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))

        return R * c

    ## @brief Calculates the arrival date for someone starting at the current position on a certain date and moving
    #         to another position at a certain speed
    #  @param p Position of object of type GPosT to move to
    #  @param d Date of type DateT of the starting date of the travel
    #  @param s Speed of type real at which someone is moving at in km/day
    #  @return The arrival date after travelling from the current position on date d and moving to position p at a speed of s
    def arrival_date(self, p, d, s):
        days_past = ceil(self.distance(p) / s)
        return d.add_days(days_past)
