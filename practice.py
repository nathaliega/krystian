
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

mylist = [1, 2, 3, 4, 5, 6]
def swap(mylist):
    mylist[0], mylist[-1] = mylist[-1], mylist[0]
    return mylist

