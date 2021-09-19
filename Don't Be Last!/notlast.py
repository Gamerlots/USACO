with open("notlast.in") as notlast:
    notlast.readline()

    amounts = {}
    for data in notlast:
        name, amount = data.split()
        if name in amounts:
            amounts[name] += int(amount)
        else:
            amounts[name] = int(amount)

minimum = min(amounts.values())

for name in amounts.copy():
    if amounts[name] == minimum:
        amounts.pop(name)

minimum = min(amounts.values())

for name in amounts.copy():
    if amounts[name] == minimum:
        with open("notlast.out", "w") as notlast:
            print(name, file=notlast)
