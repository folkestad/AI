def backtracking(chess_board):
    return "place holder"


#====== Creation of Board ======

def print_board(chess_board):
    rownumber = 1
    for i in chess_board:
        print rownumber,
        for j in i:
            print j,
        print ""
        rownumber += 1

def user_interaction():
    print 'Place queens ( ex. "24600000")'
    user_input = raw_input()
    while len(user_input) != 8:
        print 'Place queens ( ex. "24600000")'
        user_input = raw_input()
    return user_input

def create_board(user_input):
    chess_board = []
    for i in range(8):
        chess_board.append(['.','.','.','.','.','.','.','.'])
    for i in range(len(user_input)):
        if user_input[i] != '0':
            chess_board[i][int(user_input[i])-1] = 'Q'
    return chess_board

#===============================


chess_board = create_board(user_interaction())
print_board(chess_board)
