"""
Math for AI  |  Episode 0.1: the whole learning loop, from scratch
"""

hours  = [1, 2, 3, 4, 5]          # x: hours each student studied
scores = [49, 56, 65, 71, 82]     # y: the score each student earned
w, b, eta = 5, 40, 0.02           # first guess, fixed start, step size

for step in range(6):
    # 1) Measure the steepness of the error valley where we stand
    steepness = 0
    for x, y in zip(hours, scores):
        miss = y - (w * x + b)                    # one student's miss: real score - predicted score
        steepness += -2 * x * miss / len(hours)   # this student's share of the steepness

    # 2) Take a small step downhill (against the steepness)
    w = w - eta * steepness        # roll downhill
    print(step + 1, round(w, 3))

# Expected output:
# 1 6.4
# 2 7.184
# 3 7.623
# 4 7.869
# 5 8.007
# 6 8.084
