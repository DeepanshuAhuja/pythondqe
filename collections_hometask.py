'''
1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
Each line of code should be commented with description.

'''

import random
import string

number_of_dicts = random.randint(2, 10)  # To choose the random number for the length of the list
dicts_list = []
for i in range(0, number_of_dicts):
    temp_dict = {}
    for i in range(3):
        # To put the random values in the dictionaries
        temp_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
    dicts_list.append(temp_dict)
final_dict = {}
for i in range(len(dicts_list)):
    for key, value in dicts_list[i].items():
        max = dicts_list[i][key]
        number = i + 1
        flag = True
        for j in range(i + 1, len(dicts_list)):
            if (key in dicts_list[j]):
                flag = False
                if (max >= dicts_list[j][key]):
                    pass
                else:
                    max = dicts_list[j][key] # To find out the maximum value
                    number = j + 1
                dicts_list[j].pop(key) # To delete value from the dictionary , condition will not check the already check values
        if (number == i + 1 and flag == True): # Condition when key is not found in any of the dictionaries
            final_dict[key] = max
        else:
            final_dict[key + '_' + str(number)] = max
print(final_dict)
