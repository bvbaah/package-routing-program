from __future__ import annotations

from datetime import timedelta

from packages import Package


class Truck:

    """
    A truck that carries packages to their destination.

    === Instance Attributes ===
    packaage_collection: A list of packages currently loaded on the truck

    package_id_collection: A list of the id numbers of the packages originally
    loaded onto the truck

    package_visual_collection: A list of id numbers of packages that updates
    depending on which packages remain on the truck as it goes through the
    delivery process

    distance_travelled: The number of miles travelled by the truck between the
    beginning of the trip and the end of day.

    time_truck: A timedelta object that tracks the time in HH:MM format as the
    truck delivers the packages onboard (i.e. 9:00 AM when pkg 5 is delivered)

    loading_time: A timedelta object that displays the time the truck is loaded
    with packages and departs from the hub


    === Representation Invariants ===
    - There are only two drivers available at any time.
    - A truck that is in transit must always have one driver.
    - A truck can carry a maximum of 16 packages.
    - Trucks can not leave the hub before 8:00 a.m.
    - Trucks can only be loaded at the hub.
    - Trucks have unlimited gas and packages are delivered instantaneously.
    """
    # Class Attributes

    package_collection: list[Package]
    package_id_collection: list[int]
    package_visual_collection: list[int]
    distance_travelled: float
    time_truck: timedelta
    loading_time = timedelta

    # Name: __init__
    # Function: Initializes truck object
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __init__(self, time_truck: timedelta = timedelta(hours=8, minutes=0)):
        """
        Initialize truck.

        The constructor for the Truck class is a no-argument constructor that
        will be called when a Truck object is created.
        """
        self.package_collection = []
        self.package_id_collection = []  # Will be for updating package status
        # Used to visualize packages removed from truck in debugger
        self.package_visual_collection = []
        self.distance_travelled = 0.0
        # This attribute tracks the time on the truck as it delivers each pkg
        # It results in the time the truck is done delivering all packages
        self.time_truck = time_truck

        # Initialize loading_time with starting time of time_truck
        # This is the time the truck leaves the hub
        self.loading_time = time_truck

    # Name: __str__
    # Function: Provides a readable String representation of the Truck object
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __str__(self):

        return (f"Package Collection: {len(self.package_collection)}, "
                f"Package IDs: {self.package_id_collection}, "
                f"Distance Travelled: {self.distance_travelled}, "
                f"Loading Time: {self.loading_time}, "
                f"Time on Truck: {self.time_truck}")

    # Name: __repr__
    # Function: Provides a String representation of the Truck object
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __repr__(self):
        return (f"package_collection={self.package_collection}, "
                f"package_id_collection={self.package_id_collection}, "
                f"package_visual_collection={self.package_visual_collection}, "
                f"distance_travelled={self.distance_travelled}, "
                f"loading_time={self.loading_time}, "
                f"time_truck={self.time_truck}")
