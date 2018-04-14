import fileinput

(x, y) = map(int, [l for l in fileinput.input()])
print(((1, 4), (2, 3))[0 if x > 0 else 1][0 if y > 0 else 1])
