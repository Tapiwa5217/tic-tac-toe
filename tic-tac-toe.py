B = {1,2,3,4,5,6,7,8,9} # set of positions on the board

W = {{1,2,3},{4,5,6},{7,8,9},{1,5,9},{3,5,7},{1,4,7},{2,5,8},{3,6,9}} # set of winning moves

Mx = {} # moves by player X. initialized to empty set
Mo = {} # moves by player O. initialized to empty set

# if Mx ∪ Mo is not equal to B, then keep playing
# p = Mx ∪ Mo is equal to B
# q = keep playing
# ¬p → q  

# if |Mx| is equal to |Mo|, then let player X play, otherwise let player O play.
# Mc = current move

# if Mx ∪ Mo ⊆ B and Mx ∩ Mo = ∅, then the move is acceptable
# if |Mx| + |Mo| < 3, then skip to next move

# if ∃w ∈ W such that w ⊆ Mx, then player X wins 
# if ∃w ∈ W such that w ⊆ Mo, then player O wins

# if Mx ∪ Mo = B and ∀w ∈ W, w ⊈ Mx and w ⊈ Mo, then the game is a draw