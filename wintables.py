import math

class OneHeapWinTable(list):
  def __init__(self, size: int, moves: set[int] | int):
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
    if 1 not in moves:
      raise Exception("Currently, only games with 1 as a move are accepted.")
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
    table = OneHeapWinTable(2 * sum(moves), moves)
    twos = table.twostring()
    size = len(twos)
    for pd in range(size // 2,  0, -1):
      reps = (size + pd) // pd
      if (twos[:pd] * reps).startswith(twos):
        two_wins = [i for i in range(pd) if twos[i] == '2']
        def f(n: int):
          return "II" if n % pd in two_wins else "I"
        return f

def fsqrt(n: int):
  return math.floor(math.sqrt(n))

class SqrtNimWinTable(list):
  def __init__(self, size: int):
    self.size = 1
    super().__init__(["II"])
    self.expand(size)
  
  def expand(self, new: int):
    if new <= self.size + 1:
      return
    valid_moves = list(range(1, fsqrt(self.size) + 1))
    for n in range(self.size, new + 1):
      max = fsqrt(n)
      if max > valid_moves[-1]:
        valid_moves.append(max)
      seconds = filter(lambda x: x >= 0, [n - m for m in valid_moves])
      self.append("I" if any(self[s] == "II" for s in seconds) else "II")

  def __str__(self) -> str:
    rep = "  Size Winner\n"
    for n, w in enumerate(self):
      rep += f"{n:>6} {w}\n"
    return rep[:-1]

if __name__ == "__main__":
  print(SqrtNimWinTable(100))

  # TODO: 
  # CASH: Implement
  #   Amounts to a tensor win-table 