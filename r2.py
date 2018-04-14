import fileinput

(r1, s) = map(int, "".join([l for l in fileinput.input()]).strip().split(" "))
print((s * 2) - r1)