
# coding: utf-8

# In[ ]:


from IPython.display import clear_output

#function to display board:
def display_board(board):
    
    clear_output()
    print('   |   | ')
    
    print('   |   | ')
    
    print('',board[1],'|',board[2],'|',board[3])
    print('___|___|___')
    
    print('   |   | ')
    
    print('   |   | ')
    
    print('',board[4],'|',board[5],'|',board[6])
    
    print('___|___|___')
    
    print('   |   | ')
    
    print('',board[7],'|',board[8],'|',board[9])
    
    print('   |   | ')
    
    print('   |   | ')

    
     
    #ACCEPTING INPUT FROM USER:
def player_input():
    symbol = ''
    
    while not (symbol == 'X' or symbol == 'O'):
        symbol = input('Player 1: Do you want to be X or O? \n').upper()

    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')    
    
    
    
    
    #place marker accrding to user wish
def place_marker(board,symbol,position):
    board[position]=symbol
        
    
    #check board to check winner
def check_board(board,symbol):
    return( (board[1] == symbol and board[5] == symbol and board[9]==symbol) or ##diagonal
           (board[3] == symbol and board[5] == symbol and board[7] == symbol) or
           (board[1] == symbol and board[2] == symbol and board[3] == symbol) or #straight rows
           (board[4] == symbol and board[5] == symbol and board[6] == symbol) or
           (board[7] == symbol and board[8] == symbol and board[9] == symbol) or #striaght columns
           (board[1] == symbol and board[4] == symbol and board[7] == symbol) or
           (board[2] == symbol and board[5] == symbol and board[8] == symbol) or
           (board[3] == symbol and board[6] == symbol and board[9] == symbol)
          
          
          )


        #selecting player
from random import randint
def select_player():
    s=randint(0,1)
    if(s==0):
        return ('player1')
    else:
        return ('player2')
    
    
    #check availability of space:
def check_space(board,position):
    if board[position]==' ':
        return True
    else: 
        return False
    
    
    
    #check if board is full or not:
def full_board_check():
    for x in range(1,10):
        if check_space(board,x):
            return False
    return True
        
        
        
    
    #ask player's next position:
def player_choice(board):
    
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not check_space(board,position):
        position=int(input('what is your next position(1-9)?'))
    
    return position
    
    
    
    #ask player if they want to play again:
def replay():
    return (input('Do you want to play again? Enter Y or N: ').lower()=='y')





    #now all the function are over:

#lets begin to write the program and implement all the function that we wrote above:

print('WELCOME TO TIC-TAC-TOE GAME')

while True:
    #reset the board
    board=[' ']*10
    player1_symbol,player2_symbol=player_input()
    turn=select_player()
    print(turn+' goes first')
    
    play_game=input('Game is on!! Are You Ready? Y or N? ').lower()
    
    if(play_game=='y'):
        game_on=True
    else:
        game_on=False
        
        
        
    while game_on:
        
        if turn=='player1':   #Player1 turn
            display_board(board)
            position=player_choice(board)
            place_marker(board,player1_symbol,position)
            
            if(check_board(board,player1_symbol)):
                display_board(board)
                print("Congo!! Player1 WINS THE GAME ")
                game_on=False
            else:
                if(full_board_check()):
                    display_board(board)
                    print('The Game is a draw!!!!')
                    break
                else:
                    turn='player2'
        else:       #Player2 turn
            
            display_board(board)
            position=player_choice(board)
            place_marker(board,player2_symbol,position)
             
            if(check_board(board,player2_symbol)):
                display_board(board)
                print("Congo!! Player2 WINS THE GAME ")
                game_on=False
            else:
                if(full_board_check()):
                    display_board(board)
                    print('The Game is a draw!!!!')
                    break
                else:
                    turn='player1'
            
    if not replay():
        break
        
    
    

