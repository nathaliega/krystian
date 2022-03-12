

mystring = input('Input a string: ')

def palimetry(mystring):
    if len(mystring) % 2 == 0:
        print('String is symmetric')
    else:
        print('String is not symmetric')

    if mystring == mystring[::-1]:
        print('String is palindrome')
    else:
        print("Strinf is no palindorme")

palimetry(mystring)