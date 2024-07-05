import nimagent as na
from nimgame import OneHeapNimGame
import time
import wintables as wt

def test_games(rng: range, moves: set[int], player_type: str, 
               p_w: float, p_l: float, verbose=False):
  similarities = {0: 1.0}
  for i in rng:
    game = OneHeapNimGame(i, moves, player_type, (p_w, p_l))
    exp = game.win_function(i)
    similarities[i] = sum(game.iterate(i) == exp for _ in range(100)) / 100
    if(verbose):
      # print(f"Size {i}: \t{similarities[i]}")
      print(similarities[i])
  return similarities

rng = list(map(int, input("Enter size bounds (inclusive) as 'lower upper step (optional)': ").split()))
step = 1 if len(rng) < 3 else rng[2]
low, upp = rng[0], rng[1] + 1
mvs = set(map(int, input("Enter all valid moves (space-separated): ").split())) | {1}
ptype = input("Enter the player type (perfect, random, or clever): ")
p_w, p_l = (0.0, 0.0)
if ptype != "perfect":
  p_w, p_l = map(float, input(
      "Enter the accuracies of the winning- and losing-position players (space-separated): "
    ).split())

start = time.time()

test_games(range(low, upp, step), mvs, ptype, p_w, p_l, True)

print(f"{time.time() - start} seconds")

"""
for x in range(1, 16, 2):
  moves = [1, x, x + 1, x + 2]
  print(f"{str(moves) + ':':<12} {wt.OneHeapWinTable.win_condition(set(moves))}")
"""