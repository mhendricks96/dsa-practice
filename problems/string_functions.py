#Given a string and a non-negative int n, return a larger string that is n copies of the original string.


def string_times(string, num):
  answer = ''
  for i in range(0, num):
    answer += string

  return answer

# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


def string_bits(string):
  answer = [x for ind, x in enumerate(string) if ind%2==0]
  final_answer = ''
  for letter in answer:
    final_answer += letter
  return final_answer


#Given a non-empty string like "Code" return a string like "CCoCodCode"


def string_splostion(string):
  temp_string = ''
  answer = ''
  for letter in string:
    temp_string += letter
    answer += temp_string

  return answer

# given an array of integers


