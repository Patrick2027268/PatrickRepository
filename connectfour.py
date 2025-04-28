board = [[0],[0],[0],[0],[0],[0],[0],[0]]

for x in range(0,8):
    for y in range(0,8):
        board[x].append(0)
    print(board[x])

for game in range(0,49):
    column = int(input("Which column would you like to put in?"))
    for y in range(0,7):
        if board[column][y] == 0:
           board[column][y] = 1
           break
    print(board)
    column = int(input("Which column would you like to put in?"))
    for y in range(0,7):
        if board[column][y] == 0:
           board[column][y] = 2
           break
    print(board)
    
