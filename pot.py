import fileinput

print(sum([pow(int(n[:-1]), int(n[-1])) for n in [l.strip() for l in fileinput.input()][1:]]))
