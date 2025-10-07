import random

numbers=[]
even_odd={"even":[0,0],"odd":[0,0]} # dictionary that contains the sum and count of the odd and even numbers

# Function to identify that number is odd or even and sum and plus count the numbers
def even_odd_fun(num):
    if(num%2==0):
        even_odd["even"][0]=num+even_odd["even"][0]
        even_odd["even"][1] = even_odd["even"][1]+1
    else:
        even_odd["odd"][0] = num + even_odd["odd"][0]
        even_odd["odd"][1] = even_odd["odd"][1] + 1

for i in range(100):
    a = random.randint(0, 1000)
    if(len(numbers)==0):
        numbers.append(a)  # When the list is empty to insert the number
        continue
    if (a > numbers[i - 1]):
        numbers.append(a)   # When the number is largest put to the end of the list
    else:
        # This when the number is smaller and we have to iterate till 
        # we have find the number is greater than any number in the list and then insert it
        for j in range(i,0,-1):
            if(j==1 and a<=numbers[j-1]):
                numbers.insert(0,a)
                break
            if (a <= numbers[j - 1] and len(numbers)!=1):
                continue
            else:
                numbers.insert(j,a)
                break


print(numbers)
for i in numbers:
    even_odd_fun(i)
even_avg=even_odd["even"][0]/even_odd["even"][1]
odd_avg=even_odd["odd"][0]/even_odd["odd"][1]
print(even_avg)
print(odd_avg)
