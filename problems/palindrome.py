# write a function to determine wheather or not a string is a palindrome

# i think i can place a pointer at the beginning and end of the string, compare them each and then move the pointers until the meet.

# define the function that takes in a string
# assign the first and last indexes to variables called front and back
# create a while loop that goes until the front variable is equal to or higher than the back variable
# compare the letter at each of the pointers for equality at each step. if the are not equal, return false, if they are equal, continue on.
# each time through, move the front pointer forward and the back pointer back
# if you reach the end of the loop, the word is a palindrome, so return true

def find_palindrome(string):
  front_index = 0
  back_index = len(string) - 1
  
  while front_index < back_index:
    front_letter = string[front_index]
    back_letter = string[back_index]
    if front_letter != back_letter:
      return('Not a Palindrome')
    
    front_index += 1
    back_index -= 1

  print('Palindrome')
