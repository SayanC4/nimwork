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
    self.wintable = wt.OneHeapWinTable(heap, moves)
    accs = (accuracies if self.wintable[self.heap] == "I" 
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