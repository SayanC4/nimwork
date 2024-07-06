# TODO:
- **Next meeting:** 7/5 @8PM 
- Make test_games() command-line based (more interface-y too)
- Get lots of data
- Fix min/max move shenanigans (done)
- Come up w/own questions
  - Write up coherent doc w/questions, conjectures, answers
    - Try to prove conjectures
- Find various patterns ("done")
  - 1, x, x + 1 (proven)
    - Odd:  0, 2, ... x - 1 mod 2x + 1
    - Even: 0, 2, ... x - 2 mod 2x
  - 1, x, x + 2
    - Odd:  0, 2, ... 2x mod 2x + 2
    - Even: 0, 2, ... x - 2, x + 1, x + 3 ... 2x - 1 mod 2x + 2
  - 1, x, x + 3
    - Odd:  0, 2, ... x + 1 mod 2x + 3
    - Even: ???? mod x + 4??
  - 1, x, x + 4
    - Odd:  0, 2, ... 2x + 2 mod 2x + 4
    - Even: 0, 2, ... x - 2, x + 1, x + 3 ... 2x - 1 mod 2x + 4 - (except x = 2)
  - 1, x, x + a?
    - a is Odd:
      - Odd:  n ≡ {0, 2, ... x + (a − 2)} (mod 2x + a)
      - Even: ??? 
    - a is Even:
      - Odd:  0, 2, ... 2x + (a - 2) mod 2x + a
      - Even: 0, 2, ... x - 2, x + 1, x + 3 ... 2x - 1 mod 2x + a (mostly)  
  - 1, x, x + 1, x + 2 (empirically)
    - Odd:  0, 2, ... x - 1 mod 2x + 2
    - Even: 0, 2, ... x - 2 mod 2x + 1
      
    
      If x is odd, then Player 2 wins the Base 3 game of NIM with n objects iff:
        n ≡ {0, 2, ... x − 2} (mod 2x + 1)
      If x is even, then Player 2 wins the Base 3 game of NIM with n objects iff:
        n ≡ {0, 2, ... x − 2} (mod 2x)

      If x is odd, then Player 2 wins the Base 4 game of NIM with n objects iff:
        n ≡ {0, 2, ... x − 1} (mod 2x + 2)
      If x is even, then Player 2 wins the Base 4 game of NIM with n objects iff:
        n ≡ {0, 2, ... x − 2} (mod 2x + 1)
      
      If x is odd, then Player 2 wins the Base 5 game of NIM with n objects iff:
        n ≡ {0, 2, ... x − 1} (mod 2x + 3)
      If x is even, then Player 2 wins the Base 5 game of NIM with n objects iff:
        n ≡ {0, 2, ... x − 2} (mod 2x + 2)
      
      If x is odd, then Player 2 wins the Base a game of NIM with n objects iff:
        n ≡ {0, 2, ... x − 1} (mod 2x + i - 2)
      If x is even, then Player 2 wins the Base a game of NIM with n objects iff:
        n ≡ {0, 2, ... x - 2} (mod 2x + i - 3)
      (based only on the above empirically verified rules)


  - More TODOS:
    - Potentially try to prove (by induction) Base 4
    - Alt games:
      - n pieces on board: move 1, 2, ... floor(sqrt(n))
      - Nim with cash?