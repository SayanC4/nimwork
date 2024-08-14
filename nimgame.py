import nimagent as na
import wintables as wt

class OneHeapNimGame:
  def __init__(self, heap: int, moves: set[int] | int, player_type: str,
               accuracies: tuple[float, float]=(
                 0.0,   # winning pos. agent's accuracy
                 0.0)): # losing pos. agent's accuracy
    self.heap = heap
    self.moves = set(range(1, moves + 1) # n -> 1, 2, ... n
                      if isinstance(moves, int) else moves)
    self.win_function = wt.OneHeapWinTable.win_function(moves)
    accs = (accuracies if self.win_function(self.heap) == "I" 
            else (accuracies[1], accuracies[0]))
    match player_type:
      case "perfect":
        self.one = na.OneHeapPerfectAgent(self, "I")
        self.two = na.OneHeapPerfectAgent(self, "II")
      case "clever":
        self.one = na.OneHeapCleverAgent(self, "I", accs[0])
        self.two = na.OneHeapCleverAgent(self, "II", accs[1])
      case "random":
        self.one = na.OneHeapRandomAgent(self, "I", accs[0])
        self.two = na.OneHeapRandomAgent(self, "II", accs[1])
      case _:
        raise Exception(f"Invalid player type: {type}")
    self.turn = "I"
    self.terminal = not(heap > 0)
  
  def iterate(self, size: int | None=None):
    start = self.heap
    outcome = self.play()
    self.heap = size if size else start
    self.terminal = not(self.heap > 0)
    self.turn = "I"
    return outcome
  
  def play(self, verbose=False):
    curr: na.OneHeapNimAgent
    if verbose:
      print(f"{self.__repr__()} (Initial)")
    if self.terminal:
      self.turn = "II"
    while not self.terminal:
      curr = self.one if self.turn == "I" else self.two
      self.heap -= curr.move()
      if verbose:
        print(f" ↳ {self.__repr__()}")
      self.advance()
    return self.turn # returns winning player
  
  def advance(self):
    if self.heap == 0:
      self.terminal = True
    else:
      self.turn = "II" if self.turn == "I" else "I"
  
  def __repr__(self):
    return f"{self.heap} | Player {self.turn}"

class OneHeapCashGame:
  def __init__(self, dims: tuple[int, int, int], moves: set[int],
               player_type: str, accuracies: tuple[float, float] = (0.0, 0.0)):
    self.vals = dims
    self.moves = moves
    self.win_table = wt.OneHeapCashTable(moves, (x + 1 for x in dims))
    accs = (accuracies if self.win_table.outcome(*dims) == "I" 
            else (accuracies[1], accuracies[0]))
    match player_type:
      case "perfect":
        self.one = na.PerfectCashAgent(self, "I")
        self.two = na.PerfectCashAgent(self, "II")
      case "clever":
        self.one = na.CleverCashAgent(self, "I", accs[0])
        self.two = na.CleverCashAgent(self, "II", accs[1])
      case "random":
        self.one = na.RandomCashAgent(self, "I", accs[0])
        self.two = na.RandomCashAgent(self, "II", accs[1])
      case _:
        raise Exception(f"Invalid player type: {type}")
    self.turn = "I"
    self.terminal = any(d <= 0 for d in dims)
  
  def play(self):
    curr: na.OneHeapCashAgent
    if self.terminal:
      self.turn = "II"
    while not self.terminal:
      curr = self.one if self.turn == "I" else self.two
      self.vals = curr.move(self.vals, self.turn)
      self.advance()
    return self.turn # returns winning player
  
  def advance(self):
    if any(v <= 0 for v in self.vals):
      self.terminal = True
    else:
      #print(f"unterminated {self.vals}")
      self.turn = "II" if self.turn == "I" else "I"

if __name__ == "__main__":
  game = OneHeapCashGame((4, 4, 14), {1, 3, 4}, "perfect")
  print(game.play()) # II