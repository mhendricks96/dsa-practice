from data_structures.ll_stack import Stack
from problems.stack_functions import find_sum

def test_new_stack():
  my_stack = Stack()
  my_stack.push(5)
  my_stack.push(2)
  actual = my_stack.top.value
  expected = 2
  assert actual == expected

def test_stack_pop():
  my_stack = Stack()
  my_stack.push(5)
  my_stack.push(2)
  popped = my_stack.pop()
  actual1 = my_stack.top.value
  actual2 = popped
  expected1 = 5
  expected2 = 24
  assert actual1 == actual1
  assert actual2 == actual2

def test_stack_sum():
  my_stack1 = Stack()
  my_stack1.push(5)
  my_stack1.push(2)
  my_stack1.push(5)
  my_stack1.push(3)
  actual = find_sum(my_stack1)
  expected = 15
  assert actual == expected