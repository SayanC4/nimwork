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

test_games(range(1, 101), {1, 2, 3}, "clever", 0.75, 0.5)

#print(f"{time.time() - start} seconds")

"""
TODO:
  Make test_games() command-line based (more interface-y too)
  Get lots of data
  Make clever be clever(?)
  Come up w/own questions
    Write up coherent doc w/questions, conjectures, answers
      Try to prove conjectures
  Find various patterns
"""