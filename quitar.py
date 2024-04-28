T = [
  [((50, 50),'B1'),None,None,((350, 50),'N2'),None,None,((650, 50),'B3')],
  [None,((150, 150),'N1'),None,((350, 150),'v'),None,((550, 150),'v'),None],
  [None,None,((250, 250),'v'),((350, 250),'v'),((450, 250),'v'),None,None],
  [((50, 350),'N1'),((150, 350),'v'),((250, 350),'N3'),"c",((450, 350),'N2'),((550, 350),'N2'),((650, 350),'N3')],
  [None,None,((250, 450),'v'),((350, 450),'v'),((450, 450),'v'),None,None],
  [None,((150, 550),'N1'),None,((350, 550),'v'),None,((550, 550),'v'),None],
  [((50, 650),'v'),None,None,((350, 650),'N1'),None,None,((650, 650),'v')]
]
t = 'N'
F = 2
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

def hallar_posicion(pos):
  for filas in T:
    for elemento in filas:
      if isinstance(elemento, tuple):
        x = elemento[0][0]
        y = elemento[0][1]
        if x - 20 <= pos[0] <= x + 20 and y - 20 <= pos[1] <= y + 20:
          return (T.index(filas), filas.index(elemento))

  return None

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


# Quitar la ficha con numero n de la posicion M[a][b]
def quitarFichaNegra(a, b, n):
  global mol, T, f1n, f2n, f3n, t
  if(mol and isinstance(T[a][b], tuple) and ((T[a][b][1] == 'N1' and f1n > 0) or (T[a][b] == 'N2' and f2n > 0) or (T[a][b] == 'N3' and f3n > 0))):
    if(n == 1):
      # global f1n
      f1n -= 1
    elif(n == 2):
      # global f2n
      f2n -= 1
    elif(n == 3):
      # global f3n
      f3n -= 1
    T[a][b] = (T[a][b][0], 'v')
    # global t
    t = 'B'
    # global mol
    mol = False
    return 1
  return 0

# Quitar la ficha blanca con numero n de la posicion M[a][b]
def quitarFichaBlanca(a, b, n):
  global mol, T, f1n, f2n, f3n, t
  if(mol and isinstance(T[a][b], tuple) and ((T[a][b][1] == 'B1'and f1b > 0) or (T[a][b] == 'B2' and f2b > 0) or (T[a][b] == 'B3' and f3b > 0))):
    if(n == 1):
      # global f1b
      f1b -= 1
    elif(n == 2):
      # global f2b
      f2b -= 1
    elif(n == 3):
      # global f3b
      f3b -= 1
    T[a][b] = (T[a][b][0], 'v')
    # global t
    t = 'N'
    # global mol
    mol = False
    return 1
  return 0

# Imprimir las posiciones enla matriz T donde no es None
def imprimirPosiciones():
  for i in range(7):
    for j in range(7):
      if(isinstance(T[i][j], tuple)):
        print(T[i][j][1])
        
if __name__ == '__main__':
  #MoverFichaBlanca(6, 3, 6, 6)
  #print(T[6][6])
  #MoverFichaBlanca(0, 3, 1, 3)
  #print(T[1][3])
  MoverFichaNegra(6, 3, 6, 6)
  print(T[6][6])
  MoverFichaNegra(0, 3, 1, 3)
  print(T[1][3])
