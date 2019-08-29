

def arrange_list(mylist):
    if isinstance(mylist, list):
        newString = ''
        for element in mylist:
            try:
                index = mylist.index(element)
                if index == len(mylist) -1:
                    element = 'and ' + str(element)
                else:
                    element = str(element) + ', '
                newString += element
            except:
                continue
        return newString

spam = ['apples', 'bananas', 'tofu', 'cats']
newString = arrange_list(spam)
print(newString)