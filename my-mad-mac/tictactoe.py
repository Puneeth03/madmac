import pygame as pg,sys
from pygame.locals import *
import time

#Initializing the global variables
turn = 'x'
winner = None
draw = False
width = 400
height = 400

#To initialize a 3*3 board table for tic-tac-toe
table = [[None]*3,[None]*3,[None]*3]

#Initializing pg window
pg.init()
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100))
pg.display.set_caption("Tic Tac Toe")

#Loading the images
x_img = pg.image.load('X.png')
o_img = pg.image.load('O.png')

#Scaling images to produce different size of X and O appear different 
x_img = pg.transform.scale(x_img, (120,120))
o_img = pg.transform.scale(o_img, (60,60))

#Displaying window of opening with the tic-tac-toe board
def open_window():
    pg.display.update()
    #Filling of screen with a color
    screen.fill((255, 200, 255))
    
    # Drawing vertical and horizontal lines on the color filled board(here multiple proportions of cells are used just to make it appear a little different)
    pg.draw.line(screen,(10,10,10),(width/3.65,0),(width/3.65, height),7)
    pg.draw.line(screen,(10,10,10),(width/3*1.85,0),(width/3*1.85, height),7)
    pg.draw.line(screen,(10,10,10),(0,height/3.65),(width, height/3.65),7)
    pg.draw.line(screen,(10,10,10),(0,height/3*1.85),(width, height/3*1.85),7)

    #Loading or displaying the board with lines drawn on the screen making it look like 3*3 table
    display_status()
    

def display_status():
    global draw

    #Its the status of the game if there is no winner it is someone's turn or a draw
    if winner is None:
        result = turn.upper() + "'s Turn"
    else:
        result = winner.upper() + " won!"
    if draw:
        result = 'Game Draw!'

    font = pg.font.Font(None, 30)
    text = font.render(result, 1, (255, 255, 255))

    #Displaying the status/result on the screen
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 450))
    screen.blit(text, text_rect)
    pg.display.update()

#Draw a line showing the win of player
def win_status():
    global table, winner,draw

    #Checking wether the winner is in a row
    for row in range (0,3):
        if ((table [row][0] == table[row][1] == table[row][2]) and(table [row][0] is not None)):
            winner = table[row][0]
            if(row == 1):
                row = row*0.85
            elif(row == 2):
                row = row*0.95
            pg.draw.line(screen, (250,0,0), (0, (row + 1)*height/3 -height/6),(width, (row + 1)*height/3 - height/6 ), 4)
            break

    #Checking wether the winner is in a column
    for col in range (0, 3):
        if (table[0][col] == table[1][col] == table[2][col]) and (table[0][col] is not None):
            winner = table[0][col]
            if(col == 1):
                col = col*0.85
            elif(col == 2):
                col = col*0.95
            pg.draw.line (screen, (250,0,0),((col + 1)* width/3 - width/6, 0),((col + 1)* width/3 - width/6, height), 4)
            break

    #Checking wether the winner is in a diagonal
    if (table[0][0] == table[1][1] == table[2][2]) and (table[0][0] is not None):
        winner = table[0][0]
        pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)
    
    if (table[0][2] == table[1][1] == table[2][0]) and (table[0][2] is not None):
        winner = table[0][2]
        pg.draw.line (screen, (250,70,70), (315, 40), (40, 315), 4)
    
    #It shows if all the cells are filles and there is no winner then it is a draw
    if(all([all(row) for row in table]) and winner is None ):
        draw = True

    #Using the variables declared above(as global), displaying the status of the game
    display_status()

#Displaying 'X' or 'O' when a player selects an unselected cell and their respective turn
def drawturn(row,col):
    global table,turn

    #Marking the respective cell with the turn from the points collected
    if row==1:
        x = 20
    if row==2:
        x = width/3.65 + 20
    if row==3:
        x = width/3*1.85 + 20

    if col==1:
        y = 20
    if col==2:
        y = height/3.65 + 20
    if col==3:
        y = height/3*1.85 + 20

    table[row-1][col-1] = turn

    if(turn == 'x'):
        screen.blit(x_img,(y,x))
        turn= 'o'
    else:
        screen.blit(o_img,(y,x))
        turn= 'x'
    pg.display.update()
   
    
def userClick():
    #Getting the co-ordinataes of the point
    x,y = pg.mouse.get_pos()

    #From the co-ordinates of the points find the cell i.e, row and column where the cell has to be marked for respective turn
    if(x<width/3.65):
        col = 1
    elif (x<width/3*1.85):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None
        
    if(y<height/3.65):
        row = 1
    elif (y<height/3*1.85):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
    
    #Considering only the unmarked cells and marking if it is unmarked
    if(row and col and table[row-1][col-1] is None):
        global turn
        drawturn(row,col)

        #Checking and updating the status after every turn
        win_status()
        
#Reloading the game after a win or a draw
def new_game():
    pg.display.update()
    global table, winner,turn, draw
    turn = 'x'

    #removing and updating the status 
    draw = False
    winner=None
    open_window()
    table = [[None]*3,[None]*3,[None]*3]
    
#Asking user if he wants to play another game
def new_game_window():
    global flag
    flag = False
    pg.display.update()

    #Creating new interface to display the 'New Game' button
    screen.fill((200, 200, 255))
    text = ' New Game'
    font = pg.font.SysFont("Roboto", 50)
    text_render = font.render(text, 1, (255, 255, 255))
    x, y = (100,225)
    pg.draw.line(screen, (150, 150, 150), (x, y), (x + 200 , y), 5)
    pg.draw.line(screen, (50, 50, 50), (x, y + 50), (x + 200 , y + 50), 5)
    pg.draw.rect(screen, (100, 100, 100), (x, y, 200 , 50))
    screen.blit(text_render, (x, y))
    mouse = pg.mouse.get_pos()

    #Getting the co-ordinates of click and if it is on button new game is created, else nothing
    if event.type == MOUSEBUTTONDOWN:
        if 100 <= mouse[0] <= 300 and 225 <= mouse[1] <= 275:
            flag = True
            new_game()

#Variable to get not confused with the drawturn
flag2 = True

#Opening of game
open_window()

#Running the loop entirely to play
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            #Marking the cell with the player turn
            if(flag2 == True or flag == True):
                userClick()
            if(winner or draw):
                flag2 = False
                time.sleep(2)
                new_game_window()
            
    pg.display.update()
