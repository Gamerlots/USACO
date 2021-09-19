# Defines a function to simulate the chain reaction.
def chain_reaction(exploded, number_line, radius=0):
    # Find the numbers which got exploded.
    exploded = {*range(min(exploded)-radius, max(exploded)+radius+1)} & number_line
    # Explode the hay bales if a hay bale got exploded. Otherwise, print the number of hay bales that exploded.
    return chain_reaction(exploded, number_line-exploded, radius+1) if exploded else LENGTH - len(number_line)


# Opens the input file.
with open("angry.in") as angry:
    # Extracts the number of numbers.
    LENGTH = int(angry.readline())
    # Extracts the number line.
    NUMBERS = {int(line) for line in angry}

# Opens the output file.
with open("angry.out", "w") as angry:
    # Prints the maximum number of hay bales you can explode to the output file.
    print(max(chain_reaction([number], NUMBERS) for number in NUMBERS), end="", file=angry)
