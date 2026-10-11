"""
Math for AI  |  Episode 0.6: "Exponents and Logarithms"
"""

import math                      # ONLY used to double-check our home-made log
import matplotlib.pyplot as plt


def pause(section):
    """Wait for Enter before the next section, so each one runs only when we're ready."""
    input(f"\n--- Press Enter to run section {section} ---")


# 0. Last episode's challenge: paper is 0.1 mm thick, and each fold doubles it.
thickness = 0.1                  # millimeters
for fold in range(10):
    thickness = thickness * 2    # one fold = double it
print("after 10 folds:", thickness, "mm")          # 102.4 mm, about 10 cm

# Bonus: keep folding until it's MORE than 1 meter (1000 mm). Count the folds.
thickness = 0.1
folds = 0
while thickness <= 1000:
    thickness = thickness * 2
    folds = folds + 1
print("folds to pass 1 meter:", folds, "thickness then:", thickness, "mm")   # 14, 1638.4


pause(1)

# 1. Exponents in Python:  **  means "to the power of"
print("\n2 ** 10 =", 2 ** 10)    # 1024: ten 2's multiplied together
print("2 ^ 10  =", 2 ^ 10)       # 8 !!  In Python, ^ is NOT power. It's a bit trick (XOR).
                                 #       Always use ** for powers.

# The three rules, checked by Python
print("\n2**3 * 2**4  =", 2 ** 3 * 2 ** 4, "   2**7 =", 2 ** 7)      # add the exponents
print("(2**3) ** 2  =", (2 ** 3) ** 2, "    2**6 =", 2 ** 6)        # multiply the exponents
print("2**5 / 2**2  =", 2 ** 5 / 2 ** 2, "   2**3 =", 2 ** 3)       # subtract the exponents

# Zero, negative, and fraction exponents
print("\n2 ** 0    =", 2 ** 0)   # 1
print("2 ** -1   =", 2 ** -1)    # 0.5   (one half)
print("2 ** -2   =", 2 ** -2)    # 0.25  (one quarter)
print("2 ** 0.5  =", 2 ** 0.5)   # 1.414...  (the square root of 2)


pause(2)

# 2. Three kinds of growth:  adding (2*x),  squaring (x**2),  doubling (2**x)
print("\n  x    2x  x**2   2**x")
for x in range(11):
    print(f"{x:3} {2 * x:5} {x ** 2:5} {2 ** x:6}")
# By x = 10:  20,  100,  1024.  Doubling leaves everything else behind.


pause(3)

# 3. The logarithm: the question asked backwards.  "2 to WHAT power gives y?"
def count_doublings(y):
    """The whole-number answer: how many times can we double 1 and stay at or below y? (for y >= 1)"""
    count = 0
    size = 1
    while size * 2 <= y:
        size = size * 2
        count = count + 1
    return count


def log2(y):
    """
    The exact answer, from scratch: find x so that 2 ** x == y.
    Guess and check, then halve the window (bisection), 60 times.
    """
    if y <= 0:
        return None              # no power of 2 is ever 0 or negative
    low, high = -1.0, 1.0
    while high < 1024 and 2 ** high < y:   # widen the window until the answer is inside it
        high = high * 2                      # (stop at 1024: 2.0 ** 1024 is too big for a Python decimal)
    while 2 ** low > y:
        low = low * 2
    if 2 ** low == y:
        return low               # the edge of the window was already the answer (like y = 0.5 or 0.25)
    for _ in range(60):
        middle = (low + high) / 2
        if 2 ** middle == y:
            return middle        # a lucky exact hit: stop right here
        if 2 ** middle < y:
            low = middle         # too small: the answer is to the right
        else:
            high = middle        # too big: the answer is to the left
    return (low + high) / 2


print("\nlog2(8)    =", log2(8))           # 3, because 2**3 = 8
print("log2(1024) =", log2(1024))         # 10
print("log2(1)    =", log2(1))            # 0, because 2**0 = 1
print("log2(0.25) =", log2(0.25))         # -2, because 2**-2 = 1/4
print("log2(0)    =", log2(0))            # None: no answer

# Back to the paper:  0.1 * 2**n > 1000   means   2**n > 10000
print("\nwhole doublings that fit in 10000:", count_doublings(10000))   # 13 (8192)
print("log2(10000) =", log2(10000))                                    # 13.2877...
print("Python's math.log2 agrees:", math.log2(10000))                  # agrees to about 15 digits
# 13 folds isn't enough, and you can't do 0.29 of a fold, so the answer is 14.


pause(4)

# 4. The superpower: logs turn MULTIPLYING into ADDING
print("\nlog2(8 * 32)          =", log2(8 * 32))           # log2(256) = 8
print("log2(8) + log2(32)    =", log2(8) + log2(32))       # 3 + 5 = 8
print("log2(8 ** 5)          =", log2(8 ** 5))             # 15
print("5 * log2(8)           =", 5 * log2(8))              # 15


pause(5)

# 5. Why AI needs that superpower: tiny probabilities.
#    A language model gives each word a probability, and the chance of a whole
#    passage is all of them MULTIPLIED. Say 400 words, each with chance 0.1:
chance = 1.0
for word in range(400):
    chance = chance * 0.1
print("\nmultiply 400 chances of 0.1:", chance)     # 0.0 !  Too small for the computer to store.

def log10(y):
    """
    Log base 10, built from our own log2 with the "change of base" trick:
        log10(y) = log2(y) / log2(10)
    Switching bases just divides by a fixed number (log2(10) is about 3.32).
    """
    if y <= 0:
        return None              # no log for 0 or negatives, same as log2
    return log2(y) / log2(10)


total = 0.0
for word in range(400):
    total = total + log10(0.1)                    # ADD the logs instead: each one is -1
                                                  # (Python may show -0.9999999999999999: tiny rounding)
print("add 400 logs (base 10):", round(total, 6))  # -400: the answer is 10 ** -400


pause(6)

# 6. Log-loss: how AI scores a guess.
#    p = the chance the model gave to the RIGHT answer.   penalty = -log2(p)
print("\n     p      penalty")
for p in [1, 1 / 2, 1 / 4, 1 / 8, 1 / 16, 0.01]:
    print(f"{p:8.4f}   {-log2(p) + 0.0:7.3f}")      # + 0.0 turns -0.0 into 0.0
# Every time p is cut in half, the penalty goes up by exactly 1.


pause(7)

# 7. Our own training (Episode 0.1) was SHRINKING EXPONENTIALLY all along.
#    gap = error score minus the lowest possible error score
hours = [1, 2, 3, 4, 5]
scores = [49, 56, 65, 71, 82]


def error_score(w, b=40):
    total = 0
    for x, y in zip(hours, scores):
        miss = y - (w * x + b)
        total = total + miss ** 2
    return total / len(hours)


def valley_slope(w, b=40):
    """Episode 0.1's steepness = Episode 0.5's slope of the error valley."""
    total = 0
    for x, y in zip(hours, scores):
        miss = y - (w * x + b)
        total = total + (-2 * x * miss / len(hours))
    return total


lowest = error_score(90 / 11)                     # the bottom of the valley (Episode 0.4)
w, eta = 5, 0.02
gaps = [error_score(w) - lowest]
for step in range(15):
    w = w - eta * valley_slope(w)
    gaps.append(error_score(w) - lowest)

print("\nstep        gap     gap / previous gap")
for step in range(len(gaps)):
    ratio = "" if step == 0 else f"{gaps[step] / gaps[step - 1]:.4f}"
    print(f"{step:4} {gaps[step]:12.6f}   {ratio}")
# Every step multiplies the gap by 0.3136. Multiply by the same number again and again:
# that's an exponent!   gap after k steps = 111.36 * 0.3136 ** k

# Same look as the slides: the series blue, and big text so it reads on a phone.
plt.rcParams.update({"font.size": 18, "axes.titlesize": 22, "axes.labelsize": 22})
plt.figure(figsize=(12.8, 7.2))
plt.plot(range(len(gaps)), gaps, marker="o", markersize=9, linewidth=4, color="#1f5fbf")
plt.yscale("log")                # drawing only: space the up-axis like a log ruler
plt.yticks([100, 1, 0.01, 0.0001, 0.000001], ["100", "1", "0.01", "0.0001", "0.000001"])
plt.minorticks_off()             # same tick labels as the slide
plt.xticks(range(0, 16, 3))
plt.title("The gap on a log axis: a straight line")
plt.xlabel("training step")
plt.ylabel("gap above the bottom")
plt.grid(alpha=0.3)
plt.show()

