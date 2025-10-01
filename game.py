import pygame
import random

""" Morpion game """

""" window """
window_width = 400
window_height: 600
cell_size=window_width//3
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Morpion")

""" plateau """
plateau=[["" for _ in range(3)] for _ in range(3)]

""" game settings """
""" colors """
background_color = (40, 40, 40)
cell_color = (0, 0, 0)
line_color = (70, 70, 70)
AI_color = (255, 0, 0)
player_color = (0, 255, 0)
empty_color = (0, 0, 0)

""" players symbols """
AI_symbol="O"
player_symbol="X"

""" game variables """
turn="player"
party_over=False
winner=None
pygame.init()

""" Game functions """

def draw_plateau():
    window.fill(background_color)

    """ drawing vertical lines """
    for x in range(window_width//cell_size):
        """ pygame.draw.line(window, line_color, start_pos(x, y), end_pos(x, y), width) """
        pygame.draw.line(window, line_color, (cell_size * x, 0), (cell_size * x, window_height), 2)
    pass

    """ drawing horizontal lines """
    for y in range(window_height//cell_size):
        """ pygame.draw.line(window, line_color, Y start_pos(x,y), Y end_pos(x, y), width) """
        pygame.draw.line(window, line_color, (0, cell_size * y), (window_width, cell_size*y))

def draw_symbols():
    for x in range(3):
        for y in range(3):
            symbol = plateau[x][y]
            if symbol == player_symbol:
                color = player_color
            elif symbol == AI_symbol:
                color = AI_color
            else :
                color= empty_color
            if symbol != "":
                pygame.draw.circle(
                    window, color, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), cell_size // 2 - 10, 2)

def is_plateau_rempli():
    for line in plateau:
        if "" in line: 
            return False
    return True

def is_winner(symbol):
    for line in plateau:
        if all(cellule == symbol for cellule in line):
            return True
    for column in range(3):
      if all(plateau[row][column] == symbol for row in range(3)):
          return True
    if all(plateau[i][i] == symbol for i in range(3)):
        return True
    if all(plateau[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def play(x,y, symbol):
    if plateau[x][y] == "":
        plateau[x][y] = symbol
        return True
    return False

def player_plays():
    global turn
    pos_mouse = pygame.mouse.get_pos()
    cell_x = pos_mouse[0]
    cell_y = pos_mouse[1]

    if(play(cell_x, cell_y) == True, player_symbol):
        turn = "AI"
        

def AI_plays():
    global turn
    empty_cell = []
    for x in range(3):
        for y in range(3):
            if plateau[x][y] == "":
              empty_cell.append((x, y))
    
    if empty_cell:
        x, y = random.choice(empty_cell)
        play(x, y, AI_symbol)
    
    turn = "player"

def check_end_game():
    global party_over, winner
    if is_winner(player_symbol):
        party_over = True
        return "player"
    elif is_winner(AI_symbol):
        party_over = True
        return "AI"
    elif is_plateau_rempli() == True:
        party_over = True
        return "no winner"
    return None

def is_party_over():
    pass

def party_again():
    pass


# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            """ si le joueur appuie sur le reset button en cours de partie """
            """ if reset_button_rect.collidepoint(événement.pos):
                réinitialiser_partie() """
        elif not party_over and turn == "player":
                player_plays()

    if not party_over and turn == "AI":
        AI_plays()
        winner = is_party_over()

    draw_plateau()
    draw_symbols()

    if party_over:
        draw_winner()
        draw_button_reset()

    pygame.display.flip()         

pygame.quit()



best_moves = []
for x in range(window_width//cell_size):
    for y in range(window_height//cell_size):
        if plateau[x][y]== player_symbol and plateau[x][y+1]==player_symbol and plateau[x][y+2]== "":
            best_moves.append((x, y +2))
        
        if plateau[x][y] == player_symbol and plateau[x + 1][y] == player_symbol and plateau[x + 2][y] == "":
            best_moves.append(x+2, y)
