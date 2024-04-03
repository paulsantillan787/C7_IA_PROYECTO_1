import pygame

from game_piece import GamePiece

# Initialize Pygame
pygame.init()

turno = 1
number = 1
fase = 1
blancos = []
rojos = []
currentPiece = None

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
GREEN = (0, 255, 0)
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

connections = {
    (50, 50): [(350, 50), (50, 350)],
    (350, 50): [(50, 50), (650, 50), (350, 150)],
    (650, 50): [(350, 50), (650, 350)],
    (150,150): [(350,150), (150, 350)],
    (350, 150): [(150, 150), (550, 150), (350, 250), (350, 50)],
    (550, 150): [(350, 150), (550, 350)],
    (250, 250): [(350, 250), (250, 350)],
    (350, 250): [(250, 250), (450, 250), (350, 150)],
    (450, 250): [(350, 250), (450, 350)],
    (50, 350): [(50, 50), (150, 350), (50, 650)],
    (150, 350): [(50, 350), (150, 150), (250, 350), (150, 550)],
    (250, 350): [(150, 350), (250, 250), (250, 450)],
    (450, 350): [(350, 350), (450, 250), (550, 350), (450, 450)],
    (550, 350): [(450, 350), (550, 150), (650, 350), (550, 550)],
    (650, 350): [(550, 350), (650, 50), (650, 650)],
    (250, 450): [(250, 350), (350, 450)],
    (350, 450): [(250, 450), (450, 450), (350, 550)],
    (450, 450): [(350, 450), (450, 350)],
    (150, 550): [(150, 350), (350, 550)],
    (350, 550): [(150, 550), (350, 450), (550, 550)],
    (550, 550): [(350, 550), (550, 450)],
    (50, 650): [(50, 350), (350, 650)],
    (350, 650): [(50, 650), (650, 650), (350, 550)],
    (650, 650): [(350, 650), (650, 350)]
}

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
    
  if currentPiece is not None:
    for connection in connections[currentPiece.position]:
      if ocupado[positions.index(connection)] == 0:
        pygame.draw.circle(window, GREEN, connection, 10)

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
        pos = hallar_posicion(event.pos)
        if pos is not None:
          # if currentPiece is None or currentPiece.color == pieces[turno]:
          if ocupado[positions.index(pos)] == 1:
            if turno == 1:
              for piece in blancos:
                if piece.position == pos:
                  currentPiece = piece
                  print(currentPiece.number)                    
                  break
            elif turno == 2:
              for piece in rojos:
                if piece.position == pos:
                  currentPiece = piece
                  print(currentPiece.number)
                  break
          elif currentPiece is not None:
            if currentPiece.move(pos, ocupado, positions, connections):
              if turno == 1:
                turno = 2
              elif turno == 2:
                turno = 1
              currentPiece = None

# Quit Pygame
pygame.quit()