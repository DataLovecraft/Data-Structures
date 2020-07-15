"""
Linked list are an ordered collection of objects.

Each element of a linked list is called a node, and
every node has two different fields:

 - Data: contains the value to be stored in the node.

 - Next: contains a reference to the next node on the list.

A linked list is therefore a collection of nodes. The first node being the head, and its the starting point for any iteration through the list. While the last node must have a reference pointing to None indicating the end of the list.

"""

class Node:
    '''
    Object representing a node

    '''
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    '''
    Object representing a linked list

    '''
    def __init__(self, nodes=None):
        # Start of list
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        '''
        Method iterates through the list and yelds every single
        node. Method always validates that the current node
        is not None. When this condition is True, it means
        we've reached the end of the linked list.

        '''
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Inserting a new node at the beginning of a list
    def add_first(self, node):
        '''
        Here we are setting self.head as the next reference to the new
        node so that the new node points to the old self.head.
        Next we need to state that the new head of the list is the
        inserted node

        '''
        node.next = self.head
        self.head = node

    # Inserting a new node at the end of a list
    def add_last(self, node):
        '''
        Method to insert a new node at the end of the list.
        This forces us to traverse the whole linked list first
        and to add the new node when you reach the end.

        '''
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        '''
        Method that adds a node after existing node with a specific value

        '''
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f'Node with data {target_node_data} is not found')

    def add_before(self, target_node_data, new_mode):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_fist(new_mode)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_mode
                new_mode.next = node
                return
            prev_node = node

        raise Exception(f'Node with data {target_node_data} not found')

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f'Node with data {target_node_data} not found')


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == '__main__':
    print("Creating a linked list: ")
    llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
    print(llist)

    #for node in llist:
    #    print(node)
    print("Inserting 'f' to the first node: ")
    llist.add_first(Node('f'))
    print(llist)

    print("Inserting 'g' to the last node:  ")
    llist.add_last(Node('g'))
    print(llist)

    print("Inserting 'h' after 'f': ")
    llist.add_after('f', Node('h'))
    print(llist)

    print("Inserting 'i' before 'g': ")
    llist.add_before('g', Node('i'))
    print(llist)

    print("Removing 'a' fron node: ")
    llist.remove_node('a')
    print(llist)
