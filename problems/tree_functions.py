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


def compare_trees(tree1, tree2):
  '''function'''
  
  if tree1 is None and tree2 is None:
    return True

  if tree1 is not None and tree2 is not None:
    return ((tree1.value == tree2.value) and compare_trees(tree1.left_child, tree2.left_child) and compare_trees(tree1.right_child, tree2.right_child))
  
  return False


  # check if a binary tree is a sum tree or not(each nodes value is the same as the sum of all of its childrens values)

  # define a function that takes in a tree
  # do a post order traversal on the tree.
  # each "tree" keeps a total of the values before it
  # make sure that "total" == the nodes values

  def check_if_sum(tree):
    
    sum = 0

    if tree.left_child:
      sum += tree.left_child.value
      check_if_sum(tree.left_child)

    if self.right_child:
      sum += tree.right_child.value
      check_if_sum(tree.right_child)
    
    if sum != tree.value:
      return False
    

    return True