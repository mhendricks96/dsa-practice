# given a list, reverse the values iteratively

# define a function that takes in a list. make a new list to hold the list
# create a variable to hold the length of the list.
# start a while loop that goes as long as the list is not empty.
# each time through, ad the last index of the first list to the new list and lower the length by 1
def reverse_list(s_list):
  reversed_list = []
  length = len(s_list)

  while length > 0:
    reversed_list.append(s_list[length - 1])
    length -= 1

  return reversed_list