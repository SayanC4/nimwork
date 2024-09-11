import math
import time

class OneHeapWinTable(list):
  def __init__(self, size: int, moves: set[int] | int = 3): # {1, 2, 3}
    self.size = size
    self.valid_moves = (range(1, moves + 1)
      if isinstance(moves, int) else list(moves))
    super().__init__(["II"])
    for n in range(1, size + 1):
      seconds = filter(lambda x: x >= 0, [n - m for m in self.valid_moves])
      self.append("I" if any(self[s] == "II" for s in seconds) else "II")

  def __str__(self) -> str:
    rep = "  Size Winner\n"
    for n, w in enumerate(self):
      rep += f"{n:>6} {w}\n"
    return rep[:-1]

  def expand(self, new: int):
    if new <= self.size + 1:
      return
    for n in range(self.size, new + 1):
      seconds = filter(lambda x: x >= 0, [n - m for m in self.valid_moves])
      self.append("I" if any(self[s] == "II" for s in seconds) else "II")
    self.size = new

  def outcome(self, n: int) -> str:
    if n >= self.size:
      self.expand(n)
    return self[n]

  def twostring(self) -> str:
    ret = ""
    for g in self:
      ret += '2' if g == "II" else '1'
    return ret

  @staticmethod
  def win_condition(moves: set[int]) -> str:
    if 0 in moves:
      raise Exception("0 cannot be a move.")
    if 1 not in moves:
      raise Exception("Only games with 1 as a move are accepted.")
    table = OneHeapWinTable(2 * sum(moves), moves)
    twos = table.twostring()
    size = len(twos)
    for pd in range(size // 2,  0, -1):
      reps = (size + pd) // pd
      if (twos[:pd] * reps).startswith(twos):
        two_wins = [i for i in range(pd) if twos[i] == '2']
        return f"n = {two_wins} (mod {pd}) -> II wins, else I"
    return "No condition interpretable."
  
  @staticmethod
  def win_function(moves: set[int]):
    if 1 not in moves:
      raise Exception("Currently, only games with 1 as a move are accepted.")
    bound = max(moves) * 2 ** (max(moves) + 1) # m2^(m+1)
    twos = OneHeapWinTable(bound, moves).twostring()
    size = len(twos)
    for pd in range(1, 1 + size // 2):
      reps = (size + pd) // pd
      if (twos[:pd] * reps).startswith(twos):
        two_wins = {i for i in range(pd) if twos[i] == '2'}
        return lambda n: "II" if n % pd in two_wins else "I"

class FNimWinTable(list):
  def __init__(self, size: int, f):
    self.size = 1
    self.func = f
    self.two_cml = [0] # [1]
    super().__init__(["II"])
    self.expand(size)

  @staticmethod
  def fsqrt(n: int):
    return math.floor(math.sqrt(n))
  
  def expand(self, new: int):
    if new <= self.size + 1:
      return
    remake = False
    valid_moves = list(range(1, self.func(self.size) + 1))
    for n in range(self.size, new + 1):
      if(remake):
        valid_moves = list(range(1, self.func(n) + 1))
        remake = False
      if not valid_moves:
        self.append("II")
        remake = True
      else:
        max = self.func(n)
        if max > valid_moves[-1]:
          valid_moves.append(max)
        seconds = filter(lambda x: x >= 0, [n - m for m in valid_moves])
        self.append("I" if any(self[s] == "II" for s in seconds) else "II")
      self.two_cml.append(self.two_cml[-1])
      if self[-1] == "II":
        self.two_cml[-1] += 1
      # print(valid_moves)

  def __str__(self) -> str:
    rep = "  Size Winner\n"
    for n, w in enumerate(self):
      rep += f"{n:>6} {w}\n"
    return rep[:-1]


class OneHeapCashTable():
  def __init__(self, moves: set[int] = {1, 2, 3}, 
               dims: tuple[int, int, int] = (0, 0, 0)): # (d, e, n)
    if 0 in moves:
      raise Exception("0 cannot be a move.")
    if 1 not in moves:
      raise Exception("Only games with 1 as a move are accepted.")
    one, two, size = dims
    self.arr = [[
      ['' for _ in range(size)] # innermost: heap size
      for _ in range(two)]      # intermediate: P2 dollars
      for _ in range(one)]      # outermost: P1 dollars
    for d in range(one):
      for e in range(two):
        for n in range(size):
          if not self.arr[d][e][n]:
            if d < 1 or n < 1:
              self.arr[d][e][n] = "II"
            else:
              valid_moves = [m for m in moves if m <= d and m <= n]
              # if can take and win even if it would bankrupt, "m <= d" else "m < d"
              if any(self.arr[e][d - v][n - v] == "II" for v in valid_moves):
                self.arr[d][e][n] = "I"
                if all(self.arr[e][d - v][n - v] == '' for v in valid_moves):
                  raise Exception(f"{d}{e}{n}: all sources undefined")
              else:
                self.arr[d][e][n] = "II"
    self.moves = moves
    self.dims = dims
  
  def __str__(self):
    return ""

  def outcome(self, d: int, e: int, n: int) -> str:
    assert([d, e, n][i] <= self.dims[i] for i in range(3))
    return self.arr[d][e][n]

if __name__ == "__main__":
  upp = int(input("Enter heap size upper limit: "))
  toggle = input("[log]arithmic or [exp]onential: ")
  if toggle == "log":
    a = float(input("Enter the base of the log; enter anything <= 1 for e: "))
    if a <= 1:
      a = math.e
    rnd = math.ceil
    inn = math.log
    print(f"f(n) = ⌈log base {'e' if a == math.e else a} (n)⌉")
  elif toggle == "exp":
    a = float(input("Enter the power of x, less than 1: "))
    rnd = math.floor
    inn = math.pow
    print(f"f(n) = ⌊n ^ {a}⌋") 
  table = FNimWinTable(upp, lambda x: rnd(inn(x, a)))
  twos = []
  for i, win in enumerate(table[1:]):
    if win == "II":
      twos.append(i + 1)
  print(f"Player II wins for heap sizes of: {str(twos)[1:-1]}")
  # print(table)
  """
  moves = set([int(x) for x in input("Enter moves (space-separated): ").split()])
  dims = (
    int(input("Player 1's cash: ")) + 1, 
    int(input("Player 2's cash: ")) + 1, 
    int(input("Heap size: ")) + 1
  )
  #start = time.time()
  table = OneHeapCashTable(moves, dims)
  dims = (x - 1 for x in dims)
  print(f"Winner: Player {table.outcome(*dims)}")
  #print(time.time() - start)
  #print(table.arr)
  """
