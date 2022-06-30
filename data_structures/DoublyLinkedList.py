import gc
from Node import Node


class DoublyLinkedList:
    def __init__(self):
        '''
        Initialize a linked list with head as None

        Parameters:
            None

        Returns:
            None
        '''
        self.head = None
        self.tail = None

    def push(self, new_data) -> None:
        '''
        Insert a new node at the beginning of the linked list.

        Parameters:
            new_data (any): data to be stored in the node

        Returns:
            None
        '''
        # Create a new node with the new_data
        new_node = Node(new_data)

        # Make the new node as head and previous of the node as None
        new_node.next = self.head
        new_node.prev = None

        # Make the previous node of head node to new node
        if self.head is not None:
            self.head.prev = new_node

        # Make the head node as new node
        self.head = new_node

    def insert_after(self, prev_node, new_data) -> None:
        '''
        Insert a new node after a given node

        Parameters:
            prev_node (Node): node before the new node
            new_data (any): data to be stored in the node

        Returns:
            None
        '''
        # If the previous node is None, then raise an error
        if prev_node is None:
            raise Exception(
                "Previous node cannot be None and must be in the DoublyLinkedList.")

        # Create a new node with the new_data
        new_node = Node(new_data)

        # Make the head of new node as next of the previous node
        new_node.next = prev_node.next

        # Make the next of previous node as the new node
        prev_node.next = new_node

        # Make the previous node as the previous node of new node
        new_node.prev = prev_node

        # If the new node is the last node, then make the new node as the tail node
        if new_node.next is None:
            self.tail = new_node

    def append(self, new_data) -> None:
        '''
        Append a new node at the end of the linked list.

        Parameters:
            new_data (any): data to be stored in the node

        Returns:
            None
        '''
        # Create a new node with the new_data
        new_node = Node(new_data)
        last = self.head

        # As the new node is going to be the last node, the next of it will be None
        new_node.next = None

        # If the linked list is empty, then make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # Find the last node of the linked list
        while last.next is not None:
            last = last.next

        # Make the last node as next of the new node
        last.next = new_node

        # Make the last node as previous node of new node
        new_node.prev = last

    def delete_node(self, key) -> None:
        '''
        Delete a node from the linked list.

        Parameters:
            key (any): data to be deleted from the linked list

        Returns:
            None
        '''
        # If linked list is empty
        if self.head is None or key is None:
            raise Exception('Linked list is empty or key is None.')

        # Check if the head is equal to key
        if self.head == key:
            self.head = key.next

        # Change the next if the key is NOT the last node
        if key.next is not None:
            key.next.prev = key.prev

        # Change the previous if the key is NOT the first node
        if key.prev is not None:
            key.prev.next = key.next

        # Call the Garbage Collector
        gc.collect()

    def print_list(self, node: Node) -> None:
        '''
        Print the linked list

        Parameters:
            node (Node): node to start from

        Returns:
            None
        '''
        while node is not None:
            print(node.data, end=' ')
            node = node.next


if __name__ == '__main__':
    dllist = DoublyLinkedList()

    dllist.push(2)
    dllist.push(4)
    dllist.push(8)
    dllist.push(12)

    print('\nOriginal Doubly Linked List: ', end='\n')
    dllist.print_list(dllist.head)

    dllist.delete_node(dllist.head)
    dllist.delete_node(dllist.head.next)
    dllist.delete_node(dllist.head.next)

    print('\nDoubly Linked List after removing of nodes: ', end='\n')
    dllist.print_list(dllist.head)
