from data_structures.singly_linked_list import Node, SinglyLinkedList

# given a linked list, return a list of all duplicate values


def return_duplicates(linked):
  answer = []
  values_dict = {}
  current = linked.head

  while current is not None:
    if current.value in values_dict:
      values_dict[current.value] += 1
    else:
      values_dict[current.value] = 1
    current = current.next
  
  for item in values_dict:
    if values_dict[item] > 1:
      answer.append(item)
  
  return answer


#given a linked list, find the maximum value recursively

def find_max_recursively(linked):
  
  def recursive_part(node, max_value):
    
    if node.value > max_value:
      max_value = node.value
    
    if node.next is None:
      return max_value
    else:
      return recursive_part(node.next, max_value)

  max_value = recursive_part(linked.head, linked.head.value)
  
  return max_value

#Merge two sorted linked lists from their end

#For example, consider lists a = {1, 3, 5} and b = {2, 6, 7, 10}. Merging both lists should yield the list {10, 7, 6, 5, 3, 2, 1}.


def merge_opposite(ll1, ll2):
  new_ll = SinglyLinkedList()

  ll1_pointer = ll1.head
  ll2_pointer = ll2.head
  
  while ll1_pointer and ll2_pointer:
    
    if ll1_pointer.value < ll2_pointer.value:
      new_ll.insert(ll1_pointer.value)
      ll1_pointer = ll1_pointer.next

    elif ll2_pointer.value < ll1_pointer.value:
      new_ll.insert(ll2_pointer.value)
      ll2_pointer = ll2_pointer.next

  while ll1_pointer:
    new_ll.insert(ll1_pointer.value)
    ll1_pointer = ll1_pointer.next

  while ll2_pointer:
    new_ll.insert(ll2_pointer.value)
    ll2_pointer = ll2_pointer.next
  
  return new_ll

# find the middle of a linked list using 2 pointers (fast and slow)

# define a function that takes in a linked list
# create a variable for a slow pointer
# create a variable for fast pointer
# create a while loop that goes until the fast pointer ends
# every iteration the fast pointer moves 2 nodes and the slow pointer moves 1 node
# return the value of the node the first pointer is at

def find_middle(linked):
  slow_pointer = linked.head
  fast_pointer = linked.head

  while fast_pointer:
    fast_pointer = fast_pointer.next.next
    slow_pointer = slow_pointer.next
  
  return slow_pointer.value

  

  