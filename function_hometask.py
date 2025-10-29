import random
import string
import re

from collections_hometask import final_dict


def collection_hometask(a,b):
    dicts_list=make_dictionary(a,b)
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
            final_dict=assign_value_dictionary(number,i,flag, key, max)
    return final_dict

def make_dictionary(a,b):
    number_of_dicts = random.randint(a, b)  # To choose the random number for the length of the list
    dicts_list = []
    for i in range(0, number_of_dicts):
        temp_dict = {}
        for i in range(3):
            # To put the random values in the dictionaries
            temp_dict[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        dicts_list.append(temp_dict)
    return dicts_list
def assign_value_dictionary(number,i,flag,key,max):
    if (number == i + 1 and flag == True):  # Condition when key is not found in any of the dictionaries
        final_dict[key] = max
    else:
        final_dict[key + '_' + str(number)] = max
    return final_dict
collection_hometask(2,10)
def last_word_sentence(word):
    return word.capitalize().split(" ")[-1]
def string_hometask(str1):
    initial_list = str1.split(".")  # Split the string with "." to have the sentences in the list
    final_list = []
    tmp_str = ""  # Make the temporary string variable to make the list of each character of last word of the sentence
    for i in initial_list:
        i = re.sub("iz", "is", i, flags=re.IGNORECASE)  # Correcting iz with is with ignoring case
        final_list.append(i.capitalize())  # Capitalize the string and append itto the final list
        tmp_str = tmp_str + " " + "".join(last_word_sentence(i))  # Taking out the last word of each sentence
    final_list.append(tmp_str)  # Making the final list

    return final_list
str1='''tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''
final_list=string_hometask(str1)
print(final_list)
