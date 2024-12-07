B = {1,2,3,4,5,6,7,8,9} # set of positions on the board

W = {{1,2,3},{4,5,6},{7,8,9},{1,5,9},{3,5,7},{1,4,7},{2,5,8},{3,6,9}} # set of winning moves

Mx = {} # moves by player X. initialized to empty set
Mo = {} # moves by player O. initialized to empty set

# if (Mx ∪ Mo) is not equal to B, then keep playing

# p: (Mx ∪ Mo) is equal to B
# q: keep playing

# Rule: ¬p → q

# if |Mx| is equal to |Mo|, then player X plays, otherwise player O plays.

# r: ∣Mx∣ is equal to ∣Mo∣
# s: Player X plays
# t: Player O plays

# Rules:  r → s
#        ¬r → t

# if and only if (Mx ∪ Mo ⊆ B) ∧ (Mx ∩ Mo = ∅), the move is acceptable

# u: (Mx ∪ Mo ⊆ B) ∧ (Mx ∩ Mo = ∅)
# v: The move is acceptable

# Rule: u ↔ v

# if |Mx| < 3, then skip to next move

# if ∃w ∈ W such that w ⊆ Mx, then player X wins 
# if ∃w ∈ W such that w ⊆ Mo, then player O wins

# p: ∃w ∈ W such that w ⊆ Mx
# q: ∃w ∈ W such that w ⊆ Mo
# r: player X wins
# s: then player O wins

# According to modus ponens:
# p
# p → q
# -----
# ∴ q

# According to modus ponens:
# r
# r → s
# -----
# ∴ s

# if Mx ∪ Mo = B and ∀w ∈ W, w ⊈ (Mx ∪ Mo), then the game is a draw.

# t: Mx ∪ Mo = B
# u: ∀w ∈ W, w ⊆ (Mx ∪ Mo)
# v: the game is a draw

# t ∧ u → v 