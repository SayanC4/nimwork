from nimgame import OneHeapNimGame, OneHeapCashGame
from random import choice, random

class OneHeapNimAgent:
  def __init__(self, game: OneHeapNimGame, pos: str):
    self.game = game
    self.pos = pos

  def move(self) -> int:
    return 0
  
class OneHeapCashAgent:
  def __init__(self, game: OneHeapCashGame, pos: str):
    self.game = game
    self.pos = pos
  
  def move(self, vals: tuple[int, int, int], 
           pos: str) -> tuple[int, int, int]:
    return (0, 0, 0)
  
  def index_table(self, vals: tuple[int, int, int], move: int):
    d, e, n = vals
    print(f"{d - move}, {e - move}")
    if self.pos == "I":
      return self.game.win_table.outcome(e, d - move, n - move)
    else:
      return self.game.win_table.outcome(d, e - move, n - move)

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

class PerfectCashAgent(OneHeapCashAgent):
  def __init__(self, game: OneHeapCashGame, pos: str):
    super().__init__(game, pos)

  def move(self, vals: tuple[int, int, int], 
           pos: str) -> tuple[int, int, int]:
    d, e, n = vals
    bal = d if pos == "I" else e
    g = self.game
    for m in sorted(g.moves, reverse=True):
      spec_heap = n - m
      spec_cash = bal - m
      if(spec_heap >= 0 and spec_cash >= 0 and 
         self.index_table(vals, m) == "II"):
        return ((spec_heap, e, spec_cash) if pos == "I" 
                else (e, spec_heap, spec_cash)) # send opponent to losing position (II-pos)
    return (d - 1, e, n - 1) if pos == "I" else (d, e - 1, n - 1) # min(g.moves)

class RandomCashAgent(OneHeapNimAgent):
  def __init__(self, game: OneHeapNimGame, pos: str, accuracy: float):
    super().__init__(game, pos)
    self.accuracy = accuracy
    
  def move(self, vals: tuple[int, int, int], 
           pos: str) -> tuple[int, int, int]:
    d, e, n = vals
    bal = d if pos == "I" else e
    g = self.game
    optimal = random() < self.accuracy
    if optimal:
      for m in sorted(g.moves, reverse=True):
        spec_heap = n - m
        spec_cash = bal - m
        if(spec_heap >= 0 and spec_cash >= 0 and 
          self.index_table(vals, m) == "II"):
          return ((spec_heap, e, spec_cash) if pos == "I" 
                  else (e, spec_heap, spec_cash)) # send opponent to losing position (II-pos)
      return (d - 1, e, n - 1) if pos == "I" else (d, e - 1, n - 1) # min(g.moves)
    # random if suboptimal
    m = choice([x for x in g.moves if x <= n and x <= bal])
    return (d - m, e, n - m) if pos == "I" else (d, e - m, n - m)

class CleverCashAgent(OneHeapNimAgent):
  def __init__(self, game: OneHeapNimGame, pos: str, accuracy: float):
    super().__init__(game, pos)
    self.accuracy = accuracy
    
  def move(self, vals: tuple[int, int, int], 
           pos: str) -> tuple[int, int, int]:
    d, e, n = vals
    bal = d if pos == "I" else e
    g = self.game
    optimal = random() < self.accuracy
    if optimal:
      for m in sorted(g.moves, reverse=True):
        spec_heap = n - m
        spec_cash = bal - m
        if(spec_heap >= 0 and spec_cash >= 0 and 
          self.index_table(vals, m) == "II"):
          return ((spec_heap, e, spec_cash) if pos == "I" 
                  else (e, spec_heap, spec_cash)) # send opponent to losing position (II-pos)
      return (d - 1, e, n - 1) if pos == "I" else (d, e - 1, n - 1) # min(g.moves)
    # suboptimal pathway
    m = max([x for x in g.moves if x <= n and x <= bal])
    return (d - m, e, n - m) if pos == "I" else (d, e - m, n - m)