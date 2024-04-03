
class GamePiece :
  def __init__(self, color, position, number) -> None:
    self.color = color
    self.position = position
    self.number = number
    
  def draw(self, window, pygame):
    pygame.draw.circle(window, self.color, self.position, 30)
    
    font = pygame.font.Font(None, 36)
    
    text_surface = font.render(str(self.number), True, (0, 0, 0))
    
    text_x = self.position[0] - text_surface.get_width() / 2
    text_y = self.position[1] - text_surface.get_height() / 2
    text_position = (text_x, text_y)
    
    window.blit(text_surface, text_position)
    
  def move(self, position, ocupado, posiciones, connections):
    if ocupado[posiciones.index(position)] == 0 and position in connections[self.position]:
      ocupado[posiciones.index(self.position)] = 0
      self.position = position
      ocupado[posiciones.index(position)] = 1
      return True
    return False
    
    
    