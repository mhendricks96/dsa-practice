start_list = sample = ['3',5,2,'8',9,1,'12',45,6,97]


# every third item in a list
[x for ind, x in enumerate(start_list) if ind%3 == 0]

# every odd number in the list
[x for x in start_list if x%2]

# every item in the list that is a string
[x for x in start_list if type(x) is str]

# every item in the list with a value over 11
# even checks strings
[x for x in start_list if int(x) > 11]
