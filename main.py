import nimagent as na
from nimgame import OneHeapNimGame
import time
import wintables as wt

def test_games(rng: range, moves: set[int], player_type: str, 
               p_w: float, p_l: float, to_file=None, verbose=False):
  similarities = {0: 1.0}
  for i in rng:
    game = OneHeapNimGame(i, moves, player_type, (p_w, p_l))
    exp = game.win_function(i)
    similarities[i] = sum(game.iterate(i) == exp for _ in range(100)) / 100
    if(verbose):
      if(to_file):
        to_file.write(str(similarities[i]) + '\n')
      else:
        print(similarities[i])
  return similarities
"""
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
"""
# print(time.time())
init = start = time.time()
# test_games(range(low, upp, step), mvs, ptype, p_w, p_l, True)
with open("./write.txt", 'w') as writefile:
  for j in range(9, 2, -1):
    acc = j / 10
    for i in range(9, 2, -1):
      print(f"--{acc} vs. {i / 10}--")
      writefile.write(f"--{acc} vs. {i / 10}--\n")
      test_games(range(100, 10001, 100), {1, 3, 4}, "random", acc, i / 10, writefile, True)
      print(f"{time.time() - start} seconds")
      start = time.time()
      # writefile.write('\n'.join(map(str, list(sim.values()))))
print(f"Total: {time.time() - init} seconds")
#test_games(range(1, 101, 1), {1, 2, 3}, "random", 0.7, 0.7, verbose=True)
# test_games(range(low, upp, step), mvs, ptype, p_w, p_l, True)
# test_games(range(100, 10001, 100), {1, 2, 3}, "random", 0.5, 0.3, True)
"""
for x in range(1, 10, 1):
  moves = [1, x, x + 1, x + 2, x + 3]
  print(f"{str(moves) + ':':<12} {wt.OneHeapWinTable.win_condition(set(moves))}")
"""

#print(wt.OneHeapWinTable(20, {1, 5, 7}))