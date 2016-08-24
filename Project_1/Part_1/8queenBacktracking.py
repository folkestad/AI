def backtracking(chess_board):
    return "place holder"


#====== Creation of Board =====================================================

def print_board(chess_board):
    rownumber = 8
    print '  a b c d e f g h'
    for i in range(len(chess_board)-1, -1, -1):
        print rownumber,
        for j in chess_board[i]:
            print j,
        print rownumber
        rownumber -= 1
    print '  a b c d e f g h'

def user_interaction():
    print 'Place queens ( ex. "2 4 6 0 0 0 0 0")'
    user_input = raw_input().replace(' ', '')
    while len(user_input) != 8:
        print 'Place queens ( ex. "2 4 6 0 0 0 0 0")'
        user_input = raw_input().replace(' ', '')
    return user_input

def create_board(user_input):
    chess_board = []
    for i in range(8):
        chess_board.append(['.','.','.','.','.','.','.','.'])
    for i in range(len(user_input)):
        if user_input[i] != '0':
            chess_board[int(user_input[i])-1][i] = 'Q'
    return chess_board

#==============================================================================


chess_board = create_board(user_interaction())
print ""
print_board(chess_board)
