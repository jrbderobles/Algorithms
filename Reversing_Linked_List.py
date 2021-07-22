
# Python program to reverse a linked list
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    # Function to reverse the Linked_List (Iterative Method)
    def reverse_iterative(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to reverse the Linked_List (Recursive Method)
    def reverse_recursive(self, current):
        # If head is empty or has reached the list end
        if (current is None) or (current.next is None):
            self.head = current
            return

        # Reverse the rest list
        self.reverse_recursive(current.next)

        # Put first element at the end
        current.next.next = current
        current.next = None

    # Function to insert a new node at the beginning
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # Utility function to print the Linked_List
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next

sample_linked_list = Linked_List()
sample_linked_list.push(20)
sample_linked_list.push(4)
sample_linked_list.push(15)
sample_linked_list.push(85)
sample_linked_list.print_list()
print('\n\n')

sample_linked_list.reverse_iterative()
sample_linked_list.print_list()
print('\n')

sample_linked_list.reverse_recursive(sample_linked_list.head)
sample_linked_list.print_list()
