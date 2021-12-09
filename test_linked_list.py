from data_structures.singly_linked_list import Node, SinglyLinkedList

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