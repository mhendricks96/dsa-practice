from data_structures.binary_tree import TreeNode

# given a binary tree, find the maximum value 

def tree_max(tree_root):
  values_list = tree_root.pre_order_traversal()
  maximum = values_list[0]
  for number in values_list:
    if number > maximum:
      maximum = number
  
  return maximum

# given 2 binary trees, return true if they are identical and false if they are not.


# if you have reached the bottom of both trees, return false.
#compare the values of the root of both trees, if they are identical recursively run function on each side

def compare_trees(tree1, tree2):
  '''function'''
  
  if tree1 is None and tree2 is None:
    return True

  if tree1 is not None and tree2 is not None:
    return ((tree1.value == tree2.value) and compare_trees(tree1.left_child, tree2.left_child) and compare_trees(tree1.right_child, tree2.right_child))
  
  return False


  # if tree1.value != tree2.value:
  #   return False
  
  # if tree1.left_child:
  #   print(tree1.value)
  #   return compare_trees(tree1.left_child, tree2.left_child)

  # if tree1.right_child:
  #   print(tree1.value)
  #   return compare_trees(tree1.right_child, tree2.right_child)
  
  # return True
  