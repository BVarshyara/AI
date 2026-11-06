from itertools import product
print("P\tQ\tR\tP->Q\tQ->R\tKB")
for P, Q, R in product([True, False], repeat=3):
    rule1 = (not P) or Q
    rule2 = (not Q) or R
    KB = rule1 and rule2 and P
    print(
        P, Q, R,
        rule1, rule2, KB,
        sep="\t"
    )
