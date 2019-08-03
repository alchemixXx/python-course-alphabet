import unittest
from typing import List


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def convert_list_to_linkedlist(data: List) -> List[Node]:
    list_of_nodes = []
    prev = None
    for data_value in data:
        node = Node(data=data_value)
        if prev:
            prev.next = node
        prev = node
        list_of_nodes.append(node)
    return list_of_nodes


class TestConvertListToLinkedlist(unittest.TestCase):
    """
    1. тип возвращаемого значения
    2. кол-во элементов сравнить с исходным list
    3. тип значений в возвращаемом list
    4. проверить цепочку нод
    """

    def test_data_consistency(self):
        data_to_convert = [1, 2, 3]
        expected_data_value = [1, 2, 3]
        expected_next_value = [2, 3, None]
        actual_result = convert_list_to_linkedlist(data_to_convert)
        self.assertTrue(actual_result)

        for node, data, next_data in zip(actual_result, expected_data_value,
                                         expected_next_value):
            self.assertEqual(node.data, data)
            if node.next:
                self.assertEqual(type(node.next.data), type(next_data))
                self.assertEqual(node.next.data, next_data)