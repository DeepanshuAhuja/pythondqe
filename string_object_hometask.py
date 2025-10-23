'''
homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.

'''
str1 = "You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph."
str1='''tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''
import re

initial_list=str1.split(".") # Split the string with "." to have the sentences in the list

final_list=[]
tmp_str="" # Make the temporary string variable to make the list of each character of last word of the sentence
for i in initial_list:
    # print(i.split(" ")[-1]
    i=re.sub("iz","is",i,flags=re.IGNORECASE) # Correcting iz with is with ignoring case
    final_list.append(i.capitalize()) # Capitalize the string and append itto the final list
    tmp_str = tmp_str + " " + "".join(i.capitalize().split(" ")[-1]) # Taking out the last word of each sentence
final_list.append(tmp_str) # Making the final list
print(final_list)
