import re

# detect dates format DD/MM/YYYY, where DD or MM has leading zero
date_re = re.compile(r"""^([0-2][1-9]|3[01])  # day 0-29 or 30, 31
                          /(0[1-9]|1[0-2])    # '/' then month 01 to 12
                          /([12]\d{3})$""",   # '/' then yr from 1000 to 2999
                    re.VERBOSE)


def date_re_test():
    """ run this function to test the date_re regex created.
        should return 'True' for every case.
    """
    match = ('03/12/1956', '01/01/1000', '31/12/2999')
    no_match = ('32/12/1956', '01/13/1956', '01/01/999', '01/01/3001'
                '2/12/1956', '01012000', '00/12/2000', '01/012000')

    print('Matches')
    for i, test in enumerate(match):
        print(str(i) + '.', date_re.match(test) is not None)

    print('\nNon Matches')
    for i, test in enumerate(no_match):
        print(str(i) + '.', date_re.match(test) is None)


def leap_year(year):
    """ Leap years are every year evenly divisible by 4, except for years
        which are both divisible by 100 and not divisible by 400.
        @param year: int
        @return: True if arg is a leap year, False otherwise

        >>> leap_year(2000)
        True
        >>> leap_year(2048)
        True
        >>> leap_year(1700)
        False
        >>> leap_year(400)
        True
        >>> leap_year(100)
        False
    """
    assert (type(year) == int), 'error: arg "year" must be an integer.'

    if year % 4 == 0 and not(year % 100 == 0 and year % 400 != 0):
        return True
    else:
        return False


def valid_date(date_string):
    """ uses regex to test if the argument is a valid date string,
        then ensures correct values are passes for day, month and year
        @param date_string: date in format 'DD/MM/YYYY'. use leading
            zero for single digit day and month. 1000 < YYYY < 2999
        @return: False if arg is not a valid date, True otherwise

        >>> valid_date('29/02/1800')  # not leap year
        False
        >>> valid_date('31/01/0999')  # bad year
        False
        >>> valid_date('29/02/2020')  # leap year
        True
        >>> valid_date('31/08/1984')
        True
        >>> valid_date('31/04/1999')
        False
    """
    re_test = date_re.match(date_string)
    if re_test is None:
        return False
    else:
        day, mo, yr = tuple(map(int, re_test.groups()))  # int variables

        # apr, jun, sept, nov have 30 days
        if mo in (4, 6, 9, 11) and day > 30:
            return False
        # feb has 29 days in leap years
        if mo == 2:
            if leap_year(yr):
                if day > 29:
                    return False
            elif day > 28:
                return False
        elif day > 31:
            return False
    # passed all tests
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
