from __future__ import annotations


class ChainingHashTable:
    """
    A chaining hash table. This data structure stores items by mapping each item
    to a location in an array. This data structure uses a hash function to
    compute the bucket index from the item's key.
    This type of hash table uses chaining to handle collisions.
    Each element in the hash table is called a bucket. Each bucket
    is a list of lists of items (key-value pairs).
    If the hash function returns a bucket index
    that is already occupied, the key-value pair is added to the occupied bucket
    at the next index.

    Adapted from  C950 - Webinar-1 - Let’s Go Hashing.

    === Instance Attributes ===
    table: A list that represents the chaining hash table. This list holds
    other lists that represent buckets

    capacity: An integer that represents the maximum number of buckets in
    the hash table

    size: An integer that represents the number of occupied buckets in the
    hash table

    MAX_LOAD_FACTOR: A float constant that represents the load factor: the ratio
    between the size of the hashtable and the capacity of the hash table
    """
    # Chaining hash table code adapted from
    # Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
    # Modified for key-value

    table: list
    capacity: int
    size: int
    MAX_LOAD_FACTOR: float  # Constant value: The load factor threshold

    # Name: __init__
    # Function: Initializes constructor for ChainingHashTable class
    # Time Complexity: O(1)
    # Space Complexity: O(n)

    def __init__(self, capacity: int = 10):
        """
        Initialize chaining hash table.

        Each chaining hash table is a list of lists. Each list of lists
        appended to the table is a bucket that can hold multiple items.
        """

        # Initialize chaining hash table with the amount of buckets noted in
        # the hash table instance. If no capacity is inputted, the hash table
        # will default to start with 10 buckets.
        self.MAX_LOAD_FACTOR = 0.75
        self.table = []
        self.capacity = capacity
        self.size = 0
        for i in range(capacity):
            self.table.append([])

    # Name: insert
    # Function: Inserts key-value pair into hash table
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def insert(self, key, item):
        # Compute the index of the bucket list where this item will be placed
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Update the value associated with the key if the key is already in
        # the bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # If the key is not in the bucket list, add the item
        # to the end of the bucket list

        key_value = [key, item]
        bucket_list.append(key_value)
        self.size += 1

        # The load factor is the fraction of the hash table that is full
        load_factor = self.size / self.capacity

        # Check the load factor and resize the hash table if necessary
        # If the load factor is greater than MAX_LOAD_FACTOR 0.75,
        # the hash table will resize

        if load_factor > self.MAX_LOAD_FACTOR:
            self.resize()
        return True

    # Name: search
    # Function: Find and return the value associated with the key
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def search(self, key):
        # Compute the index of the bucket list where this key will be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        for kv in bucket_list:
            # print(key_value)
            if kv[0] == key:
                return kv[1]  # value of the key-value pair
        return None

    # Name: remove
    # Function: Find key-value pair in hashtable and delete it
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def remove(self, key):
        # Compute the index of the bucket list where this item will be removed
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # If item is present, remove it from the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    # Name: resize
    # Function: If the load factor of the hashtable is greater than 0.75, double
    # the capacity of the hashtable to prevent collisions
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def resize(self):
        # Double the capacity of the hash table
        new_capacity = self.capacity * 2
        # Save old table in temp variable
        old_table = self.table
        # Create a new empty table
        self.table = []
        for i in range(new_capacity):
            self.table.append([])

        self.capacity = new_capacity
        self.size = 0

        # Rehash all items in the old hash table and put them into the new table
        for bucket in old_table:
            for key, item in bucket:
                self.insert(key, item)


# Test
"""
bestMovies = [
    [1, "CITIZEN KANE - 1941"],
    [2, "CASABLANCA - 1942"],
    [3, "THE GODFATHER - 1972"],
    [4, "GONE WITH THE WIND - 1939"],
    [5, "LAWRENCE OF ARABIA - 1962"],
    [6, "THE WIZARD OF OZ - 1939"],
    [7, "THE GRADUATE - 1967"],
    [8, "ON THE WATERFRONT- 1954"],
    [9, "SCHINDLER'S LIST -1993"],
    [10, "SINGIN' IN THE RAIN - 1952"],
    [11, "STAR WARS - 1977"]
]

myHash = ChainingHashTable()

print("\nInsert:")
myHash.insert(bestMovies[0][0],
              bestMovies[0][1])  # 2nd bucket; Key=1, item="CITIZEN KANE - 1941"
print(myHash.table)

myHash.insert(bestMovies[10][0], bestMovies[10][
    1])  # 2nd bucket as well; Key=11, item="STAR WARS - 1977"
print(myHash.table)

print("\nSearch:")
print(myHash.search(1))  # Key=1, item="CITIZEN KANE - 1941"
print(myHash.search(
    11))  # Key=11, item="STAR WARS - 1977"; so same bucket and Chainin is working

print("\nUpdate:")
myHash.insert(1,
              "Star Trek - 1979")  # 2nd bucket; Key=1, item="Star Trek - 1979"
print(myHash.table)

print("\nRemove:")
myHash.remove(1)  # Key=1, item="Star Trek - 1979" to remove
print(myHash.table)

myHash.remove(11)  # Key=11, item="STAR WARS - 1977" to remove
print(myHash.table)
"""
