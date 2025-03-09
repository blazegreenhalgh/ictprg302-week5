tic_tac = ("- X O\n" +
           "X - X\n" +
           "O - O\n")

# what is the length of the string?
# insert code here

# make the following print True by substituting
# each `?` with a **different** value
# NOTE: **all** you need to do is substitute the `?` with integers!
print(tic_tac[0] ==
      tic_tac[?] ==
tic_tac[?])  # True

print(tic_tac[2] ==
      tic_tac[?] ==
tic_tac[?])  # True

print(tic_tac[5] ==
      tic_tac[?] ==
tic_tac[?])  # True

# combine two slices of the original string
# for X to win the game:
print(tic_tac[?:?] + 'X' + tic_tac[?:?])

# combine two slices of the original string
# for O to win the game:
print(tic_tac[?:?] + 'O' + tic_tac[?:?])

# Bonus question, complete the following to print 'XXX': print(tic_tac[?:?:?])
#