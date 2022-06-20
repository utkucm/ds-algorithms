class Node:

    def __init__(self, data, next=None, prev=None) -> None:
        '''
        Initialize a node with data and next as None

        Parameters:
            data (any): data to be stored in the node

        Returns:
            None
        '''
        self.data = data
        self.prev = prev
        self.next = None
