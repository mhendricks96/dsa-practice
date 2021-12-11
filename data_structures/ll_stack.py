#from data_structures.singly_linked_list import SinglyLinkedList

class Stack:

  class Node:
    def __init__(self, value=None, next=None):
      self.value = value
      self.next = next
  
  def __init__(self, top=None):
    self.top = top
    self.stack_size = 0
  
  def __len__(self):
    return self.stack_size
  
  def is_empty(self):
    if self.stack_size == 0:
      return True
    return False

  def push(self, value):
    self.top = self.Node(value, self.top)
    self.stack_size += 1

  def pop(self):
    if self.stack_size == 0:
      return('stack is empty')
    else:
      popped = self.top.value
      self.top = self.top.next
      self.stack_size -= 1
    
      return popped
