
def swap(mylist):
    mylist[0], mylist[-1] = mylist[-1], mylist[0]
    return mylist

mylist = input('input list: ').replace(" ", "").split(',')


print(swap(mylist))