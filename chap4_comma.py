"""
Write a function that takes a list value as an argument and returns a string
with all the items separated by a comma and a space, with and inserted before
the last item. For example, passing the previous spam list to the function
would return 'apples, bananas, tofu, and cats'. But your function should be
able to work with any list value passed to it. Be sure to test the case
where an empty list [] is passed to your function.
ex: spam = ['apples', 'bananas', 'tofu', 'cats']
    return 'apples, bananas, tofu, and cats'
"""
import copy


def add_comma(strings):
    # handle exceptions
    if 0 == len(strings):
        return ''
    elif 1 == len(strings):
        return strings[0]
    elif type(strings) != list:
        return "invalid type."

    rtn = []
    for item in strings:
        rtn.append(str(item))  ## convert to string and append to list

    rtn[-1] = 'and ' + str(rtn[-1])  # modify last element
    
    return ', '.join(rtn)  # create new string then return it


# test cases.
spam = ['apples', 'bananas', 'tofu', 'cats']
print('1.',add_comma(spam))
print('2.',add_comma([]))
print('3.',add_comma(['spam']))
print('4.',add_comma('spam',))
print('5.',add_comma([1,2.5,'eggs',-5,0, spam]))
