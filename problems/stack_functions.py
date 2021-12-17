from data_structures.ll_stack import Stack

# given a stack, find the sum of all elements iterively

def find_sum(stack):
  total = 0

  while not stack.is_empty():
    popped_value = stack.pop()
    total += popped_value
  
  return total

#find the length of the longest balanced parenthesis in a string

# define  a function that takes in a string of parenthesis.
#define a holding stack.
#define a variable to hold the longest streak that starts at 0
#push the first parenthesis onto the stack and go to the next one
# if the if the next parenthesis is the same, push it onto the stack and go to the next one
# if the next parenthesis is not the same, pop the top parenthesis from the stack and go to the next one in the string,

# def find_longest_parenthesis(string):
  
#   holding_stack = Stack()
#   longest_streak = 0
#   holding_stack.push(-1)
  
#   for letter in string:

#     if letter == '(':
#       holding_stack.push(letter)
#     else:
#       if not holding_stack.is_empty():
#         holding_stack.pop()
#       if not holding_stack.is_empty():
#         current_streak = 


  



