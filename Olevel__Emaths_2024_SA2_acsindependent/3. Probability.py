import math
from fractions import Fraction


def solve_dice_game(question):
    # (a) Construct the possibility diagram (36 outcomes) [cite: 30]
    outcomes = []
    scores_frequency = {}

    for die1 in range(1, 7):
        row = []
        for die2 in range(1, 7):
            # Rule: subtract lower from higher, or 0 if same [cite: 28, 29]
            score = abs(die1 - die2)
            row.append(score)
            
            scores_frequency[score] = scores_frequency.get(score, 0) + 1
        outcomes.append(row)

    # --- Printing with Headers ---
    # Print the top header row (n2)
    print(question)
    print("  n2: 1  2  3  4  5  6")
    print("n1: ")

    # Print each row with the left column header (n1)
    for i, row in enumerate(outcomes):
        # i + 1 represents the current face of die1 (n1)
        row_string = "  ".join(map(str, row))
        print(f" {i+1} | [{row_string}]")

solve_dice_game("3a. Diagram all possible outcome")


n1 = 6
n2 = 6
n_s = n1*n2
print(n_s)

n_e = 2
p1 = Fraction(n_e,n_s)
p2 = n_e/n_s
print(p1)
print(p2)
print(f"3b. Probability = {p1} = {p2}")