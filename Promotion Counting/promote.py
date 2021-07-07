with open("promote.in") as promotion_input:
    DIVISIONS = [list(map(int, division.split())) for division in promotion_input][1:]
    DIVISIONS = [after-before for before, after in DIVISIONS]
    DIVISIONS = [str(sum(DIVISIONS[rank:])) for rank in range(3)]

with open("promote.out", "w") as promotion_output:
    promotion_output.write("\n".join(DIVISIONS))
