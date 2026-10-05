"""
Math for AI  |  Episode 0.5: "Slope"
"""

import matplotlib.pyplot as plt


def pause(section):
    """Wait for Enter before the next section, so each one runs only when we're ready."""
    input(f"\n--- Press Enter to run section {section} ---")


# 0. Last episode's challenge:  y = 2x + 1 goes through (1, 3) and (4, 9)
up = 9 - 3                       # how far UP:     6
across = 4 - 1                   # how far ACROSS: 3
print("up =", up, "  across =", across)
print("up / across =", up / across)     # 2.0 ... the w in y = 2x + 1!


pause(1)

# 1. Turn rise-over-run into a reusable machine:  slope(point1, point2)
def slope(p1, p2):
    x1, y1 = p1                  # unpack the first point
    x2, y2 = p2                  # unpack the second point
    rise = y2 - y1               # how far UP
    run = x2 - x1                # how far ACROSS
    if run == 0:
        return None              # run is 0: we can't divide by zero
    return rise / run


print("\n(1, 3) to (4, 9):", slope((1, 3), (4, 9)))     # 2.0
print("(4, 9) to (1, 3):", slope((4, 9), (1, 3)))       # 2.0  order doesn't matter
print("(0, 1) to (7, 15):", slope((0, 1), (7, 15)))     # 2.0  any two points on the line
print("flat:     (0, 4) to (3, 4):", slope((0, 4), (3, 4)))   # 0.0
print("downhill: (0, 7) to (2, 1):", slope((0, 7), (2, 1)))   # -3.0
print("straight up: (2, 1) to (2, 5):", slope((2, 1), (2, 5)))  # None: undefined


pause(2)

# 2. Slope is a RATE.  Our five students: points per hour.
hours = [1, 2, 3, 4, 5]          # x: hours studied
scores = [49, 56, 65, 71, 82]    # y: test scores
points = list(zip(hours, scores))    # [(1, 49), (2, 56), ...]

print("\nneighbor to neighbor:")
for i in range(len(points) - 1):
    s = slope(points[i], points[i + 1])
    print(f"   hour {hours[i]} -> {hours[i + 1]}:  {s:g} points per hour")

print("first to last:", slope(points[0], points[-1]), "points per hour")   # 33 / 4 = 8.25


pause(3)

# 3. A curve's slope keeps changing.   g(x) = x^2
def g(x):
    return x * x


print("\nhops along y = x^2, one step across each time:")
for x in [0, 1, 2, 3]:
    print(f"   x = {x} -> {x + 1}:  slope {slope((x, g(x)), (x + 1, g(x + 1))):g}")
# 1, 3, 5, 7: the climb keeps getting steeper. No single slope!


pause(4)

# 4. Slope NEAR one spot: make the run h tiny.
#        slope near x  =  ( f(x + h) - f(x) ) / h
#    This is still just rise over run. The run is h.
def slope_near(func, x, h):
    # h must never be exactly 0 (try it: Python refuses to divide by zero).
    # That's why we only SHRINK h, closer and closer to 0.
    rise = func(x + h) - func(x)
    run = h
    return rise / run


print("\nslope of y = x^2 near x = 1:")
for h in [1, 0.5, 0.1, 0.01, 0.001, 0.0001]:
    print(f"   h = {h:<7g} slope = {slope_near(g, 1, h):.4f}")
# 3, 2.1, 2.01, 2.001, 2.0001 ... settling on 2


pause(5)

# 5. The mystery from Episode 0.1, solved.
#    The error valley is a machine:  knob w in, error score out.
#    Its slope near w = 5, by rise over run, vs. Episode 0.1's steepness formula.
def error_score(w, b=40):
    total = 0
    for x, y in zip(hours, scores):
        miss = y - (w * x + b)
        total = total + miss ** 2
    return total / len(hours)


def steepness_ep01(w, b=40):
    """Episode 0.1's formula, exactly as we wrote it back then."""
    total = 0
    for x, y in zip(hours, scores):
        miss = y - (w * x + b)
        total = total + (-2 * x * miss / len(hours))
    return total


print("\nslope of the error valley near w = 5:")
for h in [1, 0.1, 0.01, 0.001]:
    print(f"   h = {h:<6g} slope = {slope_near(error_score, 5, h):.4f}")
print("Episode 0.1's steepness at w = 5:", steepness_ep01(5))   # -70.0

# Rounding dust lands a hair below zero, so round() gives -0.0.
# Adding 0.0 turns -0.0 into a plain 0.0 (a real negative number would stay negative).
print("\nat the bottom, w = 90/11:", round(steepness_ep01(90 / 11), 6) + 0.0)   # 0.0 (flat!)
print("at w = 11:", steepness_ep01(11))                                   # 62.0


pause(6)

# 6. The slope's SIGN says which way is downhill.
#        slope negative -> downhill is to the RIGHT -> make w bigger
#        slope positive -> downhill is to the LEFT  -> make w smaller
#    One gradient descent step does exactly that:  w_new = w - eta * slope
w, eta = 5, 0.02
s = steepness_ep01(w)
w_new = w - eta * s              # 5 - 0.02 * (-70) = 5 + 1.4 = 6.4
print(f"\nslope at w = {w}: {s:g}")
print(f"new w = {w} - {eta} * ({s:g}) = {w_new:g}")
print(f"error went from {error_score(w):g} to {error_score(w_new):.2f}")   # 112.4 -> 35.96


pause(7)

# 7. Reading a loss curve with slope.
#    Train for 15 steps (Episode 0.1's loop), then measure the slope
#    between neighboring points on the loss curve.
w = 5
errors = [error_score(w)]
for step in range(15):
    w = w - eta * steepness_ep01(w)
    errors.append(error_score(w))

print("\nloss-curve slope, step by step:")
for step in range(len(errors) - 1):
    print(f"   step {step:2} -> {step + 1:2}:  {slope((step, errors[step]), (step + 1, errors[step + 1])):10.5f}")
# Big negative numbers at first (learning fast), then almost 0 (done learning).

# Same look as the slides: the series blue, and big text so it reads on a phone.
plt.rcParams.update({"font.size": 18, "axes.titlesize": 22, "axes.labelsize": 22})
plt.figure(figsize=(12.8, 7.2))
plt.plot(range(len(errors)), errors, marker="o", markersize=9, linewidth=4, color="#1f5fbf")
plt.title("The loss curve: steep early, flat late")
plt.xlabel("training step")
plt.ylabel("error score")
plt.grid(alpha=0.3)
plt.show()
