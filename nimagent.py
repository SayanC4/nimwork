from nimgame import OneHeapNimGame
from random import choice, random

class OneHeapNimAgent:
  def __init__(self, game: OneHeapNimGame, pos: str):
    self.game = game
    self.pos = pos

  def move(self) -> int:
    return 0

class OneHeapPerfectAgent(OneHeapNimAgent):
  def __init__(self, game: OneHeapNimGame, pos: str):
    super().__init__(game, pos)

  def move(self) -> int:
    g = self.game
    for m in sorted(g.moves, reverse=True):
      spec = g.heap - m
      if spec >= 0 and g.win_function(spec) == "II":
        return m # send opponent to losing position (II-pos)
    return 1 # min(g.moves) - optimal while losing

class OneHeapRandomAgent(OneHeapNimAgent):
  def __init__(self, game: OneHeapNimGame, pos: str, accuracy: float):
    super().__init__(game, pos)
    self.accuracy = accuracy
    
  def move(self) -> int:
    g = self.game
    optimal = random() < self.accuracy
    if optimal:
      for m in sorted(g.moves, reverse=True):
        spec = g.heap - m
        if spec >= 0 and g.win_function(spec) == "II":
          return m # send opponent to II-pos
      return 1 # min(g.moves)
    # random if suboptimal
    return choice([x for x in g.moves if x <= g.heap])

class OneHeapCleverAgent(OneHeapNimAgent):
  def __init__(self, game: OneHeapNimGame, pos: str, accuracy: float):
    super().__init__(game, pos)
    self.accuracy = accuracy
    
  def move(self) -> int:
    g = self.game
    optimal = random() < self.accuracy
    if optimal:
      for m in sorted(g.moves, reverse=True):
        spec = g.heap - m
        if spec >= 0 and g.win_function(spec) == "II":
          return m # send opponent to II-pos
      return 1 # min(g.moves)
    # suboptimal pathway
    return (max([x for x in g.moves if x <= g.heap]) 
            if g.win_function(g.heap) == "II" else 1)