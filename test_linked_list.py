from data_structures.singly_linked_list import Node, SinglyLinkedList
from problems.linked_list_functions import return_duplicates, find_max_recursively, merge_opposite, find_middle

def test_create_node():
  my_node = Node(99)
  actual = my_node.value
  expected = 99
  assert actual == expected

def test_node_instance_wrong_value():
    node = Node('apples', None)
    actual = node.value
    expected = 'oranges'
    assert actual != expected

def test_create_list():
  my_list = SinglyLinkedList()
  my_list.insert(1)
  actual = str(my_list)
  expected = "{1} -> NONE"
  assert actual == expected

def test_create_and_add():
  my_list = SinglyLinkedList()
  my_list.insert(1)
  my_list.insert(2)
  my_list.insert(3)
  actual = str(my_list)
  expected = "{3} -> {2} -> {1} -> NONE"
  assert actual == expected

def test_return_duplicate():
  my_list = SinglyLinkedList()
  my_list.insert(1)
  my_list.insert(2)
  my_list.insert(3)
  my_list.insert(4)
  my_list.insert(2)
  my_list.insert(3)
  actual = return_duplicates(my_list)
  expected = [3,2]
  assert actual == expected

def test_recursive_max():
  my_list = SinglyLinkedList()
  my_list.insert(1)
  my_list.insert(5)
  my_list.insert(9)
  my_list.insert(77)
  my_list.insert(12)
  my_list.insert(3)
  actual = find_max_recursively(my_list)
  expected = 77
  assert actual == expected

def test_merge_opposite():
  my_list1 = SinglyLinkedList()
  my_list1.insert(5)
  my_list1.insert(3)
  my_list1.insert(1)
  my_list2 = SinglyLinkedList()
  my_list2.insert(10)
  my_list2.insert(7)
  my_list2.insert(6)
  my_list2.insert(2)
  actual = str(merge_opposite(my_list1, my_list2))
  expected = "{10} -> {7} -> {6} -> {5} -> {3} -> {2} -> {1} -> NONE"
  assert actual == expected

def test_find_middle():
  my_list1 = SinglyLinkedList()
  my_list1.insert(5)
  my_list1.insert(3)
  my_list1.insert(1)
  my_list1.insert(10)
  my_list1.insert(7)
  my_list1.insert(6)
  my_list1.insert(2)
  actual = find_middle(my_list1)
  expected = 10
  #assert actual == expected