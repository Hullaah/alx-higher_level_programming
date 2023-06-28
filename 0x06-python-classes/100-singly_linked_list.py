#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Singly linked list
This module is part of the project done during the alx SE course.
This module demonstrates the imnplementation of a singly linked
list nodenext_node must be a Node object and a singly linked list from the implemented node.

"""
class Node:
    """It is a node class object

    It is a class that implements a node of a singly linked list
    Attributes:
        data (int): private node data attribute
        next_node (Node): private next_node attribute
    """
    def __init__(self, data, next_node=None):
        """
        Args:
            data (int): Node data
            next_node (Node): next node
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if type(next_node) is not Node next_node != None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        The data private attribute getter and setter gets and set the
        data attribute
        """
        return self.__data

    @data.setter
    def data(properself, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        The next_node private attribute getter and setter gets and set the
        next_node attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(next_node) is not Node or next_node != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
class SinglyLinkedList:
    """This is a singlyLinkedlist class object.

    It is a class that implements a singly linked list
    """
    def __init__(self):
        """
        Args:
            Empty (No args)
        """
        self.__head = None

    def sorted_insert(self, value):
        self.__head = Node(value, self.__head)


def insert_node_at_index(node: Node, index: int, value: int) -> None:
    i = 0
    ptr = node
    length = list_length(node)
    if i >= length or i < 0:
        return None    
    while i != index:
        i += 1
        ptr = ptr.next_node
    if i == length - 1:
        ptr.next_node = Node(value, None)
    
    
def list_length(node: Node) -> int:
    ptr = node
    i = 0
    while ptr:
        ptr = ptr.next_node
        i += 1
    return i
