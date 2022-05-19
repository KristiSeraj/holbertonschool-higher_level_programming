#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        tmp = self.__head
        values = []
        
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)

    def sorted_insert(self, value):
        newNode = Node(value)
        if self.__head is None:
            newNode.next_node = None
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            tmpNode = self.__head
            while tmpNode.next_node != None and tmpNode.next_node.data < value:
                tmpNode = tmpNode.next_node
            newNode.next_node = tmpNode.next_node
            tmpNode.next_node = newNode
