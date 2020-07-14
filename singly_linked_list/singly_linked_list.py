"""
Linked list are an ordered collection of objects.

Each element of a linked list is called a node, and
every node has two different fields:

 - Data: contains the value to be stored in the node.

 - Next: contains a reference to the next node on the list.

 A linked list is therefore a collection of nodes. The first node being the head, and its the starting point for any iteration through the list. While the last node must have a reference pointing to None indicating the end of the list.

"""

# first create a class to represet a linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == '__main__':
    llist = LinkedList()
    llist

    first_node = Node('a')
    llist.head = first_node
    llist

    second_node = Node('b')
    third_node = Node('c')
    first_node.next = second_node
    second_node.next = third_node
    print(llist) # a -> b -> c -> None
