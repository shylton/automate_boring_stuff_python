import re


def strong_psw(psw, verbose=False):
    """ uses regex to determine if passed string is a strong password.
        Eight or more characters. Both upper and lowecase. One or more digits.
        @param psw: string to be checked
        @param verbose: boolean: True returns string on error
        @return boolean: True if psw is strong, False or error string otherwise

        >>> strong_psw('bob')
        False
        >>> strong_psw(1234)  # not string
        Traceback (most recent call last):
        ...
        ValueError: arg must be a string
        >>> strong_psw('AuntMary12345')
        True
        >>> strong_psw('nouppercasecharshere')
        False
        >>> print(strong_psw('1234567890', True))
        must have upper case letter

    """
    if type(psw) != str:
        raise ValueError('arg must be a string')

    # REFACTOR: these can be combined with lookahead, but cleaner this way
    psw_check1 = re.compile('.{8,}')    # 8 or more anything in length
    psw_check2 = re.compile('[A-Z]+')   # one or more upper case
    psw_check3 = re.compile('[a-z]+')   # one or more lower case
    psw_check4 = re.compile(r'\d+')     # one or more digits

    if verbose:
        if psw_check1.search(psw) is None:
            return 'password must be longer than 8'
        if psw_check2.search(psw) is None:
            return 'must have upper case letter'
        if psw_check3.search(psw) is None:
            return 'must have lower case letter'
        if psw_check4.search(psw) is None:
            return 'must have at least one digit'
        return True
    else:
        test = bool(psw_check1.search(psw)) and bool(psw_check2.search(psw)) \
            and bool(psw_check3.search(psw)) and bool(psw_check4.search(psw))
        return test


if __name__ == '__main__':
    import doctest
    doctest.testmod()
