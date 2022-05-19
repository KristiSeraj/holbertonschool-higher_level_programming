#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """__init__ initialize Node class and its properties
    Args:
        data: int
        next_node: link to next node
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the instance attribute for data"""

        return self.__data

    @property
    def next_node(self):
        """Retrieves the instance attribute for next node"""

        return self.__next_node

    @data.setter
    def data(self, value):
        """Sets value to data and checks for errors"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Sets value to next_node and checks for errors"""

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """__init__ initializes SinglyLinkedList class"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        """Prints the entire list in stdout converted to str
        Return:
            returns values (list)
        """
        tmp = self.__head
        values = []

        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position
        in the list
        Args:
            value (int): data of the new Node
        """
        newNode = Node(value)
        if self.__head is None:
            newNode.next_node = None
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            tmpNode = self.__head
            while tmpNode.next_node is not None\
                    and tmpNode.next_node.data < value:
                tmpNode = tmpNode.next_node
            newNode.next_node = tmpNode.next_node
            tmpNode.next_node = newNode
