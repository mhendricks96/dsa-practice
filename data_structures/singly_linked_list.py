class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def __len__(self):
    return self.length
    
  def __str__(self):
      string = ""
      current = self.head
      while current is not None:
          string += f"{ {current.value} } -> "
          current = current.next

      string += f"NONE"
      return string
  
  def insert(self, value):
    node = Node(value)

    if self.head is not None:
      node.next = self.head
    self.head = node
    self.length += 1