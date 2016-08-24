def backTracking(chess_board):

    return "place holder"


print 'Place queens ( ex. "24600000")'
user_input = input()
while len(user_input) != 8:
    print 'Place queens ( ex. "24600000")'
    user_input = input()

chess_board = []
for i in range(8):
    chess_board.append(['.','.','.','.','.','.','.','.'])
solution = backTracking(user_input)
print solution
