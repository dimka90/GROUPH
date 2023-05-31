
import time
"""
This function print the sorted list in ascending or descending order 
Arg:
numbers:List of sorted number
value:The value for check if to sort in ascending or descending order
Return:
None
"""
def print_sorted_number(numbers,value):
    if value==1:
        sorted_number=sorted(numbers)
        print("sorting Numbers in Ascending order....")
        for x in sorted_number:
            print(x)
            time.sleep(1)
    else:
        sorted_number=sorted(numbers,reverse=True)
        print("sorting Numbers in Descending order....")
        for x in sorted_number:
            print(x)
            time.sleep(1)
"""
This function takes input from the user,
split it and convert it into an int or float 
Arg:
value:The value for check if to sort in ascending or descending order
Return:
None
"""

def split_num(value):
    
    user_input=input("Enter series of numbers to sort seperated by space \n>>>")

    split_input=user_input.split(" ")
    #an empty list that store 
    numbers=[]
    #looping throug the list
    for num in split_input:
        try:
            num=int(num)
        except ValueError:
            try:
                num=float(num)
            except ValueError:
                print("Invalid input")
                break
        numbers.append(num)
    print_sorted_number(numbers,value)
   
   