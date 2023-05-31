import GROUPH
import time

print(
        '''
        *****Sorting program*******
        Select one of the operation
        1)Sort Numbers in Ascending order
        2)Sort Numbers in Descending Order
        3)Quit
        ***************************
        '''
)
user_input=int(input("Enter either 1, 2 or 3\n>>>"))
if user_input == 1:
    GROUPH.split_num(user_input)
if user_input==2:
    GROUPH.split_num(user_input)
if user_input <0 or user_input > 3:
    print("Out of Range, please number sholud be between 1 and 3..")
if user_input ==3:
        exit()