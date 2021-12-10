from data_structures.binary_tree import TreeNode

def test_create_node():
  my_node = TreeNode(99)
  actual = my_node.value
  expected = 99
  assert actual == expected

def test_add_node():
  my_node = TreeNode(77)
  my_node.add(44)
  my_node.add(33)
  actual2 = my_node.left_child.value
  expected2 = 44
  assert actual2 == expected2

def test_pre_order():
  my_node = TreeNode(77)
  my_node.add(44)
  my_node.add(33)
  my_node.add(1)
  my_node.add(2)
  actual = my_node.pre_order_traversal()
  expected = [77, 44, 33, 1, 2]
  assert actual == expected
  