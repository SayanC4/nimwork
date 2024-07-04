import nimagent as na
from nimgame import OneHeapNimGame
#import time
import wintables as wt

#start = time.time()

def test_games(rng: range, moves: set[int], player_type: str, 
               p_w: float, p_l: float, verbose=False):
  similarities = {0: 1.0}
  for i in rng:
    game = OneHeapNimGame(i, moves, player_type, (p_w, p_l))
    exp = game.win_function(i)
    similarities[i] = sum(game.iterate(i) == exp for _ in range(100)) / 100
    if(verbose):
      print(f"Size {i}: \t{similarities[i]}")
  return similarities

# test_games(range(1, 101), {1, 2, 3}, "clever", 0.75, 0.5)

#print(f"{time.time() - start} seconds")

for x in range(1, 16, 2):
  moves = [1, x, x + 1, x + 2]
  print(f"{str(moves) + ':':<12} {wt.OneHeapWinTable.win_condition(set(moves))}")

"""
TODO:
  Make test_games() command-line based (more interface-y too)
  Get lots of data
  Make clever be clever(?)
  Come up w/own questions
    Write up coherent doc w/questions, conjectures, answers
      Try to prove conjectures
  Find various patterns
    1, x, x + 1 (proven)
      Odd:  0, 2, ... x - 1 mod 2x + 1
      Even: 0, 2, ... x - 2 mod 2x
    1, x, x + 2 (empirically)
      Odd:  0, 2, ... 2x mod 2x + 2
      Even: 0, 2, ... x - 2, x + 1, x + 3 ... 2x - 1 mod 2x + 2
    1, x, x + 3
      Odd:  0, 2, ... x + 1 mod 2x + 3
      Even: ???? mod x + 4??
    1, x, x + 4
      Odd:  0, 2, ... 2x + 2 mod 2x + 4
      Even: 0, 2, ... x - 2, x + 1, x + 3 ... 2x - 1 mod 2x + 4 - (except x = 2)
    1, x, x + a?
      a is Odd:
        Odd:  0, 2, ... x + (a - 2) mod 2x + a
        Even: ??? 
      a is Even:
        Odd:  0, 2, ... 2x + (a - 2) mod 2x + a
        Even: 0, 2, ... x - 2, x + 1, x + 3 ... 2x - 1 mod 2x + a (mostly)  
    1, x, x + 1, x + 2
      Odd:  0, 2, ... x - 1 mod 2x + 2
      Even: 0, 2, ... x - 2 mod 2x + 1
"""