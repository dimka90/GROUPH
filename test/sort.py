
def sort_ascen(numbers):
    for sort_pass in range(0,len(numbers)):
        for x in range(0,len(numbers)-1):
            if numbers[x]>numbers[x+1]:
                temp=numbers[x]
                numbers[x]=numbers[x+1]
                numbers[x+1]=temp
    return numbers

def sort_desc(numbers):
    for sort_pass in range(0,len(numbers)):
        for x in range(0,len(numbers)-1):
            if numbers[x]<numbers[x+1]:
                temp=numbers[x]
                numbers[x]=numbers[x+1]
                numbers[x+1]=temp
    return numbers