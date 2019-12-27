from boss import sol

pairs = [(3,5), (5,6), (5,2), (2,7), (2,4), (3,1), (1,0), (1,8)]
print(sol(pairs, 5, 1), "Expected: ", 3)
print(sol(pairs, 5, 4), "Expected: ", 5)