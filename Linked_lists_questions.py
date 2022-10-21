# Initiate singly linked list

# first need to create node class
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def add_Node(self, node):
        head = self.head
        if head is None:
            self.head = node
            return
        while head.next:
            head = head.next
        head.next = node

    def print(self):
        # if empty
        if self.head is None:
            print("None")
            return
        # else iterate through, adding elements to a resualt string
        list_string = ""
        curr = self.head
        while curr:
            list_string += str(curr.data) + "-->"
            curr = curr.next
        print(list_string)

    # add val to the front of the linked list
    def add_to_front(self, val):
        new_node = Node(val, self.head)
        self.head = new_node

    def add_to_end(self, val):
        new_node = Node(val, None)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node



    # question one - remove dupes

    # a function that removes all duplicate values from the linked list
    def remove_dupes(self):

        if self.head is None:
            return None

        prev = self.head
        curr = prev.next

        # vals
        vals = []

        vals.append(prev.data)

        while curr:
            if not curr.data in vals:
                vals.append(curr.data)

                curr = curr.next
                prev = prev.next
            else:
                prev.next = curr.next
                curr = curr.next

    # Question 2: remove_kth_to_last

    # uses two pointers, seprated by k elements to remove the k to last element in time O(N), obvious edge case is if k is greater than the length of the list, I need to make it work for first element
    def remove_kth_to_last(self, k):
        # p2 is the pointer in front, followed by p1 (k nodes off), followed by p0 (one extra node off)

        p1 = self.head
        p2 = self.head

        # previous to p1 so that I can remove it
        p0 = Node(None, self.head)

        sepration = 0

        while p2:
            while p2 and sepration <= k:
                p2 = p2.next
                sepration += 1
            # now p1 and p2 have a sepration of k, when p2 hits the end, p1 will be on the k to last element
            p1 = p1.next
            p2 = p2.next

            p0 = p0.next
        p0.next = p1.next

    # Question 3: Remove middle node

    # remove node given, which is not at the start of end of the linked list. This is done by updating the value of that node, then remving the next one from the chain
    def remove_middle_node(self, node_to_remove):
        if node_to_remove is None:
            return
        node_to_remove.data = node_to_remove.next.data
        node_to_remove.next = node_to_remove.next.next
        return

    # Question 4: Partition the list at a value of x, with all values before x at one side, and all other values on the other side
    def partition(self, x):
        # make two seprate lists that will be joined at the end
        front, back = LinkedList(), LinkedList()
        front_end = Node() # to keep track of the end of the first list, for joining up after

        curr = self.head
        while curr:
            if curr.data < x:
                front.add_to_front(curr.data)
                if front_end is None:
                    front_end = front.head
                else:
                    front_end = front_end.next
            else:
                back.add_to_front(curr.data)
            curr = curr.next

        #join the lists up, then set this new list to the original one
        front_end.next = back.head
        l4.head = front.head

    # Question 5: Sum two lists soted in reversed order
    def sum_lists(self, lst_1, lst_2):

        l1, l2 = lst_1.head, lst_2.head

        digit, carry = 0, 0

        resualt = LinkedList()

        while l1 and l2:
            total = l1.data + l2.data
            digit = total % 10 + carry

            resualt.add_to_end(digit)

            carry = total // 10

            l1, l2 = l1.next, l2.next

        if l1 or l2:
            if l1:
                rest = l1
            else:
                rest = l2
            while rest:
                resualt.add_to_end(rest.data)
                rest = rest.next
        return resualt

    # determine if two list intercect
    def intercection(self, other_list):
        h1, h2 = self.head, other_list.head

        seen = []

        while h1 and h2:
            if h1 in seen or h2 in seen:
                return True
            seen.append(h1)
            seen.append(h2)
            h1 = h1.next
            h2 = h2.next
        if h1:
            while h1:
                if h1 in seen:
                    return True
                h1 = h1.next
        if h2:
            while h2:
                if h2 in seen:
                    return True
                h2 = h2.next
        return False

    # find if a list has a loop in it, if it does return the head of the loops value
    def loop_detection(self):

        if self.head is None:
            return None

        head = self.head

        if not head.next and not head.next.next:
            return None

        slow, fast = head.next, head.next.next

        # let them run until they colide k steps from the end of the loop
        while slow.next and fast.next and fast.next.next and not slow == fast:
            slow = slow.next
            fast = fast.next.next

        if fast is None or fast.next is None or fast.next.next is None:
            return None

        # now set fast to head and increment at same steps untill they reach the head of the loop
        while not slow == head:
            slow = slow.next
            head = head.next
        return head.data


if __name__ == "__main__":
    print("Question 1: remove_dupes")
    linked_list = LinkedList()

    linked_list.add_to_front(3)
    linked_list.add_to_front(3)
    linked_list.add_to_front(2)
    linked_list.add_to_front(2)
    linked_list.add_to_front(2)
    linked_list.add_to_front(1)

    print("List before remove_dupes")
    linked_list.print()

    linked_list.remove_dupes()

    print("List after remove_dupes")
    linked_list.print()

    print("Question 2: return_kth_to_last")

    l2 = LinkedList()

    for i in range(9, -1, -1):
        l2.add_to_front(i)

    print("Before remove_kth_to_last (k = 2)")
    l2.print()

    print("After remove_kth_to_last_element (k = 2)")
    l2.remove_kth_to_last(2)
    l2.print()

    print("Question 3: remove a middle node, given that node only")

    print("List before node C is removed")
    l3 = LinkedList()

    l3.add_to_front("E")
    l3.add_to_front("D")
    l3.add_to_front("C")
    l3.add_to_front("B")
    l3.add_to_front("A")

    l3.print()

    print("List after node C is removed")

    # find node C so that it can be used as an input
    def get_adress():
        curr = l3.head
        while curr and not curr.data == "C":
            curr = curr.next
        return curr

    l3.remove_middle_node(get_adress())
    l3.print()

    print("Question 4: Partion the lists about a value, x")

    print("List before partion at x = 5")

    l4 = LinkedList()
    l4.add_to_front(1)
    l4.add_to_front(2)
    l4.add_to_front(10)
    l4.add_to_front(5)
    l4.add_to_front(8)
    l4.add_to_front(5)
    l4.add_to_front(3)

    l4.print()

    print("List after partition at x = 5")

    l4.partition(5)

    l4.print()

    print("Question 4: Sum Lists (Stored in reversed order)")

    lst_1, lst_2 = LinkedList(), LinkedList()

    lst_1.add_to_front(6)
    lst_1.add_to_front(1)
    lst_1.add_to_front(7)

    lst_2.add_to_front(2)
    lst_2.add_to_front(9)
    lst_2.add_to_front(5)

    print("Lists to be summed:")

    lst_1.print()
    lst_2.print()

    print("Resualt")
    lst_3 = lst_1.sum_lists(lst_1, lst_2)
    lst_3.print()

    print("Do question 6 after stacks")

    print("Question 7: Determine if two linked lists intersect")

    a, b = LinkedList(), LinkedList()

    # unique nodes
    a_nodes = [Node(3), Node(1), Node(5), Node(9)]
    b_nodes = [Node(4), Node(6)]

    # shared nodes
    node_of_intercection = Node(7)
    c_nodes = [Node(2), Node(1)]

    for node in a_nodes:
        a.add_Node(node)
    for node in b_nodes:
        b.add_Node(node)
    a.add_Node(node_of_intercection)
    b.add_Node(node_of_intercection)
    # only need to do this to one as they are intercecting now
    for node in c_nodes:
        a.add_Node(node)

    print("Where they both intercect at a node with value 7")
    a.print()
    b.print()

    print(a.intercection(b))

    print("Where they don't intercect")

    d, e = LinkedList(), LinkedList()


    d_nodes = [Node(3), Node(1), Node(5)]
    e_nodes = [Node(3), Node(1), Node(5)]

    for node in d_nodes:
        d.add_Node(node)
    for node in e_nodes:
        e.add_Node(node)

    d.print()
    e.print()

    print(d.intercection(e))

    print("Question 8: Find if a list has a loop in it, if so return the head of the loop")

    loop, no_loop = LinkedList(), LinkedList()

    nodes = [Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)]
    make_loop = Node(7, nodes[3])

    for node in nodes:
        loop.add_Node(node)
    loop.add_Node(make_loop)

    print("Where there is one")
    print(loop.loop_detection())

    print("Where there is not one")
    print(a.loop_detection())