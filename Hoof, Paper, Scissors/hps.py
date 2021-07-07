with open("hps.in") as hps:
    hps.readline()
    games = [tuple(map(int, line.split())) for line in hps]

combinations = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

with open("hps.out", "w") as hps:
    print(max(len([0 for game in games if game in {(hoof, scissors), (paper, hoof), (scissors, paper)}])
              for hoof, paper, scissors in combinations), file=hps)
