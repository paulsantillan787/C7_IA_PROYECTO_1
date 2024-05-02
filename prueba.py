import pygame

# Initialize Pygame
pygame.init()

T = [
  ['v',None,None, 'v' ,None,None,'v'],
  [None,'v',None, 'v' ,None,'v',None],
  [None,None,'v', 'v' ,'v',None,None],
  ['v', 'v', 'v', None,'v', 'v', 'v'],
  [None,None,'v', 'v' ,'v',None,None],
  [None,'v',None, 'v' ,None,'v',None],
  ['v',None,None, 'v' ,None,None,'v']
]

P = [
  [(50, 50) , None      , None      , (350, 50) , None      , None      , (650, 50) ],
  [None     , (150, 150), None      , (350, 150), None      , (550, 150), None      ],
  [None     , None      , (250, 250), (350, 250), (450, 250), None      , None      ],
  [(50, 350), (150, 350), (250, 350), None      , (450, 350), (550, 350), (650, 350)],
  [None     , None      , (250, 450), (350, 450), (450, 450), None      , None      ],
  [None     , (150, 550), None      , (350, 550), None      , (550, 550), None      ],
  [(50, 650), None      , None      , (350, 650), None      , None      , (650, 650)]
]

G = {
    (0, 0): [(0, 3), (3, 0)],
    (0, 3): [(0, 0), (0, 6), (1, 3)],
    (0, 6): [(0, 3), (3, 6)],
    (1, 1): [(1, 3), (3, 1)],
    (1, 3): [(1, 1), (1, 5), (2, 3), (0, 3)],
    (1, 5): [(1, 3), (3, 5)],
    (2, 2): [(2, 3), (3, 2)],
    (2, 3): [(2, 2), (2, 4), (1, 3)],
    (2, 4): [(2, 3), (3, 4)],
    (3, 0): [(0, 0), (3, 1), (6, 0)],
    (3, 1): [(5, 1), (1, 1), (3, 2), (3, 0)],
    (3, 2): [(3, 1), (2, 2), (4, 2)],
    (3, 4): [(2, 4), (3, 5), (4, 4)],
    (3, 5): [(3, 4), (1, 5), (3, 6), (5, 5)],
    (3, 6): [(3, 5), (0, 6), (6, 6)],
    (4, 2): [(3, 2), (4, 3)],
    (4, 3): [(4, 2), (4, 4), (5, 3)],
    (4, 4): [(4, 3), (3, 4)],
    (5, 1): [(3, 1), (5, 3)],
    (5, 3): [(5, 1), (4, 3), (5, 5), (6, 3)],
    (5, 5): [(5, 3), (3, 5)],
    (6, 0): [(3, 0), (6, 3)],
    (6, 3): [(6, 0), (6, 6), (5, 3)],
    (6, 6): [(6, 3), (3, 6)]
}

t = 'B'
F = 1
FGB = 9
FGN = 9
f1n = 0
f2n = 0
f3n = 0
f1b = 0
f2b = 0
f3b = 0
fbm = True
fnm = True
mol = False
mact = []
lmn = []
lmb = []

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

# Funciones auxiliares
def hallar_posicion(pos):
  for i, filas in enumerate(P):
    for j, elemento in enumerate(filas):
      if elemento is not None:
        x = elemento[0]
        y = elemento[1]
        if x - 25 <= pos[0] <= x + 25 and y - 25 <= pos[1] <= y + 25:
          return (i, j)

  return None

def dibujarPosition(coord, color, number):
  pygame.draw.circle(window, color, coord, 30)
  font = pygame.font.Font(None, 36)
  if(color == BLACK):
    text_surface = font.render(str(number), True, WHITE)
  else:
    text_surface = font.render(str(number), True, BLACK)
  
  text_x = coord[0] - text_surface.get_width() / 2
  text_y = coord[1] - text_surface.get_height() / 2
  text_position = (text_x, text_y)
  window.blit(text_surface, text_position)
  
  
def buscarMolino(listaMolino, mact):
  return mact in listaMolino

def verificarMolinoNegro(a, b):
  global mol, T, t, lmn
  if t == 'N':
    if T[a][b] in ['N1', 'N2', 'N3'] and (T[a][b] == 'N1' and f1n > 0) or (T[a][b] == 'N3' and f3n > 0) or (T[a][b] == 'N2' and f2n > 0):
      if P[a][b][0] - P[a][b][1] == 0 or P[a][b][0] + P[a][b][1] == 700:
        if T[a][b] == 'N1':
          for conn1 in G[(a, b)]:
            x1, y1 = conn1
            if T[x1][y1] == 'N2':
              for conn2 in G[(x1, y1)]:
                x2, y2 = conn2
                if (x2 == a or y2 == b) and T[x2][y2] == 'N3':
                  mact = [(a, b), (x1, y1), (x2, y2)]
                  if not buscarMolino(lmn, mact):
                    print(mact)
                    lmn.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
        elif T[a][b] == 'N3':
          for conn1 in G[(a, b)]:
            x1, y1 = conn1
            if T[x1][y1] == 'N2':
              for conn2 in G[(x1, y1)]:
                x2, y2 = conn2
                if (x2 == a or y2 == b) and T[x2][y2] == 'N1':
                  mact = [T[a][b][0], conn1, conn2]
                  if not buscarMolino(lmb, mact):
                    print(mact)
                    lmn.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
      else:
        if T[a][b] == 'N1' and (P[a][b][0] - P[a][b][1] == 300 or P[a][b][0] - P[a][b][1] == -300 or P[a][b][0] - P[a][b][1] == 100 or P[a][b][0] - P[a][b][1] == -100):
          for conn1 in G[(a, b)]:
            x1, y1 = conn1
            if T[x1][y1] == 'N2' and (P[a][b][0] - P[a][b][1] != 0 and P[a][b][0] + P[a][b][1] != 700):
              for conn2 in G[(x1, y1)]:
                x2, y2 = conn2
                if (x2 == a or y2 == b) and T[x2][y2] == 'N3':
                  mact = [(a, b), (x1, y1), (x2, y2)]
                  if not buscarMolino(lmn, mact):
                    print(mact)
                    lmn.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
        elif T[a][b] == 'N2':
          aux = G[(a, b)]
          for conn1 in G[(a, b)]:
            x1, y1 = conn1
            if T[x1][y1] == 'N1':
              for conn2 in aux:
                x2, y2 = conn2
                if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and T[x2][y2] == 'N3':
                  mact = [(x1, y1), (a, b), (x2, y2)]
                  if not buscarMolino(lmn, mact):
                    print(mact)
                    lmn.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
            elif T[x1][y1] == 'N3':
              for conn2 in aux:
                x2, y2 = conn2
                if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and T[x2][y2] == 'N1':
                  mact = [(x1, y1), (a, b), (x2, y2)]
                  if not buscarMolino(lmn, mact):
                    print(mact)
                    lmn.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
        elif T[a][b] == 'N3' and (P[a][b][0] - P[a][b][1] == 300 or P[a][b][0] - P[a][b][1] == -300 or P[a][b][0] - P[a][b][1] == 100 or P[a][b][0] - P[a][b][1] == -100):
          for conn1 in G[(a, b)]:
            x1, y1 = conn1
            if T[x1][y1] == 'N2' and (P[a][b][1] - P[a][b][0] != 0 and P[a][b][1] + P[a][b][0] != 700):
              for conn2 in G[(x1, y1)]:
                x2, y2 = conn2
                if (x2 == a or y2 == b) and T[x2][y2] == 'N1':
                  mact = [(a, b), (x1, y1), (x2, y2)]
                  if not buscarMolino(lmn, mact):
                    print(mact)
                    lmn.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
  print('turno negro')
  t = 'B'
  mol = False
  return mol



def verificarMolinoBlanco(a, b):
  global mol, T, t, lmb
  if t == 'B':
    if (T[a][b] == 'B1' and f1b > 0) or (T[a][b] == 'B3' and f3b > 0) or (T[a][b] == 'B2' and f2b > 0):
      if P[a][b][0] - P[a][b][1] == 0 or P[a][b][0] + P[a][b][1] == 700:
        if T[a][b] == 'B1':
          for conn1 in G[(a, b)]:
            x1, y1 = conn1
            if T[x1][y1] == 'B2':
              for conn2 in G[(x1, y1)]:
                x2, y2 = conn2
                if (x2 == a or y2 == b) and T[x2][y2] == 'B3':
                  mact = [(a, b), (x1, y1), (x2, y2)]
                  if not buscarMolino(lmb, mact):
                    print(mact)
                    lmb.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
        elif T[a][b] == 'B3':
          for conn1 in G[(a, b)]:
            x1, y1 = conn1
            if T[x1][y1] == 'B2':
              for conn2 in G[(x1, y1)]:
                x2, y2 = conn2
                if (x2 == a or y2 == b) and T[x2][y2] == 'B1':
                  mact = [(a, b), conn1, conn2]
                  if not buscarMolino(lmb, mact):
                    print(mact)
                    lmb.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
      else:
        if T[a][b] == 'B1' and (P[a][b][0] - P[a][b][1] == 300 or P[a][b][0] - P[a][b][1] == -300 or P[a][b][0] - P[a][b][1] == 100 or P[a][b][0] - P[a][b][1] == -100):
          for conn1 in G[(a, b)]:
            x1, y1 = conn1
            if T[x1][y1] == 'B2' and (P[a][b][0] - P[a][b][1] != 0 and P[a][b][0] + P[a][b][1] != 700):
              for conn2 in G[(x1, y1)]:
                x2, y2 = conn2
                if (x2 == a or y2 == b) and T[x2][y2] == 'B3':
                  mact = [(a, b), (x1, y1), (x2, y2)]
                  if not buscarMolino(lmb, mact):
                    print(mact)
                    lmb.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
        elif T[a][b] == 'B2':
          aux = G[(a, b)]
          for conn1 in G[(a, b)]:
            x1, y1 = conn1
            if T[x1][y1] == 'B1':
              for conn2 in aux:
                x2, y2 = conn2
                if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and T[x2][y2] == 'B3':
                  mact = [(x1, y1), (a, b), (x2, y2)]
                  if not buscarMolino(lmb, mact):
                    print(mact)
                    lmb.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
            elif T[x1][y1] == 'B3':
              for conn2 in aux:
                x2, y2 = conn2
                if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and T[x2][y2] == 'B1':
                  mact = [(x1, y1), (a, b), (x2, y2)]
                  if not buscarMolino(lmb, mact):
                    print(mact)
                    lmb.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
        elif T[a][b] == 'B3' and (P[a][b][0] - P[a][b][1] == 300 or P[a][b][0] - P[a][b][1] == -300 or P[a][b][0] - P[a][b][1] == 100 or P[a][b][0] - P[a][b][1] == -100):
          for conn1 in G[(a, b)]:
            x1, y1 = conn1
            if T[x1][y1] == 'B2' and (P[a][b][1] - P[a][b][0] != 0 and P[a][b][1] + P[a][b][0] != 700):
              for conn2 in G[(x1, y1)]:
                x2, y2 = conn2
                if (x2 == a or y2 == b) and T[x2][y2] == 'B1':
                  mact = [(a, b), (x1, y1), (x2, y2)]
                  if not buscarMolino(lmb, mact):
                    print(mact)
                    lmb.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
  print('turno negro')
  t = 'N'
  mol = False
  return mol


def PosicionarFichaBlanca(a, b):
  global T, f1b, f2b, f3b, t, f1n, f2n, f3n, F, nB, FGB, mol
  if F == 1 and not mol and t == 'B' and T[a][b] == 'v':
    if nB == 1:
      f1b += 1
      T[a][b] = 'B1'
    elif nB == 2:
      f2b += 1
      T[a][b] = 'B2'
    elif nB == 3:
      f3b += 1
      T[a][b] = 'B3'
    
    verificarMolinoBlanco(a, b)
    # t = 'N'
    FGB -= 1

    if FGB + FGN == 0:
      F = 2
      # mol = True
  
    nB = 1 if nB > 2 else nB + 1


#aux
nB = 1
nN = 1
nuevaPos = ()
    
#REGLAS 
    
def PosicionarFichaNegra(a, b):
  global T, f1n, f2n, f3n, t, f1b, f2b, f3b, F, nN, FGN, mol
  if F == 1 and not mol and t == 'N' and T[a][b] == 'v':
    if nN == 1:
      f1n += 1
      T[a][b] = 'N1'
    elif nN == 2:
      f2n += 1
      T[a][b] = 'N2'
    elif nN == 3:
      f3n += 1
      T[a][b] = 'N3'
    
    verificarMolinoNegro(a, b)
    # t = 'B'
    FGN -= 1

    if FGN + FGB == 0:
      F = 2
      # mol = True
      
  
    nN = 1 if nN > 2 else nN + 1


 
# MOVER FICHA
def MoverFichaBlanca(a, b, x, y):
  global T, F, mol, t, f1b, f2b, f3b, conexiones
  if F == 2:
    if t == 'B':  
      if not mol and T[x][y] == 'v' and (x, y) in G[(a, b)] and T[a][b] in ['B1', 'B2', 'B3']:
          T[x][y], T[a][b] = T[a][b], 'v'
          verificarMolinoBlanco(x, y)
      
  else:
    print("Fase no válida. Sólo puedes mover piezas en la fase 2.")

def MoverFichaNegra(a, b, x, y):
  global T, F, mol, t, f1n, f2n, f3n, conexiones
  if F == 2:
    if t == 'N':
      if not mol and T[x][y] == 'v' and (x, y) in G[(a, b)] and T[a][b] in ['N1', 'N2', 'N3']:
        T[x][y], T[a][b] = T[a][b], 'v'
        verificarMolinoNegro(x, y)
      
      
  else:
    print("Fase no válida. Sólo puedes mover piezas en la fase 2.")
        
# Quitar la ficha con numero n de la posicion M[a][b]
def quitarFichaNegra(a, b):
  global mol, T, f1n, f2n, f3n, t
  if t == 'B' and mol and T[a][b] in ['N1', 'N2', 'N3']:
    if T[a][b] == 'N1' and f1n > 0:
      f1n -= 1
    elif T[a][b] == 'N2' and f2n > 0:
      f2n -= 1
    elif T[a][b] == 'N3' and f3n > 0:
      f3n -= 1
    T[a][b] = 'v'
    t = 'N'
    mol = False

# Quitar la ficha blanca con numero n de la posicion M[a][b]
def quitarFichaBlanca(a, b):
  global mol, T, f1b, f2b, f3b, t
  if t == 'N' and mol and T[a][b] in ['B1', 'B2', 'B3']:
    if T[a][b] == 'B1' and f1b > 0:
      f1b -= 1
    elif T[a][b] == 'B2' and f2b > 0:
      f2b -= 1
    elif T[a][b] == 'B3' and f3b > 0:
      f3b -= 1
    T[a][b] = 'v'
    t = 'B'
    mol = False


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
  
  # Draw the positions (REFACTORIZADO)
  for i, filas in enumerate(T):
    for j, elemento in enumerate(filas):
      if(elemento == 'v'):
        pygame.draw.circle(window, BLUE, P[i][j] , 20)
      elif(elemento == 'N1'):
        dibujarPosition(P[i][j], BLACK, 1)
      elif(elemento == 'N2'):
        dibujarPosition(P[i][j], BLACK, 2)
      elif(elemento == 'N3'):
        dibujarPosition(P[i][j], BLACK, 3)
      elif(elemento == 'B1'):
        dibujarPosition(P[i][j], WHITE, 1)
      elif(elemento == 'B2'):
         dibujarPosition(P[i][j], WHITE, 2)
      elif(elemento == 'B3'):
        dibujarPosition(P[i][j], WHITE, 3)
    
  # Update the display
  pygame.display.update()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        print(event.pos)
        pos = hallar_posicion(event.pos)
        if pos is not None:
          PosicionarFichaBlanca(pos[0], pos[1])
          PosicionarFichaNegra(pos[0], pos[1])
          quitarFichaBlanca(pos[0], pos[1])
          quitarFichaNegra(pos[0], pos[1])
      elif event.button == 3:
        if pos is not None:
          nuevaPos = hallar_posicion(event.pos)
          if nuevaPos is not None:
            MoverFichaBlanca(pos[0], pos[1], nuevaPos[0], nuevaPos[1])
            MoverFichaNegra(pos[0], pos[1], nuevaPos[0], nuevaPos[1])