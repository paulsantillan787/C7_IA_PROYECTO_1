T = [
  [((50, 50),'N1'),None,None,((350, 50),'B1'),None,None,((650, 50),'B3')],
  [None,((150, 150),'N1'),None,((350, 150),'B2'),None,((550, 150),'v'),None],
  [None,None,((250, 250),'v'),((350, 250),'B3'),((450, 250),'v'),None,None],
  [((50, 350),'N2'),((150, 350),'v'),((250, 350),'N3'),"c",((450, 350),'N2'),((550, 350),'N2'),((650, 350),'N3')],
  [None,None,((250, 450),'v'),((350, 450),'v'),((450, 450),'v'),None,None],
  [None,((150, 550),'N1'),None,((350, 550),'v'),None,((550, 550),'v'),None],
  [((50, 650),'N3'),None,None,((350, 650),'N3'),None,None,((650, 650),'N2')]
]
t = 'B'
F = 1
f1n = 3
f2n = 3
f3n = 3
f1b = 3
f2b = 3
f3b = 3
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
    (150, 350): [(50, 350), (150, 150), (250, 350), (150, 550)],
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

# Funciones auxiliares
def hallar_posicion(pos):
  for filas in T:
    for elemento in filas:
      if isinstance(elemento, tuple):
        x = elemento[0][0]
        y = elemento[0][1]
        if x - 20 <= pos[0] <= x + 20 and y - 20 <= pos[1] <= y + 20:
          return (T.index(filas), filas.index(elemento))

  return None

def buscarMolino(listaMolino, mact):
    return mact in listaMolino

def verficarMolinoNegro(a, b):
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
        elif(T[a][b][1] == 'N3'):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'N2' and ((T[a][b][0][1] - T[a][b][0][0] != 0 and T[a][b][0][1] + T[a][b][0][0] != 700))):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[y1][y2][1] == 'N1'):
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
  t = 'B'
  mol = False
  return mol

def verficarMolinoBlanco(a, b):
  global mol, T, t, lmn
  if(t == 'B'):
    if(isinstance(T[a][b], tuple) and ( (T[a][b][1] == 'B1' and f1n > 0) or (T[a][b][1] == 'B3' and f3n > 0)  or (T[a][b][1] == 'B2' and f2n > 0) )):
      if((T[a][b][0][0] - T[a][b][0][1] == 0 or T[a][b][0][0] + T[a][b][0][1] == 700)):
        if(T[a][b][1] == 'B1'):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'B2'):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[x2][y2][1] == 'B3'):
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
        elif(T[a][b][1] == 'B3'):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'B2'):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[x2][y2][1] == 'B1'):
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
        if(T[a][b][1] == 'B1' and ((T[a][b][0][0] - T[a][b][0][1] == 300 or T[a][b][0][0] - T[a][b][0][1] == -300 or T[a][b][0][0] - T[a][b][0][1] == 100 or T[a][b][0][0] - T[a][b][0][1] == -100))):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'B2' and ((T[a][b][0][0] - T[a][b][0][1] != 0 and T[a][b][0][0] + T[a][b][0][1] != 700))):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[x2][y2][1] == 'B3'):
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
        elif(T[a][b][1] == 'B2'):
            aux = G[T[a][b][0]]
            for conn1 in G[T[a][b][0]]:
              x1, y1 = hallar_posicion(conn1)
              if(T[x1][y1][1] == 'B1'):
                for conn2 in aux:
                  x2, y2 = hallar_posicion(conn2)
                  if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and T[x2][y2][1] == 'B3':
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
              elif(T[x1][y1][1] == 'B3'):
                for conn2 in aux:
                  x2, y2 = hallar_posicion(conn2)
                  if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and T[x2][y2][1] == 'B1':
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
        elif(T[a][b][1] == 'B3'):
          for conn1 in G[T[a][b][0]]:
            x1, y1 = hallar_posicion(conn1)
            if(T[x1][y1][1] == 'B2' and ((T[a][b][0][1] - T[a][b][0][0] != 0 and T[a][b][0][1] + T[a][b][0][0] != 700))):
              for conn2 in G[conn1]:
                x2, y2 = hallar_posicion(conn2)
                if((conn2[0] == T[a][b][0][0] or conn2[1] == T[a][b][0][1]) and T[y1][y2][1] == 'B1'):
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
  t = 'N'
  mol = False
  return mol

if __name__ == "__main__":
  print(verficarMolinoBlanco(0, 3))
  print(mact)
  mol = False
  t = 'N'
  print(verficarMolinoNegro(3, 0))
  print(mact)