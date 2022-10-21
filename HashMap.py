# This is an introduction to HashMaps in Python

# this handles colisions with a linked list

class HashTable:
    def __init__(self, size=100):
        # allocate an array of a given size for the storing of items in the HashMap
        self.size = size
        self.arr = [[] for i in range(self.size)]

    # methods

    # hash function to map keys to values
    def hash_function(self, key):
        hash_total = 0
        for char in key:
            hash_total += ord(char)
        return hash_total % self.size


    # the next two methods take advantage of the standard set items

    # add value
    def __setitem__(self, key, val):
        hash_total = self.hash_function(key)

        found = False

        # when you want to update value, if confusing debug this block


        # element = (key, value), if that key, value tuple pair exsits, replace it. if not append in the later code
        for i, element in enumerate(self.arr[hash_total]):
            # this is the case where an element with that key already exsits, so you just update it
            if len(element) == 2 and element[0] == key:
                # as a tuple you have to insert a brand new one
                self.arr[hash_total][i] = (key, val)
                found = True # sorted, i.e. finish the function
                break

        # if it does not already exsits this will either add a new tuple to the end of the list or add a fresh one
        if not found:
            self.arr[hash_total].append(((key, val)))

    # to get a value from a key
    def __getitem__(self, key):
        hash_total = self.hash_function(key)

        for element in self.arr[hash_total]:
            if element[0] == key:
                return element[1]


    def __delitem__(self, key):
        hash_total = self.hash_function(key)

        for i, element in enumerate(self.arr[hash_total]):
            if element[0] == key:
                del self.arr[hash_total][i]


if __name__ == "__main__":
    ht = HashTable(10)

    ht["march 6"] = 120
    ht["march 8"] = 67
    ht["march 9"] = 4

    print(ht.arr)

    print("update the march 6 value")
    ht["march 6"] = 100
    print(ht.arr)


    ht["march 17"] = 459

    print("colision has occoured with march 6")
    print(ht.arr)

    print(ht["march 17"])

    del ht["march 6"]

    print(ht["march 6"])

    print(ht.arr)

    del ht["march 17"]

    print(ht["march 6"])

    print(ht.arr)