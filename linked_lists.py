# This is an introduction to linked lists in python

# Initiate Node class
class Node:

    # initiate what a node is, and what attributes it has, in this case it is a singly linked list
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # methods

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        self.length += 1

    def print(self):
        if self.head is None:
            print("Null")
            return

        curr = self.head
        list_string = ""

        while curr:
            list_string += str(curr.data) + "-->"
            curr = curr.next
        print(list_string)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.length = 1
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)
        self.length += 1

    # new list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # as a check
    def get_length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def remove_at_index(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Invalid Index")
        self.length -= 1
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        curr = self.head
        while curr:
            if count == index - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.length:
            raise Exception("Invalid Index")
        self.length += 1
        if index == 0:
            self.insert_at_begining(data)

        count = 0
        curr = self.head

        while curr:
            if count == index - 1:
                new_node = Node(data, curr.next)
                curr.next = new_node
            curr = curr.next
            count += 1


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_begining(2)
    linked_list.insert_at_begining(1)
    linked_list.insert_at_end(3)
    linked_list.insert_values(["a", "b", "c"])

    linked_list.remove_at_index(1)

    linked_list.insert_at(1, 2)

    print("length = " + str(linked_list.length))
    print("length = " + str(linked_list.get_length()))

    linked_list.print()