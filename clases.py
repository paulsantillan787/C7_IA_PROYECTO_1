class Juego:
  
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
  
  #aux
  nB = 1
  nN = 1
  nuevaPos = ()
  
  def __init__(self):
    pass
  
  # Funciones auxiliares
  def hallar_posicion(self, pos):
    for i, filas in enumerate(self.P):
      for j, elemento in enumerate(filas):
        if elemento is not None:
          x = elemento[0]
          y = elemento[1]
          if x - 25 <= pos[0] <= x + 25 and y - 25 <= pos[1] <= y + 25:
            return (i, j)

    return None
    
    
  def buscarMolino(listaMolino, mact):
    return mact in listaMolino

  def verificarMolinoNegro(self, a, b):
    if self.t == 'N':
      if self.T[a][b] in ['N1', 'N2', 'N3'] and (self.T[a][b] == 'N1' and self.f1n > 0) or (self.T[a][b] == 'N3' and self.f3n > 0) or (self.T[a][b] == 'N2' and self.f2n > 0):
        if self.P[a][b][0] - self.P[a][b][1] == 0 or self.P[a][b][0] + self.P[a][b][1] == 700:
          if self.T[a][b] == 'N1':
            for conn1 in self.G[(a, b)]:
              x1, y1 = conn1
              if self.T[x1][y1] == 'N2':
                for conn2 in self.G[(x1, y1)]:
                  x2, y2 = conn2
                  if (x2 == a or y2 == b) and self.T[x2][y2] == 'N3':
                    self.mact = [(a, b), (x1, y1), (x2, y2)]
                    if not self.buscarMolino(self.lmn, self.mact):
                      print(self.mact)
                      self.lmn.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
          elif self.T[a][b] == 'N3':
            for conn1 in self.G[(a, b)]:
              x1, y1 = conn1
              if self.T[x1][y1] == 'N2':
                for conn2 in self.G[(x1, y1)]:
                  x2, y2 = conn2
                  if (x2 == a or y2 == b) and self.T[x2][y2] == 'N1':
                    self.mact = [self.T[a][b][0], conn1, conn2]
                    if not self.buscarMolino(self.lmb, self.mact):
                      print(self.mact)
                      self.lmn.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
        else:
          if self.T[a][b] == 'N1' and (self.P[a][b][0] - self.P[a][b][1] == 300 or self.P[a][b][0] - self.P[a][b][1] == -300 or self.P[a][b][0] - self.P[a][b][1] == 100 or self.P[a][b][0] - self.P[a][b][1] == -100):
            for conn1 in self.G[(a, b)]:
              x1, y1 = conn1
              if self.T[x1][y1] == 'N2' and (self.P[a][b][0] - self.P[a][b][1] != 0 and self.P[a][b][0] + self.P[a][b][1] != 700):
                for conn2 in self.G[(x1, y1)]:
                  x2, y2 = conn2
                  if (x2 == a or y2 == b) and self.T[x2][y2] == 'N3':
                    self.mact = [(a, b), (x1, y1), (x2, y2)]
                    if not self.buscarMolino(self.lmn, self.mact):
                      print(self.mact)
                      self.lmn.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
          elif self.T[a][b] == 'N2':
            aux = self.G[(a, b)]
            for conn1 in self.G[(a, b)]:
              x1, y1 = conn1
              if self.T[x1][y1] == 'N1':
                for conn2 in aux:
                  x2, y2 = conn2
                  if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and self.T[x2][y2] == 'N3':
                    self.mact = [(x1, y1), (a, b), (x2, y2)]
                    if not self.buscarMolino(self.lmn, self.mact):
                      print(self.mact)
                      self.lmn.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
              elif self.T[x1][y1] == 'N3':
                for conn2 in aux:
                  x2, y2 = conn2
                  if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and self.T[x2][y2] == 'N1':
                    self.mact = [(x1, y1), (a, b), (x2, y2)]
                    if not self.buscarMolino(self.lmn, self.mact):
                      print(self.mact)
                      self.lmn.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
          elif self.T[a][b] == 'N3' and (self.P[a][b][0] - self.P[a][b][1] == 300 or self.P[a][b][0] - self.P[a][b][1] == -300 or self.P[a][b][0] - self.P[a][b][1] == 100 or self.P[a][b][0] - self.P[a][b][1] == -100):
            for conn1 in self.G[(a, b)]:
              x1, y1 = conn1
              if self.T[x1][y1] == 'N2' and (self.P[a][b][1] - self.P[a][b][0] != 0 and self.P[a][b][1] + self.P[a][b][0] != 700):
                for conn2 in self.G[(x1, y1)]:
                  x2, y2 = conn2
                  if (x2 == a or y2 == b) and self.T[x2][y2] == 'N1':
                    self.mact = [(a, b), (x1, y1), (x2, y2)]
                    if not self.buscarMolino(self.lmn, self.mact):
                      print(self.mact)
                      self.lmn.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
    print('turno negro')
    self.t = 'B'
    self.mol = False
    return self.mol



  def verificarMolinoBlanco(self, a, b):
    if self.t == 'B':
      if (self.T[a][b] == 'B1' and self.f1b > 0) or (self.T[a][b] == 'B3' and self.f3b > 0) or (self.T[a][b] == 'B2' and self.f2b > 0):
        if self.P[a][b][0] - self.P[a][b][1] == 0 or self.P[a][b][0] + self.P[a][b][1] == 700:
          if self.T[a][b] == 'B1':
            for conn1 in self.G[(a, b)]:
              x1, y1 = conn1
              if self.T[x1][y1] == 'B2':
                for conn2 in self.G[(x1, y1)]:
                  x2, y2 = conn2
                  if (x2 == a or y2 == b) and self.T[x2][y2] == 'B3':
                    self.mact = [(a, b), (x1, y1), (x2, y2)]
                    if not self.buscarMolino(self.lmb, self.mact):
                      print(self.mact)
                      self.lmb.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
          elif self.T[a][b] == 'B3':
            for conn1 in self.G[(a, b)]:
              x1, y1 = conn1
              if self.T[x1][y1] == 'B2':
                for conn2 in self.G[(x1, y1)]:
                  x2, y2 = conn2
                  if (x2 == a or y2 == b) and self.T[x2][y2] == 'B1':
                    self.mact = [(a, b), conn1, conn2]
                    if not self.buscarMolino(self.lmb, self.mact):
                      print(self.mact)
                      self.lmb.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
        else:
          if self.T[a][b] == 'B1' and (self.P[a][b][0] - self.P[a][b][1] == 300 or self.P[a][b][0] - self.P[a][b][1] == -300 or self.P[a][b][0] - self.P[a][b][1] == 100 or self.P[a][b][0] - self.P[a][b][1] == -100):
            for conn1 in self.G[(a, b)]:
              x1, y1 = conn1
              if self.T[x1][y1] == 'B2' and (self.P[a][b][0] - self.P[a][b][1] != 0 and self.P[a][b][0] + self.P[a][b][1] != 700):
                for conn2 in self.G[(x1, y1)]:
                  x2, y2 = conn2
                  if (x2 == a or y2 == b) and self.T[x2][y2] == 'B3':
                    self.mact = [(a, b), (x1, y1), (x2, y2)]
                    if not self.buscarMolino(self.lmb, self.mact):
                      print(self.mact)
                      self.lmb.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
          elif self.T[a][b] == 'B2':
            aux = self.G[(a, b)]
            for conn1 in self.G[(a, b)]:
              x1, y1 = conn1
              if self.T[x1][y1] == 'B1':
                for conn2 in aux:
                  x2, y2 = conn2
                  if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and self.T[x2][y2] == 'B3':
                    self.mact = [(x1, y1), (a, b), (x2, y2)]
                    if not self.buscarMolino(self.lmb, self.mact):
                      print(self.mact)
                      self.lmb.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
              elif self.T[x1][y1] == 'B3':
                for conn2 in aux:
                  x2, y2 = conn2
                  if conn2 != conn1 and (conn2[0] == conn1[0] or conn2[1] == conn1[1]) and self.T[x2][y2] == 'B1':
                    self.mact = [(x1, y1), (a, b), (x2, y2)]
                    if not self.buscarMolino(self.lmb, self.mact):
                      print(self.mact)
                      self.lmb.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
          elif self.T[a][b] == 'B3' and (self.P[a][b][0] - self.P[a][b][1] == 300 or self.P[a][b][0] - self.P[a][b][1] == -300 or self.P[a][b][0] - self.P[a][b][1] == 100 or self.P[a][b][0] - self.P[a][b][1] == -100):
            for conn1 in self.G[(a, b)]:
              x1, y1 = conn1
              if self.T[x1][y1] == 'B2' and (self.P[a][b][1] - self.P[a][b][0] != 0 and self.P[a][b][1] + self.P[a][b][0] != 700):
                for conn2 in self.G[(x1, y1)]:
                  x2, y2 = conn2
                  if (x2 == a or y2 == b) and self.T[x2][y2] == 'B1':
                    self.mact = [(a, b), (x1, y1), (x2, y2)]
                    if not self.buscarMolino(self.lmb, self.mact):
                      print(self.mact)
                      self.lmb.append(self.mact)
                      self.mol = True
                      self.mact = []
                      return self.mol
                    else:
                      self.mol = False
                      return self.mol
    print('turno negro')
    self.t = 'N'
    self.mol = False
    return self.mol


  def PosicionarFichaBlanca(self, a, b):
    if self.F == 1 and not self.mol and self.t == 'B' and self.T[a][b] == 'v':
      if self.nB == 1:
        self.f1b += 1
        self.T[a][b] = 'B1'
      elif self.nB == 2:
        self.f2b += 1
        self.T[a][b] = 'B2'
      elif self.nB == 3:
        self.f3b += 1
        self.T[a][b] = 'B3'
      
      self.verificarMolinoBlanco(a, b)
      # self.t = 'N'
      self.FGB -= 1

      if self.FGB + self.FGN == 0:
        self.F = 2
        # self.mol = True
    
      self.nB = 1 if self.nB > 2 else self.nB + 1

  def PosicionarFichaNegra(self, a, b):
    if self.F == 1 and not self.mol and self.t == 'N' and self.T[a][b] == 'v':
      if self.nN == 1:
        self.f1n += 1
        self.T[a][b] = 'N1'
      elif self.nN == 2:
        self.f2n += 1
        self.T[a][b] = 'N2'
      elif self.nN == 3:
        self.f3n += 1
        self.T[a][b] = 'N3'
      
      self.verificarMolinoNegro(a, b)
      # t = 'B'
      self.FGN -= 1

      if self.FGN + self.FGB == 0:
        self.F = 2
        # mol = True
        
    
      self.nN = 1 if self.nN > 2 else self.nN + 1


  
  # MOVER FICHA
  def MoverFichaBlanca(self, a, b, x, y):
    if self.F == 2:
      if self.t == 'B':  
        if not self.mol and self.T[x][y] == 'v' and (x, y) in self.G[(a, b)] and self.T[a][b] in ['B1', 'B2', 'B3']:
            self.T[x][y], self.T[a][b] = self.T[a][b], 'v'
            self.verificarMolinoBlanco(x, y)
        
    else:
      print("Fase no válida. Sólo puedes mover piezas en la fase 2.")

  def MoverFichaNegra(self, a, b, x, y):
    if self.F == 2:
      if self.t == 'N':
        if not self.mol and self.T[x][y] == 'v' and (x, y) in self.G[(a, b)] and self.T[a][b] in ['N1', 'N2', 'N3']:
          self.T[x][y], self.T[a][b] = self.T[a][b], 'v'
          self.verificarMolinoNegro(x, y)
        
        
    else:
      print("Fase no válida. Sólo puedes mover piezas en la fase 2.")
          
  # Quitar la ficha con numero n de la posicion M[a][b]
  def quitarFichaNegra(self, a, b):
    if self.t == 'B' and self.mol and self.T[a][b] in ['N1', 'N2', 'N3']:
      if self.T[a][b] == 'N1' and self.f1n > 0:
        self.f1n -= 1
      elif self.T[a][b] == 'N2' and self.f2n > 0:
        self.f2n -= 1
      elif self.T[a][b] == 'N3' and self.f3n > 0:
        self.f3n -= 1
      self.T[a][b] = 'v'
      self.t = 'N'
      self.mol = False

  # Quitar la ficha blanca con numero n de la posicion M[a][b]
  def quitarFichaBlanca(self, a, b):
    if self.t == 'N' and self.mol and self.T[a][b] in ['B1', 'B2', 'B3']:
      if self.T[a][b] == 'B1' and self.f1b > 0:
        self.f1b -= 1
      elif self.T[a][b] == 'B2' and self.f2b > 0:
        self.f2b -= 1
      elif self.T[a][b] == 'B3' and self.f3b > 0:
        self.f3b -= 1
      self.T[a][b] = 'v'
      self.t = 'B'
      self.mol = False