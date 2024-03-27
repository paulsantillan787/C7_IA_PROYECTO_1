import pygame

from game_piece import GamePiece

# Initialize Pygame
pygame.init()

turno = 1
number = 1
fase = 1
blancos = []
rojos = []

# Set the dimensions of the game window
WIDTH = 700
HEIGHT = 700
WINDOW_SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Nine Men's Morris")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)

# Define the board positions
positions = [
  (50, 50), (350, 50), (650, 50),
  (150, 150), (350, 150), (550, 150),
  (250, 250), (350, 250), (450, 250),
  (50, 350), (150, 350), (250, 350), (450, 350), (550, 350), (650, 350),
  (250, 450), (350, 450), (450, 450),
  (150, 550), (350, 550), (550, 550),
  (50, 650), (350, 650), (650, 650)
]

ocupado = [
  0,0,0,
  0,0,0,
  0,0,0,0,0,0,
  0,0,0,
  0,0,0,
  0,0,0,
  0,0,0
]

# Funciones auxiliares
def hallar_posicion(pos):
  for position in positions:
    x, y = position
    if x - 20 <= pos[0] <= x + 20 and y - 20 <= pos[1] <= y + 20:
      return position

  return None



# Game loop
running = True
while running:
  
  # Clear the screen
  window.fill(BROWN)

    # Draw the board
  pygame.draw.rect(window, BLACK, (50, 50, 600, 600), 5)
  pygame.draw.rect(window, BLACK, (150, 150, 400, 400), 5)
  pygame.draw.rect(window, BLACK, (250, 250, 200, 200), 5)
    
  pygame.draw.line(window, BLACK, (350, 50), (350, 250), 5)
  pygame.draw.line(window, BLACK, (350, 450), (350, 650), 5)
  pygame.draw.line(window, BLACK, (50, 350), (250, 350), 5)
  pygame.draw.line(window, BLACK, (450, 350), (650, 350), 5)

  # Draw the positions
  for position in positions:
    pygame.draw.circle(window, BLUE, position, 20)
    
  for piece in blancos:
    piece.draw(window, pygame)
    
  for piece in rojos:
    piece.draw(window, pygame)

  # Update the display
  pygame.display.update()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if fase == 1:
        pos = hallar_posicion(event.pos)
        if pos is not None and ocupado[positions.index(pos)] == 0:
          if turno == 1:
            piece = GamePiece(WHITE, pos, number)
            blancos.append(piece)
            ocupado[positions.index(pos)] = 1
            turno = 2
          elif turno == 2:
            piece = GamePiece(RED, pos, number)
            rojos.append(piece)
            ocupado[positions.index(pos)] = 1
            turno = 1
            number += 1
            if number == 4:
              number = 1
        if len(rojos) == 9 and len(blancos) == 9:
          fase = 2
      elif fase == 2:
        print("Fase 2")

# Quit Pygame
pygame.quit()