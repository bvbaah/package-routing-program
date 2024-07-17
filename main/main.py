"""
Title: C950 - WGUPS Routing Program
Student Name: Brandon Van Baah
Student ID: 011130244
"""
from __future__ import annotations

import csv
import time
from datetime import timedelta

from hashtable import ChainingHashTable
from packages import Package
from trucks import Truck
from colors import Colors


# Name: string_to_timedelta
# Function: Converts a string to timedelta type
# Time Complexity: O(1)
# Space Complexity: O(1)
def string_to_timedelta(time_str: str) -> timedelta:
    try:
        # Split the string into hours and minutes
        parts = time_str.split(':')

        # Check if the split parts are exactly two
        if len(parts) != 2:
            raise ValueError

        # Convert the split string values to integers
        hours = int(parts[0])
        minutes = int(parts[1])

        # Check if hours and minutes are within valid ranges
        if not (0 <= hours <= 23 and 0 <= minutes <= 59):
            raise ValueError

        # Create and return a timedelta object
        return timedelta(hours=hours, minutes=minutes)

    except (ValueError, TypeError):
        raise ValueError("Invalid input. Please enter time in HH:MM format.")


# Name: add_time_to_truck
# Function: Add time to time_truck attribute of truck
# Time Complexity: O(1)
# Space Complexity: O(1)
def add_time_to_truck(truck: Truck, time_elapsed: timedelta) -> None:

    # Time_elapsed is the amount of time taken to travel between addresses

    # Add the additional time, time_elapsed, to the initial time of the truck
    truck.time_truck += time_elapsed


# Function: time_elapsed_between_packages
# Function: This will calculate how much time has elapsed between loading_time
# time of delivery for the package. Update the time tracker for package.
# Add this time to the truck to update time tracker for truck the package is on
# Time Complexity: O(1)
# Space Complexity: O(1)
def time_elapsed_between_packages(distance: float) -> timedelta:

    # Convert the time you will be adding to the truck_time to timedelta obj
    additional_time = timedelta(minutes=distance)

    return additional_time


class Main:
    """
    The main class where the WGUPS program is run.

    distance_matrix: A 2D array that holds all distance values between addresses
    package_hashtable: A hashtable that holds all package data and updates
    as the trucks deliver packages
    location_list: A list that holds all possible package addresses

    """
    distance_matrix: list[list[str]]
    package_hashtable: ChainingHashTable
    updated_package_hashtable: ChainingHashTable
    location_list: list[str]

    # Name: __init__
    # Function: Initializes main class object
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __init__(self):
        """
        Initialize class attributes of Main class. These attributes are data
        structures that will hold crucial information necessary to run the
        program.
        """
        self.distance_matrix = []
        self.package_hashtable = ChainingHashTable()
        self.updated_package_hashtable = ChainingHashTable()
        self.updated_package_hashtable = self.package_hashtable
        self.location_list = []

    # Name: main
    # Function: This method runs the program and its user interface
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def main(self) -> None:
        # Load package data into hashtable
        self.read_package_data('../data/packages.csv')
        # Load distance data into distance 2D array
        self.read_distance_data('../data/distances.csv')
        # Load address data into location list
        self.read_location_data('../data/locations.csv')

        print("\nWelcome to the WGUPS Routing System!")

        while True:

            # Store 9:05 AM in timedelta object to hold the late leave time
            late_leave_time = timedelta(hours=9, minutes=5)

            # Create truck objects
            t1 = Truck()
            t2 = Truck(late_leave_time)
            t3 = Truck()
            print("\nOptions")
            print("1: Print All Package Status and Total Mileage")
            print("2: Get a Single Package Status with a Time")
            print("3: Get All Package Status with a Time")
            print("4: Exit the Program\n")

            option = input("Please enter your option: ")

            match option:
                case "1":

                    # Update package 9 address to the correct address
                    pkg_9 = self.package_hashtable.search(9)
                    pkg_9.delivery_address = "410 S State St"
                    pkg_9.delivery_city = "Salt Lake City"
                    pkg_9.delivery_state = "UT"
                    pkg_9.delivery_zipcode = 84111

                    # Update package information in package hashtable
                    self.package_hashtable.insert(pkg_9.package_id, pkg_9)

                    # Start delivery process
                    self.package_delivery_process(t1, t2, t3)

                    # Print all truck distances travelled and total distance
                    # of all trucks
                    total_distance = t1.distance_travelled + \
                                     t2.distance_travelled + \
                                     t3.distance_travelled

                    print("\nTruck 1 Statistics\n")
                    print(f"Departure Time: {t1.loading_time}")
                    print(f"Trip Completed Time: {t1.time_truck}")
                    print(f"Time Elapsed: {t1.time_truck - t1.loading_time}")
                    print(f"Truck 1 Total Distance: "
                          f"{round(t1.distance_travelled, 2)} miles \n")

                    print(f"Truck 2 Statistics\n")
                    print(f"Departure Time: {t2.loading_time}")
                    print(f"Trip Completed Time: {t2.time_truck}")
                    print(f"Time Elapsed: {t2.time_truck - t2.loading_time}")
                    print(f"Truck 2 Total Distance: "
                          f"{round(t2.distance_travelled, 2)} miles\n")

                    print(f"Truck 3 Statistics\n")
                    print(f"Departure Time: {t3.loading_time}")
                    print(f"Trip Completed Time: {t3.time_truck}")
                    print(f"Time Elapsed: {t3.time_truck - t3.loading_time}")
                    print(f"Truck 3 Total Distance: "
                          f"{round(t3.distance_travelled, 2)} miles \n")

                    print(f"Total Distance Travelled: "
                          f"{round(total_distance, 2)} miles\n")

                    # Print status of every package after trucks have
                    # delivered all packages
                    self.print_package_status()

                case "2":

                    valid_input = False
                    time_delta = None
                    time_input = None

                    valid_input_2 = False
                    package_id_input = None

                    while not valid_input:
                        print("Please input the time using a 24-hour clock!")
                        print("Example: 1:05 AM = 1:05 | 1:05 PM = 13:05")
                        time_input = input(
                            "Please enter the time at which you want to view "
                            "package (in HH:MM format): ")

                        try:
                            # Convert time_input to timedelta and raise
                            # ValueError if wrong format is inputted

                            time_delta = string_to_timedelta(time_input)

                            # Set the flag to True to exit the loop
                            valid_input = True

                            while not valid_input_2:
                                try:
                                    # Ask user which package they would like to
                                    # see and return package info using lookup
                                    # function
                                    package_id_input = int(input(
                                        "Please enter the ID # of the "
                                        "package you "
                                        "would like to lookup (demonstration of"
                                        " lookup function): "))
                                    # Set flag to true to exit out of
                                    # while loop
                                    valid_input_2 = True
                                except ValueError:
                                    print(
                                        "Invalid input. Please enter an "
                                        "integer.")
                        except ValueError as e:
                            print(e)

                    # If correct format is inputted then update pkg 9
                    # to the correct information is the time is
                    # inputted by the user is greater than 10:20 AM

                    # Package 9 will update if the user inputted time
                    # is greater than 10:20 AM Else, the WGUPS
                    # program will act like it does not know the
                    # correct address for package 9 before 10:20 AM
                    pkg_9 = self.package_hashtable.search(9)
                    if time_delta >= timedelta(hours=10, minutes=20):
                        pkg_9.delivery_address = "410 S State St"
                        pkg_9.delivery_city = "Salt Lake City"
                        pkg_9.delivery_state = "UT"
                        pkg_9.delivery_zipcode = 84111

                    # Else, return package 9 back to its original info
                    else:
                        pkg_9.delivery_address = "300 State St"
                        pkg_9.delivery_city = "Salt Lake City"
                        pkg_9.delivery_state = "UT"
                        pkg_9.delivery_zipcode = 84103

                    # Update package information in package hashtable with its
                    # respective info to time
                    self.package_hashtable.insert(pkg_9.package_id, pkg_9)

                    # Start delivery process
                    self.package_delivery_process(t1, t2, t3)

                    # Update statuses on all trucks for time inputted by user
                    self.update_packages_for_truck(time_input, t1)
                    self.update_packages_for_truck(time_input, t2)
                    self.update_packages_for_truck(time_input, t3)

                    # Return info for package looked up by user (printed)
                    self.lookup_package(package_id_input)

                case "3":
                    valid_input = False
                    time_delta = None
                    time_input = None

                    while not valid_input:
                        print("Please input the time using a 24-hour clock!")
                        print("Example: 1:05 AM = 1:05 | 1:05 PM = 13:05")
                        time_input = input(
                            "Please enter the time at which you want to view "
                            "packages (in HH:MM format): ")

                        try:
                            time_delta = string_to_timedelta(time_input)
                            # Set the flag to True to exit the loop
                            valid_input = True

                        except ValueError as e:
                            print(e)

                    # Package 9 will update if the user inputted time
                    # is greater than 10:20 AM Else, the WGUPS
                    # program will act like it does not know the
                    # correct address for package 9 before 10:20 AM
                    pkg_9 = self.package_hashtable.search(9)
                    if time_delta >= timedelta(hours=10, minutes=20):
                        pkg_9.delivery_address = "410 S State St"
                        pkg_9.delivery_city = "Salt Lake City"
                        pkg_9.delivery_state = "UT"
                        pkg_9.delivery_zipcode = 84111

                    # Else, return package 9 back to its original info
                    else:
                        pkg_9.delivery_address = "300 State St"
                        pkg_9.delivery_city = "Salt Lake City"
                        pkg_9.delivery_state = "UT"
                        pkg_9.delivery_zipcode = 84103

                    # Update package information in package
                    # hashtable
                    self.package_hashtable.insert(pkg_9.package_id,
                                                  pkg_9)

                    # Start delivery process
                    self.package_delivery_process(t1, t2, t3)

                    # Update statuses on all trucks for time inputted by user
                    self.update_packages_for_truck(time_input, t1)
                    self.update_packages_for_truck(time_input, t2)
                    self.update_packages_for_truck(time_input, t3)

                    # Print package data for all packages
                    self.lookup_all_packages()

                case "4":
                    # Exit out of program
                    print("\nThank you for using the WGUPS Routing Program!")
                    time.sleep(2)
                    exit()

                case _:
                    # Returns error message if user enters an invalid option and
                    # prompts the user to enter a correct option
                    print("Invalid option. Please enter a number between 1 "
                          "and 4.")

    # Name: package_delivery_process
    # Function: Deliver all packages loaded on each truck
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def package_delivery_process(self, t1: Truck, t2: Truck, t3: Truck) -> None:
        # Store 9:05 AM in timedelta object to hold the late departing time
        late_leave_time = timedelta(hours=9, minutes=5)
        # Make Truck objects
        # t1 = Truck()
        # t2 = Truck(late_leave_time)
        # t3 = Truck()

        # Load Trucks with packages
        self.truck_load_packages(t1, t2, t3)

        # Update all pkgs loading time for truck 2 because they are leaving late
        # i.e. 9:05 AM

        for package in t2.package_collection:
            package.loading_time = late_leave_time

        # Deliver packages on trucks t1 and t2
        self.truck_deliver_packages(t1)
        self.truck_deliver_packages(t2)

        # Find the truck that delivered all of its packages the fastest
        # and set the loading time of truck t3 to the time tracker
        # of the fastest truck between t1 and t2
        # Set each package on the truck's loading time and initial time tracker
        # to the time the fastest truck is finished delivering its packages

        t3.loading_time = min(t1.time_truck, t2.time_truck)
        t3.time_truck = min(t1.time_truck, t2.time_truck)

        for package in t3.package_collection:
            package.loading_time = t3.time_truck

        # If the truck time for truck 3 is greater than 10:20, update the
        # package stats to reflect the new address

        # Deliver packages on truck t3
        self.truck_deliver_packages(t3)

    # Name: print_package_status
    # Function: Print out every package status for case 1
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def print_package_status(self) -> None:

        # Define the column headers
        headers = ["Package ID", "Address", "Deadline", "Delivery Status"]
        # Print the headers
        print(
            f"{headers[0]:<12} {headers[1]:<25} {headers[2]:<12} "
            f"{headers[3]:<15}")

        for package_id in range(1, 41):
            package = self.package_hashtable.search(package_id)

            package_id = package.package_id
            address = package.delivery_address
            deadline = package.delivery_deadline
            delivery_status = package.delivery_status
            delivery_time = package.time_tracker

            t1_package_list = [4, 5, 7, 12, 13, 14, 15, 16, 19, 20,
                               21, 29, 31, 34, 37, 40]

            t2_package_list = [1, 2, 3, 6, 8, 10, 17, 18, 27, 28, 30, 32,
                               33, 35, 36, 38]

            # t3_package_list = [9, 11, 22, 23, 24, 25, 26, 39]

            if package_id in t1_package_list:
                truck_num = 1
            elif package_id in t2_package_list:
                truck_num = 2
            else:
                truck_num = 3

            # Convert delivery_time to string if it's a timedelta
            if isinstance(delivery_time, timedelta):
                delivery_time_str = str(delivery_time)
            else:
                delivery_time_str = delivery_time

            # Shorten address if it is too long, so it fits within column
            if len(address) > 25:
                address = address[:21] + "..."

            # Create delivery status statement so its readable for user
            delivery_statement = \
                f"{Colors.color_text(delivery_status, Colors.GREEN)} " \
                f"by Truck {truck_num} at {delivery_time_str} "

            # Print the specific columns for each package
            print(f"{package_id:<12} {address:<25} {deadline:<12} "
                  f"{delivery_statement:<15}")

    # Name: lookup_package
    # Function: This function returns the package info for the package and time
    # requested by the user in the main method for option 2
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def lookup_package(self, p_id: int) -> None:
        hashtable = self.updated_package_hashtable
        package = hashtable.search(p_id)

        package_id = package.package_id
        address = package.delivery_address
        city = package.delivery_city
        state = package.delivery_state
        zipcode = package.delivery_zipcode
        deadline = package.delivery_deadline
        weight = package.weight
        delivery_status = package.delivery_status
        delivery_time = package.time_tracker

        t1_package_list = [4, 5, 7, 12, 13, 14, 15, 16, 19, 20,
                           21, 29, 31, 34, 37, 40]

        t2_package_list = [1, 2, 3, 6, 8, 10, 17, 18, 27, 28, 30, 32,
                           33, 35, 36, 38]

        # t3_package_list = [9, 11, 22, 23, 24, 25, 26, 39]

        # Initialize truck_num
        if p_id in t1_package_list:
            truck_num = 1

        elif p_id in t2_package_list:
            truck_num = 2

        else:
            truck_num = 3

        # Color the status text
        # Use if statement to output the correct delivery status statement

        # For delivery status == "DELAYED - ON FLIGHT TO DEPOT", make
        # delivery_status red
        if delivery_status == "DELAYED - ON FLIGHT TO DEPOT":
            print(f"\nPackage ID: {package_id}, Delivery Address: {address}, "
                  f"City: {city}, State: {state}, Zipcode: {zipcode}, "
                  f"Deadline: {deadline}, Weight: {weight}, "
                  f"{Colors.color_text(delivery_status, Colors.LIGHT_RED)}")

        elif delivery_status == "AT THE HUB":
            print(f"\nPackage ID: {package_id}, Delivery Address: {address}, "
                  f"City: {city}, State: {state}, Zipcode: {zipcode}, "
                  f"Deadline: {deadline}, Weight: {weight}, "
                  f"{Colors.color_text(delivery_status, Colors.ORANGE)}")

        # For delivery_status = "EN ROUTE", make delivery status text yellow
        elif delivery_status == "EN ROUTE":
            print(f"\nPackage ID: {package_id}, Delivery Address: {address}, "
                  f"City: {city}, State: {state}, Zipcode: {zipcode}, "
                  f"Deadline: {deadline}, Weight: {weight}, "
                  f"Delivery Status: "
                  f"{Colors.color_text(delivery_status, Colors.YELLOW)} "
                  f"on Truck {truck_num}")

        # For delivery status == DELIVERED, make delivery_status green
        else:
            print(f"\nPackage ID: {package_id}, Delivery Address: {address}, "
                  f"City: {city}, State: {state}, Zipcode: {zipcode}, "
                  f"Deadline: {deadline}, Weight: {weight}, "
                  f"Delivery Status: "
                  f"{Colors.color_text(delivery_status, Colors.GREEN)} "
                  f"on Truck {truck_num} at {delivery_time}")

    # Name: lookup_all_packages
    # Function: This function returns the package info for all packages at the
    # time requested by the user in the main method for case 3
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lookup_all_packages(self) -> None:
        headers = ["Package ID", "Address", "City", "State", "Zipcode",
                   "Deadline", "Weight", "Delivery Status"]
        header_line = f"\n{headers[0]:<12} {headers[1]:<25} {headers[2]:<20} " \
                      f"{headers[3]:<10} " \
                      f"{headers[4]:<10} {headers[5]:<12} {headers[6]:<8} " \
                      f"{headers[7]:<15}"
        print(header_line)

        for package_id in range(1, 41):
            package = self.updated_package_hashtable.search(package_id)

            package_id = package.package_id
            address = package.delivery_address
            city = package.delivery_city
            state = package.delivery_state
            zipcode = package.delivery_zipcode
            deadline = package.delivery_deadline
            weight = package.weight
            # notes = package.notes  # Removed from data
            delivery_status = package.delivery_status
            # delivery_time can be str or timedelta
            delivery_time = package.time_tracker

            t1_package_list = [4, 5, 7, 12, 13, 14, 15, 16, 19, 20, 21, 29, 31,
                               34, 37, 40]
            t2_package_list = [1, 2, 3, 6, 8, 10, 17, 18, 27, 28, 30, 32, 33,
                               35, 36, 38]
            # t3_package_list = [9, 11, 22, 23, 24, 25, 26, 39]

            truck_num = None

            if package_id in t1_package_list:
                truck_num = 1
            elif package_id in t2_package_list:
                truck_num = 2
            else:
                truck_num = 3

            # Convert delivery time (timedelta) to a string
            if isinstance(delivery_time, timedelta):
                delivery_time_str = str(delivery_time)
            else:
                delivery_time_str = delivery_time

            status_list = ["DELAYED - ON FLIGHT TO DEPOT", "AT THE HUB"]

            # Use if statement to output the correct delivery status statement

            # For delivery status == "DELAYED - ON FLIGHT TO DEPOT" or "AT HUB"
            if delivery_status == "DELAYED - ON FLIGHT TO DEPOT":
                delivery_status = \
                    f"{Colors.color_text(delivery_status, Colors.LIGHT_RED)}"

            elif delivery_status == "AT THE HUB":
                delivery_status = \
                    f"{Colors.color_text(delivery_status, Colors.ORANGE)}"

            elif delivery_status == "EN ROUTE":
                delivery_status = f"{Colors.color_text(delivery_status, Colors.YELLOW)} " \
                                  f"on Truck {truck_num}"

            else:
                delivery_status = \
                    f"{Colors.color_text(delivery_status, Colors.GREEN)} " \
                    f"by Truck {truck_num} at {delivery_time_str}"

            if len(address) > 25:
                address = address[:21] + "..."

            data = [package_id, address, city, state, zipcode, deadline, weight,
                    delivery_status]

            print(f"{data[0]:<12} {data[1]:<25} {data[2]:<20} {data[3]:<10} "
                  f"{data[4]:<10} {data[5]:<12} {data[6]:<8} {data[7]:<15}")

    # Name: update_packages_for_trucks
    # Function: Updates package hash table
    # for each package depending on the time entered by the user
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def update_packages_for_truck(self, user_time: str, truck: Truck) -> None:

        # Use a for loop to loop through list of package_id (i.e.
        # truck_1_package_ids - [2, 4, 7, 12, 13, 14, 15, 16, 17, 19, 20, 21,
        # 28, 33, 39, 40]).
        # We use a list of id,s instead of a list of packages to loop through
        # b/c the list of packages on the truck is empty after every package
        # has been delivered
        for i in truck.package_id_collection:
            original_package = self.package_hashtable.search(i)
            updated_package = original_package
            time_user_input = string_to_timedelta(user_time)

            # The flight with packages will arrive at 9:05 AM
            flight_arrival_time = timedelta(hours=9, minutes=5)

            delay = "Delayed on flight---will not arrive to depot until 9:05 am"

            if original_package.notes == delay and \
                    time_user_input < flight_arrival_time:
                updated_package.delivery_status = "DELAYED - ON FLIGHT TO DEPOT"

            elif time_user_input <= original_package.loading_time:
                updated_package.delivery_status = "AT THE HUB"

            elif time_user_input < original_package.time_tracker:
                updated_package.delivery_status = "EN ROUTE"

            elif time_user_input >= original_package.time_tracker:
                updated_package.delivery_status = "DELIVERED"

            # Add updated package to the updated hashtable of packages
            self.updated_package_hashtable.insert(updated_package.package_id,
                                                  updated_package)

    # Name: read_package_data
    # Function: Reads package data from a CSV file into a chaining hash table
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def read_package_data(self, filename: str) -> None:
        # Open the CSV file
        with open(filename) as packages:
            package_data = csv.reader(packages, delimiter=',')
            # For each row in csv file, separate data points into variables
            for package in package_data:
                package_id = int(package[0])
                package_address = str(package[1])
                package_city = str(package[2])
                package_state = str(package[3])
                package_zipcode = int(package[4])
                package_deadline = str(package[5])
                package_weight = int(package[6])
                package_notes = str(package[7])

                # Place data into Package object

                p = Package(package_id, package_address, package_city,
                            package_state, package_zipcode, package_deadline,
                            package_weight, package_notes)

                # Insert new Package object into hashtable
                self.package_hashtable.insert(package_id, p)

    # Name: read_distance_data
    # Function: This method reads distance data from a CSV file into a 2D array
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def read_distance_data(self, filename: str) -> None:

        # Open CSV file
        with open(filename) as distances:
            distance_data = csv.reader(distances, delimiter=',')

            # For every row in CSV file, convert each element to a float and
            # append the row to 2D array
            for row in distance_data:
                distance_row = []
                for distance in row:
                    distance_row.append(distance)
                self.distance_matrix.append(distance_row)

    # Name: read_location_data
    # Function: Reads data from locations/addresses file and stores it in
    # in a list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def read_location_data(self, filename: str) -> None:

        # Open CSV file and read it to a variable
        with open(filename) as locations:
            location_data = csv.reader(locations, delimiter=',')

            # For each row in the CSV file, take the third value at the index
            # of the row, and add it to the location_list
            for row in location_data:
                location = row[2]
                self.location_list.append(location)

    # Name: calculate_distance
    # Function: Calculates the distance between two addresses
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def calculate_distance(self, a1: str, a2: str) -> float:

        # Store the indexes of a1 and a2 in location_list
        i = self.location_list.index(a1)
        j = self.location_list.index(a2)

        # Set distance variable
        distance = self.distance_matrix[i][j]

        # If distance is equal to an empty string in the csv file, flip
        # the indexes because distance[i][j] = distance[j][i]
        if distance == '':
            distance = self.distance_matrix[j][i]

        return float(distance)

    # Name: min_distance_from_address
    # Function: Return the closest address to the inputted address
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def min_distance_from_address(self, a1: str, truck: Truck) -> \
            list[str, float, Package]:

        # Set minimum distance to a very high value
        min_distance = 5000.0
        # Set min_address (nearest address) to an empty string
        min_address = ""
        # Set the pkg that needs to be delivered to the nearest address to None
        p = None

        # Iterate through every package's delivery address and find the closest
        # address to address a1
        for package in truck.package_collection:
            a2 = package.delivery_address
            distance = self.calculate_distance(a1, a2)

            if distance < min_distance:
                min_distance = distance
                min_address = a2
                p = package

        result = [min_address, min_distance, p]

        # Return the nearest address to a1, the distance between a1 and the
        # nearest address, a2, and the package that is being delivered to
        # the nearest address
        return result

    # Name: truck_deliver_packages
    # Function: Deliver all packages on truck using nearest neighbor algorithm
    # Update the time travelled by the truck after each package is delivered in
    # the package hash table and update delivery time and status
    # of each package on the truck
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def truck_deliver_packages(self, truck: Truck) -> None:

        # Deliver the rest of the packages on the truck
        # Set hub address
        hub = "4001 South 700 East"

        # Initialize previous_address with hub address
        previous_address = [hub, 0]
        while len(truck.package_collection) > 0:
            # For the closest address to the previous address,
            # the nearest address is stored in nearest_address[0] and
            # the package_id of the package that will
            # be delivered there is stored in nearest_address[1]

            # Find the nearest address to the previous address
            nearest_address = self.min_distance_from_address(
                previous_address[0], truck)

            next_package = nearest_address[2]

            # Calculate the distance between the previous address and
            # nearest address
            first_distance = self.calculate_distance(previous_address[0],
                                                     nearest_address[0])
            # Make truck travel to the nearest address and update the total
            # distance the truck has travelled
            truck.distance_travelled += first_distance

            # Calculate the amount of time the truck took to
            # reach the nearest address IN MINUTES
            # Note that 18 miles per hour = 0.3 miles per minute
            time_to_deliver = float(first_distance / 0.3)

            # Update time of time_tracker attribute for package ON the truck
            # to determine the time the package arrived at its destination
            # This line calculates the amount of time passed between the
            # previous address and the next nearest address and will be used to
            # update time tracker for truck

            truck_distance_travelled = \
                time_elapsed_between_packages(time_to_deliver)

            # Update time of truck_time attribute of truck which is used to
            # track time for the truck after its travelled to a new address
            add_time_to_truck(truck, truck_distance_travelled)

            # Update package delivery time to the CURRENT truck time after the
            # package has been delivered
            next_package.time_tracker = truck.time_truck

            # Update status of the delivered package to "DELIVERED"
            # ON the truck
            next_package.delivery_status = "DELIVERED"

            # Store address of the package that was delivered
            previous_address = nearest_address

            # Insert delivered package into original hashtable
            self.package_hashtable.insert(next_package.package_id, next_package)

            # Find which package on the truck has the same delivery address
            # as the nearest address and remove it from the truck because it has
            # been delivered

            # Remove package from truck
            truck.package_collection.remove(next_package)
            # Remove in visual package collection for debugger
            truck.package_visual_collection.remove(next_package.package_id)

    # Run this function in main method and use it as input for package lookup
    # If the user inputs the time in the wrong format, raise an error

    # Name: truck_load_packages
    # Function: This function loads packages onto all trucks
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def truck_load_packages(self, t1: Truck, t2: Truck, t3: Truck) -> None:

        # Assign every package to a package variable

        p1 = self.package_hashtable.search(1)
        p2 = self.package_hashtable.search(2)
        p3 = self.package_hashtable.search(3)
        p4 = self.package_hashtable.search(4)
        p5 = self.package_hashtable.search(5)
        p6 = self.package_hashtable.search(6)
        p7 = self.package_hashtable.search(7)
        p8 = self.package_hashtable.search(8)
        p9 = self.package_hashtable.search(9)
        p10 = self.package_hashtable.search(10)
        p11 = self.package_hashtable.search(11)
        p12 = self.package_hashtable.search(12)
        p13 = self.package_hashtable.search(13)
        p14 = self.package_hashtable.search(14)
        p15 = self.package_hashtable.search(15)
        p16 = self.package_hashtable.search(16)
        p17 = self.package_hashtable.search(17)
        p18 = self.package_hashtable.search(18)
        p19 = self.package_hashtable.search(19)
        p20 = self.package_hashtable.search(20)
        p21 = self.package_hashtable.search(21)
        p22 = self.package_hashtable.search(22)
        p23 = self.package_hashtable.search(23)
        p24 = self.package_hashtable.search(24)
        p25 = self.package_hashtable.search(25)
        p26 = self.package_hashtable.search(26)
        p27 = self.package_hashtable.search(27)
        p28 = self.package_hashtable.search(28)
        p29 = self.package_hashtable.search(29)
        p30 = self.package_hashtable.search(30)
        p31 = self.package_hashtable.search(31)
        p32 = self.package_hashtable.search(32)
        p33 = self.package_hashtable.search(33)
        p34 = self.package_hashtable.search(34)
        p35 = self.package_hashtable.search(35)
        p36 = self.package_hashtable.search(36)
        p37 = self.package_hashtable.search(37)
        p38 = self.package_hashtable.search(38)
        p39 = self.package_hashtable.search(39)
        p40 = self.package_hashtable.search(40)

        # Load Truck 1
        t1.package_collection = [p4, p5, p7, p12, p13, p14, p15, p16, p19,
                                 p20, p21, p29, p31, p34, p37, p40]

        t1.package_id_collection = [4, 5, 7, 12, 13, 14, 15, 16, 19, 20,
                                    21, 29, 31, 34, 37, 40]

        t1.package_visual_collection = [4, 5, 7, 12, 13, 14, 15, 16, 19, 20,
                                        21, 29, 31, 34, 37, 40]

        # Load Truck 2
        t2.package_collection = [p1, p2, p3, p6, p8, p10, p17, p18,
                                 p27, p28, p30, p32, p33, p35, p36, p38]

        t2.package_id_collection = [1, 2, 3, 6, 8, 10, 17, 18, 27, 28, 30, 32,
                                    33, 35, 36, 38]

        t2.package_visual_collection = [1, 2, 3, 6, 8, 10, 17, 18, 27, 28, 30,
                                        32, 33, 35, 36, 38]

        # Load Truck 3
        t3.package_collection = [p9, p11, p22, p23, p24, p25, p26, p39]

        t3.package_id_collection = [9, 11, 22, 23, 24, 25, 26, 39]

        t3.package_visual_collection = [9, 11, 22, 23, 24, 25, 26, 39]


if __name__ == "__main__":
    main = Main()
    main.main()
