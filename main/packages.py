from __future__ import annotations

from datetime import timedelta


class Package:
    """
    A package.

    === Instance Attributes ===
    package_id: The id number for the package

    delivery_address: The address the package is being delivered to

    delivery_city: The city the package is being delivered to

    delivery_zipcode: The zipcode the package is delivered to

    weight: The weight of the package (in kilograms)

    delivery_status: The delivery status of the package (i.e. AT THE HUB,
    EN ROUTE, DELIVERED, DELAYED - ON FLIGHT TO DEPOT)

    loading_time: The time the package is loaded onto the truck

    time_tracker: The time the package is delivered
    """
    package_id: int
    delivery_address: str
    delivery_city: str
    delivery_state: str
    delivery_zipcode: int
    delivery_deadline: str
    weight: int
    notes: str
    delivery_status: str
    loading_time: timedelta
    time_tracker: timedelta

    # Name: __init__
    # Function: Initializes package object
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __init__(self, id_num: int, address: str, city: str, state: str,
                 zipcode: int, deadline: str, weight: int, notes: str) -> None:
        """
        Initialize package.

        The constructor for the Package class will take the id, delivery
        address,delivery city, delivery zipcode and package weight as parameters

        The delivery status of the package will not be a parameter
        because we want to update that value as each package is delivered

        The package status will begin as 'AT THE HUB' and then be adjusted
        accordingly.

        """
        self.package_id = id_num
        self.delivery_address = address
        self.delivery_city = city
        self.delivery_state = state
        self.delivery_zipcode = zipcode
        self.delivery_deadline = deadline
        self.notes = notes
        self.weight = weight

        self.delivery_status = 'AT THE HUB'
        # Loading time is the time the packages are loaded onto the track
        self.loading_time = timedelta(hours=8, minutes=0)
        # Time tracker acts as a counter to track the time that passes as the
        # package moves from the hub to its destination. It is initally
        # the same value as the loading time and has time added to it everytime
        # a package is delivered
        self.time_tracker = self.loading_time

    # Name: __str__
    # Function: Provides a readable String representation of the Package object
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __str__(self):
        return f"Package ID: {self.package_id}\n" \
               f"Delivery Address: {self.delivery_address}\n" \
               f"City: {self.delivery_city}\n" \
               f"State: {self.delivery_state}\n" \
               f"Zipcode: {self.delivery_zipcode}\n" \
               f"Delivery Deadline: {self.delivery_deadline}\n" \
               f"Weight: {self.weight} kg\n" \
               f"Notes: {self.notes}" \
               f"Delivery Status: {self.delivery_status}\n" \
               f"Loading Time: {self.loading_time}" \
               f"Time Tracker: {self.time_tracker}" \

    # Name: __repr__
    # Function: Provides a String representation of the Package object
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def __repr__(self):
        return f"Package(id_num={self.package_id}, " \
               f"address='{self.delivery_address}', " \
               f"city='{self.delivery_city}', state='{self.delivery_state}', " \
               f"zipcode='{self.delivery_zipcode}', " \
               f"deadline= '{self.delivery_deadline}', '" \
               f"weight={self.weight}, " \
               f"notes='{self.notes}', " \
               f"delivery_status='{self.delivery_status}', " \
               f"loading_time={self.loading_time}, " \
               f"time tracker={self.time_tracker}"


# Example Use
"""
package = Package(1, '195 W Oakland Ave', 'Salt Lake City', 'UT',
                  84115, '10:30:00', 21, 'Must be delivered by 1:00 PM')
print(package)
print(repr(package))

"""
