#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

# The first step is to define the function that takes in a string and an integer
# declare a variable and start it off as an empty string
# create a for-loop that goes as many times as the imputed integer
#on each loop, add the inputed string to the variable. return the variable

def string_times(string, num):
  answer = ''
  for i in range(0, num):
    answer += string

  return answer

# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

# first step is to define the function that takes in a string
# next step is to write a list comprehension that returns a string of only every other letter. This returns a list of letters.
#add the letters together to make a word

def string_bits(string):
  answer = [x for ind, x in enumerate(string) if ind%2==0]
  final_answer = ''
  for letter in answer:
    final_answer += letter
  return final_answer


#Given a non-empty string like "Code" return a string like "CCoCodCode"

# the first step is to define a function that takes in a string
# next is asign a variable to an empty string to hold the answer
# for loop that goes over ever letter of the string
# each for loop adds every index befor it to the final string

def string_splostion(string):
  temp_string = ''
  answer = ''
  for letter in string:
    temp_string += letter
    answer += temp_string

  return answer




