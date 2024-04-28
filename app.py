import pygame

# Initialize Pygame
pygame.init()

T = [
  [((50, 50),'v'),None,None,((350, 50),'v'),None,None,((650, 50),'v')],
  [None,((150, 150),'v'),None,((350, 150),'v'),None,((550, 150),'v'),None],
  [None,None,((250, 250),'v'),((350, 250),'v'),((450, 250),'v'),None,None],
  [((50, 350),'v'),((150, 350),'v'),((250, 350),'v'),"c",((450, 350),'v'),((550, 350),'v'),((650, 350),'v')],
  [None,None,((250, 450),'v'),((350, 450),'v'),((450, 450),'v'),None,None],
  [None,((150, 550),'v'),None,((350, 550),'v'),None,((550, 550),'v'),None],
  [((50, 650),'v'),None,None,((350, 650),'v'),None,None,((650, 650),'v')]
]

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
fbm = False
fnm = False
mol = False
mact = []
lmn = []
lmb = []

G = {
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
    (150, 350): [(150, 550), (150, 150), (250, 350),(50, 350)],
    (250, 350): [(150, 350), (250, 250), (250, 450)],
    (450, 350): [(450, 250), (550, 350), (450, 450)],
    (550, 350): [(450, 350), (550, 150), (650, 350), (550, 550)],
    (650, 350): [(550, 350), (650, 50), (650, 650)],
    (250, 450): [(250, 350), (350, 450)],
    (350, 450): [(250, 450), (450, 450), (350, 550)],
    (450, 450): [(350, 450), (450, 350)],
    (150, 550): [(150, 350), (350, 550)],
    (350, 550): [(150, 550), (350, 450), (550, 550)],
    (550, 550): [(350, 550), (550, 350)],
    (50, 650): [(50, 350), (350, 650)],
    (350, 650): [(50, 650), (650, 650), (350, 550)],
    (650, 650): [(350, 650), (650, 350)]
}

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
  for filas in T:
    for elemento in filas:
      if isinstance(elemento, tuple):
        x = elemento[0][0]
        y = elemento[0][1]
        if x - 25 <= pos[0] <= x + 25 and y - 25 <= pos[1] <= y + 25:
          return (T.index(filas), filas.index(elemento))

  return None

def dibujarPosition(x, y, color, number):
  pygame.draw.circle(window, color, (x, y), 30)
  font = pygame.font.Font(None, 36)
  if(color == BLACK):
    text_surface = font.render(str(number), True, WHITE)
  else:
    text_surface = font.render(str(number), True, BLACK)
  
  text_x = x - text_surface.get_width() / 2
  text_y = y - text_surface.get_height() / 2
  text_position = (text_x, text_y)
  window.blit(text_surface, text_position)
  
#aux
nB = 1
nN = 1
nuevaPos = ()


def PosicionarFichaBlanca(a, b):
  global T, f1b, f2b, f3b, t, f1n, f2n, f3n, F, nB, FGB
  if F == 1:
    print('A0')
    print(mol)
    if not mol and t == 'B' and isinstance(T[a][b], tuple) and T[a][b][1] == 'v':
      print('A1')
      # Sea la ficha a posicionar, se toma en cuenta el numero de la ficha
      if nB == 1:
        f1b += 1
        T[a][b] = (T[a][b][0], 'B1')
      elif nB == 2:
        f2b += 1
        T[a][b] = (T[a][b][0], 'B2')
      elif nB == 3:
        f3b += 1
        T[a][b] = (T[a][b][0], 'B3')
      
      # Incluir función verificarMolino(x,y,n)
      verificarMolinoBlanco(a, b)
      FGB -= 1
      print(FGB)
      
      if FGB + FGN == 0:
        # Si se consumió todas las fichas, se cambia de fase
        F = 2
        print(F)
        
      nB += 1
      if nB > 3:
        nB = 1
        
      
    
    
    
def PosicionarFichaNegra(a, b):
  global T, f1n, f2n, f3n, t, f1b, f2b, f3b, F, nN, FGN
  if F == 1:
    print('A2')
    
    if not mol and t == 'N' and isinstance(T[a][b], tuple) and T[a][b][1] == 'v':
      print('A3')
      # Sea la ficha a posicionar, se toma en cuenta el numero de la ficha
      if nN == 1:
        f1n += 1
        T[a][b] = (T[a][b][0], 'N1')
      elif nN == 2:
        f2n += 1
        T[a][b] = (T[a][b][0], 'N2')
      elif nN == 3:
        f3n += 1
        T[a][b] = (T[a][b][0], 'N3')
      # Incluir función verificarMolino(x,y,n)
      
      verificarMolinoNegro(a, b)
      print(FGN)
      FGN -= 1
      
      if FGN + FGB== 0:
        # Si se consumio todas las fichas, se cambia de fase
        F = 2
        print(F)
      
      nN += 1
      if nN > 3:
        nN = 1
        
 
 
# BORRAR
def MoverFichaBlanca(a, b, x, y):
  global T, F, n, mol, t, f1b, f2b, f3b
  if F == 2:  
    if(not mol and isinstance(T[a][b], tuple)
      and isinstance(T[x][y], tuple)
      and T[x][y][1] == "v"  
      and (T[x][y][0] in G[T[a][b][0]]) 
      and ((T[a][b][1] == 'B1' and (f1b > 0 and f1b < 4)) 
      or (T[a][b][1] == 'B2' and (f2b > 0 and f2b < 4))
      or (T[a][b][1] == 'B3' and (f2b > 0 and f2b < 4)))):
      if t == "B":
        if (T[a][b][1]=="B1"):
          for conn in G[T[a][b][0]]:
            x1, y2 = hallar_posicion(conn)
            if T[x1][y2] == T[x][y]:
              T[x][y] = (T[x][y][0],"B1")
        if (T[a][b][1]=="B2"):
          for conn in G[T[a][b][0]]:
            x1, y2 = hallar_posicion(conn)
            if T[x1][y2] == T[x][y]:
              T[x][y] = (T[x][y][0],"B2" ) 
        if (T[a][b][1]=="B3"):
          for conn in G[T[a][b][0]]:
            x1, y2 = hallar_posicion(conn)
            if T[x1][y2] == T[x][y]:
              T[x][y] = (T[x][y][0],"B3" )
        T[a][b] = (T[a][b][0],"v" )
        mol = verificarMolinoBlanco(x, y)
        if mol:
          quitarFichaNegra(x, y)
      else:
        print("Movimiento no válido. No es tu turno.")
    else:
      print("Movimiento no válido. La posición seleccionada no es válida o la pieza seleccionada no está disponible.")
  else:
    print("Fase no válida. Sólo puedes mover piezas en la fase 2.")

def MoverFichaNegra(a, b, x, y):
    global T, F, n, mol, t, f1n, f2n, f3n
    if F == 2:
        if (not mol
            and isinstance(T[a][b], tuple)
            and isinstance(T[x][y], tuple)
            and T[x][y][1] == "v"
            and (T[x][y][0] in G[T[a][b][0]])
            and ((T[a][b][1] == "N1" and (f1n > 0 and f1n < 4))
                or (T[a][b][1] == "N2" and (f2n > 0 and f2n < 4))
                or (T[a][b][1] == "N3" and (f2n > 0 and f2n < 4)))):
            if t == "N":
                if T[a][b][1] == "N1":
                    for conn in G[T[a][b][0]]:
                        x1, y2 = hallar_posicion(conn)
                        if T[x1][y2] == T[x][y]:
                            T[x][y] = (T[x][y][0], "N1")
                if T[a][b][1] == "N2":
                    for conn in G[T[a][b][0]]:
                        x1, y2 = hallar_posicion(conn)
                        if T[x1][y2] == T[x][y]:
                            T[x][y] = (T[x][y][0], "N2")
                if T[a][b][1] == "N3":
                    for conn in G[T[a][b][0]]:
                        x1, y2 = hallar_posicion(conn)
                        if T[x1][y2] == T[x][y]:
                            T[x][y] = (T[x][y][0], "N3")
                T[a][b] = (T[a][b][0], "v")
                mol = verificarMolinoNegro(x, y)
                if mol:
                  quitarFichaBlanca(x, y)
            else:
                print("Movimiento no válido. No es tu turno.")
        else:
            print("Movimiento no válido. La posición seleccionada no es válida o la pieza seleccionada no está disponible.")
    else:
        print("Fase no válida. Sólo puedes mover piezas en la fase 2.")


def buscarMolino(listaMolino, mact):
  return mact in listaMolino

def verificarMolinoNegro(a, b):
  global mol, T, t, lmn
  if(t == 'N'):
    if(isinstance(T[a][b], tuple) and ( (T[a][b][1] == 'N1' and f1n > 0) or (T[a][b][1] == 'N3' and f3n > 0)  or (T[a][b][1] == 'N2' and f2n > 0) )):
      if((T[a][b][0][0] - T[a][b][0][1] == 0 or T[a][b][0][0] + T[a][b][0][1] == 700)):
        if(T[a][b][1] == 'N1'):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'N2'):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[x2][y2][1] == 'N3'):
                  mact = [T[a][b][0], conn1, conn2]
                  if(not buscarMolino(lmn, mact)):
                    print(mact)
                    lmn.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
        elif(T[a][b][1] == 'N3'):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'N2'):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[x2][y2][1] == 'N1'):
                  mact = [T[a][b][0], conn1, conn2]
                  if(not buscarMolino(lmn, mact)):
                    print(mact)
                    lmn.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
      else:
        if(T[a][b][1] == 'N1' and ((T[a][b][0][0] - T[a][b][0][1] == 300 or T[a][b][0][0] - T[a][b][0][1] == -300 or T[a][b][0][0] - T[a][b][0][1] == 100 or T[a][b][0][0] - T[a][b][0][1] == -100))):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'N2' and ((T[a][b][0][0] - T[a][b][0][1] != 0 and T[a][b][0][0] + T[a][b][0][1] != 700))):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[x2][y2][1] == 'N3'):
                  mact = [T[a][b][0], conn1, conn2]
                  if(not buscarMolino(lmn, mact)):
                    print(mact)
                    lmn.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
        elif(T[a][b][1] == 'N2'):
            aux = G[T[a][b][0]]
            for conn1 in G[T[a][b][0]]:
              x1, y1 = hallar_posicion(conn1)
              if(T[x1][y1][1] == 'N1'):
                for conn2 in aux:
                  x2, y2 = hallar_posicion(conn2)
                  if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and T[x2][y2][1] == 'N3':
                    mact = [conn1, T[a][b][0], conn2]
                    if(not buscarMolino(lmn, mact)):
                      print(mact)
                      lmn.append(mact)
                      mol = True
                      mact = []
                      return mol
                    else:
                      mol = False
                      return mol
              elif(T[x1][y1][1] == 'N3'):
                for conn2 in aux:
                  x2, y2 = hallar_posicion(conn2)
                  if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and T[x2][y2][1] == 'N1':
                    mact = [conn1, T[a][b][0], conn2]
                    if(not buscarMolino(lmn, mact)):
                      print(mact)
                      lmn.append(mact)
                      mol = True
                      mact = []
                      return mol
                    else:
                      mol = False
                      return mol
        elif(T[a][b][1] == 'N3' and ((T[a][b][0][0] - T[a][b][0][1] == 300 or T[a][b][0][0] - T[a][b][0][1] == -300 or T[a][b][0][0] - T[a][b][0][1] == 100 or T[a][b][0][0] - T[a][b][0][1] == -100))):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'N2' and ((T[a][b][0][1] - T[a][b][0][0] != 0 and T[a][b][0][1] + T[a][b][0][0] != 700))):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[x2][y2][1] == 'N1'):
                  mact = [T[a][b][0], conn1, conn2]
                  if(not buscarMolino(lmn, mact)):
                    print(mact)
                    lmn.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
  print('turno blanco')
  t = 'B'
  mol = False
  return mol

def verificarMolinoBlanco(a, b):
  global mol, T, t, lmb
  if(t == 'B'):
    if(isinstance(T[a][b], tuple) and ( (T[a][b][1] == 'B1' and f1b > 0) or (T[a][b][1] == 'B3' and f3b > 0)  or (T[a][b][1] == 'B2' and f2b > 0) )):
      if((T[a][b][0][0] - T[a][b][0][1] == 0 or T[a][b][0][0] + T[a][b][0][1] == 700)):
        if(T[a][b][1] == 'B1'):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'B2'):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[x2][y2][1] == 'B3'):
                  mact = [T[a][b][0], conn1, conn2]
                  if(not buscarMolino(lmb, mact)):
                    print(mact)
                    lmb.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
        elif(T[a][b][1] == 'B3'):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'B2'):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[x2][y2][1] == 'B1'):
                  mact = [T[a][b][0], conn1, conn2]
                  if(not buscarMolino(lmb, mact)):
                    print(mact)
                    lmb.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
      else:
        if(T[a][b][1] == 'B1' and ((T[a][b][0][0] - T[a][b][0][1] == 300 or T[a][b][0][0] - T[a][b][0][1] == -300 or T[a][b][0][0] - T[a][b][0][1] == 100 or T[a][b][0][0] - T[a][b][0][1] == -100))):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'B2' and ((T[a][b][0][0] - T[a][b][0][1] != 0 and T[a][b][0][0] + T[a][b][0][1] != 700))):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[x2][y2][1] == 'B3'):
                  mact = [T[a][b][0], conn1, conn2]
                  if(not buscarMolino(lmb, mact)):
                    print(mact)
                    lmb.append(mact)
                    mol = True
                    mact = []
                    return mol
                  else:
                    mol = False
                    return mol
        elif(T[a][b][1] == 'B2'):
            aux = G[T[a][b][0]]
            for conn1 in G[T[a][b][0]]:
              x1, y1 = hallar_posicion(conn1)
              if(T[x1][y1][1] == 'B1'):
                for conn2 in aux:
                  x2, y2 = hallar_posicion(conn2)
                  if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and T[x2][y2][1] == 'B3':
                    mact = [conn1, T[a][b][0], conn2]
                    if(not buscarMolino(lmb, mact)):
                      print(mact)
                      lmb.append(mact)
                      mol = True
                      mact = []
                      return mol
                    else:
                      mol = False
                      return mol
              elif(T[x1][y1][1] == 'B3'):
                for conn2 in aux:
                  x2, y2 = hallar_posicion(conn2)
                  if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and T[x2][y2][1] == 'B1':
                    mact = [conn1, T[a][b][0], conn2]
                    if(not buscarMolino(lmb, mact)):
                      print(mact)
                      lmb.append(mact)
                      mol = True
                      mact = []
                      return mol
                    else:
                      mol = False
                      return mol
        elif(T[a][b][1] == 'B3' and ((T[a][b][0][0] - T[a][b][0][1] == 300 or T[a][b][0][0] - T[a][b][0][1] == -300 or T[a][b][0][0] - T[a][b][0][1] == 100 or T[a][b][0][0] - T[a][b][0][1] == -100))):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'B2' and ((T[a][b][0][1] - T[a][b][0][0] != 0 and T[a][b][0][1] + T[a][b][0][0] != 700))):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[x2][y2][1] == 'B1'):
                  mact = [T[a][b][0], conn1, conn2]
                  if(not buscarMolino(lmb, mact)):
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
  
# Quitar la ficha con numero n de la posicion M[a][b]
def quitarFichaNegra(a, b):
  global mol, T, f1n, f2n, f3n, t
  if t == 'B':
    if(mol and isinstance(T[a][b], tuple) and ((T[a][b][1] == 'N1' and f1n > 0) or (T[a][b][1] == 'N2' and f2n > 0) or (T[a][b][1] == 'N3' and f3n > 0))):
      if(T[a][b][1] == 'N1'):
        # global f1n
        f1n -= 1
      elif(T[a][b][1] == 'N2'):
        # global f2n
        f2n -= 1
      elif(T[a][b][1] == 'N3'):
        # global f3n
        f3n -= 1
      T[a][b] = (T[a][b][0], 'v')
      # global t
      t = 'N'
      # global mol
      mol = False

# Quitar la ficha blanca con numero n de la posicion M[a][b]
def quitarFichaBlanca(a, b):
  global mol, T, f1b, f2b, f3b, t
  if t == 'N':
    if(mol and isinstance(T[a][b], tuple) and ((T[a][b][1] == 'B1'and f1b > 0) or (T[a][b][1] == 'B2' and f2b > 0) or (T[a][b][1] == 'B3' and f3b > 0))):
      if(T[a][b][1] == 'B1'):
        # global f1b
        f1b -= 1
      elif(T[a][b][1] == 'B2'):
        # global f2b
        f2b -= 1
      elif(T[a][b][1] == 'B3'):
        # global f3b
        f3b -= 1
      T[a][b] = (T[a][b][0], 'v')
      # global t
      t = 'B'
      # global mol
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
  for filas in T:
    for elemento in filas:
      if isinstance(elemento, tuple):
        if(elemento[1] == 'v'):
          pygame.draw.circle(window, BLUE, elemento[0] , 20)
        elif(elemento[1] == 'N1'):
          dibujarPosition(elemento[0][0], elemento[0][1], BLACK, 1)
        elif(elemento[1] == 'N2'):
          dibujarPosition(elemento[0][0], elemento[0][1], BLACK, 2)
        elif(elemento[1] == 'N3'):
          dibujarPosition(elemento[0][0], elemento[0][1], BLACK, 3)
        elif(elemento[1] == 'B1'):
          dibujarPosition(elemento[0][0], elemento[0][1], WHITE, 1)
        elif(elemento[1] == 'B2'):
          dibujarPosition(elemento[0][0], elemento[0][1], WHITE, 2)
        elif(elemento[1] == 'B3'):
          dibujarPosition(elemento[0][0], elemento[0][1], WHITE, 3)
          
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
          print(T[pos[0]][pos[1]][1])
          PosicionarFichaBlanca(pos[0], pos[1])
          PosicionarFichaNegra(pos[0], pos[1])
          quitarFichaNegra(pos[0], pos[1])
          quitarFichaBlanca(pos[0], pos[1])
      elif event.button == 3:
        nuevaPos = hallar_posicion(event.pos)
        if nuevaPos is not None:
          MoverFichaBlanca(pos[0], pos[1], nuevaPos[0], nuevaPos[1])
          MoverFichaNegra(pos[0], pos[1], nuevaPos[0], nuevaPos[1])
  
  
# Quit Pygame
pygame.quit()
