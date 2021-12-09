# given a linked list, return a list of all duplicate values

#define a function that takes in a linked list
#define an empty list to hold answer
# set up an empty dictionary to hold the values and their counts
# set up a while loop that goes until a node is none
# each node, check to see if its value is in the dictionary as a key. if so, add 1 to its value. if not add it with a value of 1
#check every key in the dictionary. if its value is more than 1, add it to the list
# return the list

def return_duplicates(linked):
  answer = []
  values_dict = {}
  current = linked.head

  while current is not None:
    if current.value in values_dict:
      values_dict[current.value] += 1
    else values_dict[current.value] = 1
    current = current.next
  
  for item in values_dict:
    if values_dict[item] > 1:
      answer.append(item)
  
  return answer