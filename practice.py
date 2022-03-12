
def swap(mylist):
    mylist[0], mylist[-1] = mylist[-1], mylist[0]
    return mylist

mylist = input('input list: ').replace(" ", "").split(',')

print('hello')

def list_reverse(mylist):
    print(mylist[::-1])

print('hi')

print(swap(mylist))
list_reverse(mylist)