from pprint import pprint
import re  # re might be overkill, doing it for practice

def isValidChessBoard(board_dict):
    """ Function will return verbose string instead of True False.
        ONLY checking the conditions specified in the problem:
            1. one wking and one bking
            2. each player has 16 piece max
            3. max 8 pawns
            4. keys 1a to 8h
            5. piece names begin with 'w' or 'b' followed by
                'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'

        >>> isValidChessBoard({'1h': 'bking','6c': 'wqueen', '2g':'bbishop', \
                    '5h': 'bqueen', '3e': 'wking'})
        True
        >>> isValidChessBoard({'6c': 'wqueen', '2g':'bbishop', \
            '5h': 'bqueen', '3e': 'wking'})
        'invalid king count'
        >>> isValidChessBoard({'9c': 'bking','6c': 'wqueen', '2g':'bbishop', \
                    '5h': 'bqueen', '3e': 'wking'})
        '9c is not a valid coordinate'
        >>> isValidChessBoard({'6c': 'queen', '1h': 'bking', '2g':'bbishop', \
                    '5h': 'bqueen', '3e': 'wking'})
        'queen is not valid'
        >>> isValidChessBoard({'6c': 'bcar', '1h': 'bking', '2g':'bbishop', \
                    '5h': 'bqueen', '3e': 'wking'})
        'bcar is not valid'
    """

    # 1. check for one white king and one black king
    pieces = tuple( board_dict.values() )
    if pieces.count('bking') != 1 or pieces.count('wking') != 1:
        return 'invalid king count'

    # Check pieces
    valid_piece = re.compile('[wb](pawn|knight|bishop|rook|queen|king)$')
    whites = blacks = pawns_w = pawns_b = 0

    for piece in pieces:
        if valid_piece.match(piece) == None:
            return f'{piece} is not valid'  # 5 failure
        if 'w' == piece[0]:
            whites += 1
        if 'b' == piece[0]:
            blacks += 1
        if 'wpawn' == piece:
            pawns_w += 1
        if 'bpawn' == piece:
            pawns_b += 1

    # 2 check piece count
    if whites > 16:
        return 'Too many white pieces'
    if blacks > 16:
        return 'Too many black pieces'

    # 3 check pawns count
    if pawns_w > 8:
        return 'Too many white pawns'
    if pawns_b > 8:
        return 'Too many black pawns'

    # 4. chech if each key represents a valid coordinate
    coordinates = tuple(board_dict.keys())
    valid_keys = set()  # keys = board spaces labeled 1-8 and a-h
    
    for row in range(1,9):
        for col in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            valid_keys.add(str(row) + col)

    for coord in coordinates:
        if coord not in valid_keys:
            return f'{coord} is not a valid coordinate'

    return True  # nothing failed


if __name__ == "__main__":
    import doctest
    doctest.testmod()
