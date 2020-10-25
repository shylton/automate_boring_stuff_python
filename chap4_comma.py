def add_comma(items):
    """
    Write a function that takes a list as an argument and returns a string
    with all the items separated by a comma and a space, with 'and' inserted 
    before the last item. Your function should be able to work with any list 
    value passed to it. Be sure to test the case where an empty list is passed 
    to your function.

    >>> add_comma(['apples', 'bananas', 'tofu', 'cats'])
    'apples, bananas, tofu and cats'
    >>> add_comma([])
    ''
    >>> add_comma('spam')
    's, p, a and m'
    >>> add_comma(['spam'])
    'spam'
    >>> add_comma([1, 2, 3, 4])
    '1, 2, 3 and 4'
    >>> add_comma(['spam', 'eggs'])
    'spam and eggs'
    """

    comma_str = ''
    for i in range(len(items)):
        if i == len(items) - 1:
            comma_str += str(items[i])
        elif i == len(items) - 2:
            comma_str += str(items[i]) + ' and '
        else:
            comma_str += str(items[i]) + ', '

    return comma_str

if __name__ == '__main__':
    from doctest import testmod
    testmod()
