# McNeill Chimuka
def main():
    player = next_player("")
    board = make_board()
    while not (win_board(board) or draw_board(board)):
        show_board(board)
        play(player,board)
        player = next_player(player)
    show_board(board)
    print("Good game,Thanks for playing")






def make_board():
    board =[]
    for num_square in range(9):
        board.append(num_square +1)
    return board

def show_board(board):
    print(f"{board[0]}| {board[1]}| {board[2]} ")
    print("+ - + - + ")
    print(f"{board[3]}| {board[4]}| {board[5]} ")
    print("+ - + - + ")
    print(f"{board[6]}| {board[7]}| {board[8]}")
    print()

def draw_board(board):
    for num_square in range(9):
        if board[num_square] != "o" and board[num_square] != "x":
            return False
    return True

def win_board(board):
    return(board[0]==board[1]==board[2] or
          board[3]==board[4]==board[5] or
          board[6]==board[7]==board[8] or
          board[0]==board[3]==board[6] or
          board[1]==board[4]==board[7] or
          board[2]==board[5]==board[8] or
          board[0]==board[4]==board[8] or
          board[2]==board[4]==board[6] 
          )

def play(player,board):
    num_square = int(input(f"{player}'s turn to choose a square(1-9): "))
    board[num_square - 1] = player

def next_player(current):
    if current == "" or current =="o":
        return "x"
    elif current =="" or current =="x":
        return "o"
if __name__  =="__main__":
    main()


    
 