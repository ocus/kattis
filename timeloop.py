import fileinput

inp = "".join([l for l in fileinput.input()]).strip()
for n in range(1, int(inp) + 1):
    print("{} Abracadabra".format(n))
