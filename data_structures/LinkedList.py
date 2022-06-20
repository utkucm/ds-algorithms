from Node import Node


class LinkedList:

    def __init__(self) -> None:
        '''
        Initialize a linked list with head as None

        Parameters:
            None

        Returns:
            None
        '''
        self.head = None

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

        # Make the new node as next of the previous node
        new_node.next = self.head

        # Make the previous node as next of the new node
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
                "Previous node cannot be None and must be in the LinkedList.")

        # Create a new node with the new_data
        new_node = Node(new_data)

        # Make the new node as next of the previous node
        new_node.next = prev_node.next

        # Make the previous node as next of the new node
        prev_node.next = new_node

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

        # If the linked list is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return

        # Find the last node of the linked list
        last = self.head
        while last.next:
            last = last.next

        # Append the new node to the end of the linked list
        last.next = new_node

    def delete_node(self, key) -> None:
        '''
        Delete a node from the linked list.

        Parameters:
            key (any): data to be deleted from the linked list

        Returns:
            None
        '''
        # If linked list is empty
        if self.head is None:
            raise Exception('Linked list is empty.')

        # Store head node to temp
        temp = self.head

        # If the node to be deleted is head, then make the next node as head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Search for the Node to be deleted, keep track of the previous node as the next of prev Node needs to be updated
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If the key to be deleted is not present in the linked list
        if temp is None:
            raise Exception('The key is not present in the linked list.')

        # Unlink the node from the linked list
        prev.next = temp.next

        temp = None

    def print_list(self) -> None:
        '''
        Print the linked list

        Parameters:
            None

        Returns:
            None
        '''
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()

    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)

    llist.insert_after(llist.head.next, 3)
    llist.print_list()
    print('-----------------------------------------------------')
    llist.delete_node(1)
    llist.print_list()
