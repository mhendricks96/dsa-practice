class TreeNode:
  def __init__(self, value=None, right_child=None, left_child=None):
    self.value = value
    self.right_child = right_child
    self.left_child = left_child

  def add(self, new_value):

    if self.value == new_value:
      pass
      return

    if self.value > new_value:
      if self.left_child:
        self.left_child.add(new_value)
      else:
        self.left_child = TreeNode(new_value)
    else:
      if self.right_child:
        self.right_child.add(new_value)
      else:
        self.right_child = TreeNode(new_value)

  def pre_order_traversal(self, values=[]):

    values.append(self.value)

    if self.left_child:
      self.left_child.pre_order_traversal(values)

    if self.right_child:
      self.right_child.pre_order_traversal(values)
    
    return values