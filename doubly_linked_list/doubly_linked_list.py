"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


class Node:
    def __init__(self, data):
        self.data = data    # stores the data
        self.nref = None    # stores the reference to the next node
        self.pref = None    # stores the reference to the previous node

    def __repr__(self):
        return self.data

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        pass

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        pass

class DoublyLinkedList:
    '''
    Object representings a Doubly Linked List
    '''
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.nref = Node(data=elem)
                node = node.nref

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, node):
        node.nref = self.head
        self.head = node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self): # redundant see 'remove_node'
        pass

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, node):
        if not self.head:
            self.head = node
        for current_node in self:
            pass
        current_node.nref = node

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self): # redundant see 'remove_node'
        pass

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.head = self.head.nref
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.nref = node.nref
                return
            previous_node = node

        raise Exception(f'Node with data {target_node_data} not found')

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        max_ = self.value
        for item in max_:
            if item > max_:
                max_ = item
        return max_

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.nref     # we are still iterating forward only


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.nref
        nodes.append("None")
        return " -> ".join(nodes)
