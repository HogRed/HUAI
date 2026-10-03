"""
Math for AI  |  Episode 0.4: "Graphing Functions"
"""

import matplotlib.pyplot as plt


def pause(section):
    """Wait for Enter before the next section, so each one runs only when we're ready."""
    input(f"\n--- Press Enter to run section {section} ---")


# 0. Last episode's challenge:  g(x) = x^2  at  x = -2, -1, 0, 1, 2
def g(x):
    """Square it."""
    return x * x


print("x | g(x)")
print("--+-----")
for x in [-2, -1, 0, 1, 2]:
    print(x, "|", g(x))          # 4, 1, 0, 1, 4: down, then back up. A U shape!


pause(1)

# 1. Turn the table into dots.
#    Build two lists side by side: the inputs (across) and the outputs (up).
xs = [-2, -1, 0, 1, 2]
ys = []                          # start with an empty list of outputs
for x in xs:
    ys.append(g(x))              # run each input through the machine, keep the answer
print("\nxs =", xs)
print("ys =", ys)

plt.scatter(xs, ys, s=120)       # one dot per pair:  (xs[0], ys[0]), (xs[1], ys[1]), ...
plt.title("$y = x^2$ with 5 inputs")       # $...$ draws real math, like x²
plt.grid(alpha=0.3)
plt.show()


pause(2)

# 2. More inputs -> more dots -> a smooth curve.
#    Instead of typing inputs by hand, a loop makes 101 of them:
#    -3.00, -2.94, -2.88, ..., 3.00   (a step of 0.06 each time)
xs = []
for k in range(101):
    xs.append(-3 + k * 0.06)     # k = 0 gives -3,  k = 100 gives -3 + 6 = 3
ys = [g(x) for x in xs]          # same as the loop in section 1, written on one line
print("\nhow many dots:", len(xs))

plt.plot(xs, ys, linewidth=3)    # plot() joins neighboring dots with tiny straight lines
plt.title("$y = x^2$ with 101 inputs")
plt.grid(alpha=0.3)
plt.show()


pause(3)

# 3. Is a point ON the graph?  Plug in its x. Does the machine give back its y?
def f(x):
    """Episode 0.3's first machine: double it, then add 1."""
    return 2 * x + 1


def on_graph(point):
    x, y = point                 # unpack the pair: x is across, y is up
    return f(x) == y             # True if the machine's output matches the y


print("\n(2, 5) on the graph of f?", on_graph((2, 5)))   # True:  f(2) = 5
print("(3, 8) on the graph of f?", on_graph((3, 8)))     # False: f(3) = 7, not 8


pause(4)

# 4. Lines:  y = w*x + b.   Turn one knob at a time and watch what happens.
#    A line only needs TWO points, so we only plug in x = -3 and x = 3.
def line(x, w, b):
    return w * x + b


ends = [-3, 3]
for w in [-1, 0, 1, 3]:          # turn the w knob (b stays at 1)
    plt.plot(ends, [line(x, w, 1) for x in ends], linewidth=3, label="w = " + str(w))
plt.title("w TILTS the line   (b = 1)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

for b in [-2, 1, 4]:             # turn the b knob (w stays at 2)
    plt.plot(ends, [line(x, 2, b) for x in ends], linewidth=3, label="b = " + str(b))
plt.title("b SLIDES the line up and down   (w = 2)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

print("\nWhere does y = 2x + 1 cross the y-axis?  At x = 0, y =", line(0, 2, 1))


pause(5)

# 5. Our five students, and the model from Episode 0.1:  y_hat = w*x + 40
hours = [1, 2, 3, 4, 5]          # x: hours studied
scores = [49, 56, 65, 71, 82]    # y: test scores

plt.scatter(hours, scores, s=120, color="black", zorder=3)
for w in [5, 8.18]:              # a bad knob setting, then (about) the best one
    plt.plot([0, 6], [line(0, w, 40), line(6, w, 40)], linewidth=3, label="w = " + str(w))
plt.title("Same data, two settings of the knob w")
plt.xlabel("hours studied")
plt.ylabel("test score")
plt.legend()
plt.grid(alpha=0.3)
plt.show()


pause(6)

# 6. The error valley is a PARABOLA.
#    Long way:  the loop from Episode 0.3.
#    Short way: the tidy formula  E(w) = 11 w^2 - 180 w + 737.4
#    If they really are the same machine, they must agree for EVERY w we try.
def error_long(w):
    total = 0
    for i in range(len(hours)):
        miss = scores[i] - line(hours[i], w, 40)
        total = total + miss ** 2
    return total / len(hours)


def error_short(w):
    return 11 * w * w - 180 * w + 737.4


print("\n   w | long way | short way")
for w in [2, 5, 8, 11, 14]:
    print(f"{w:4} | {error_long(w):8.1f} | {error_short(w):9.1f}")   # :8.1f = 8 wide, 1 decimal

# Where is the bottom?  Use the mirror idea.
#   11w^2 - 180w = w * (11w - 180), which is 0 when w = 0 and when w = 180/11.
#   So those two knob settings have the SAME error (737.4), like the mirror pairs on x^2.
#   The bottom of the U sits exactly halfway between them.
print("\nE(0)      =", round(error_short(0), 1))                # 737.4
print("E(180/11) =", round(error_short(180 / 11), 1))           # 737.4, the same height
print("bottom of the valley: w =", round((0 + 180 / 11) / 2, 2))   # 8.18


pause(7)

# 7. The loss curve: the graph every AI engineer watches during training.
#    This is Episode 0.1's gradient descent, unchanged. We just keep a list
#    of the error score after every step, and graph it.
w, eta = 5, 0.02                 # first guess, step size
errors = [error_long(w)]         # the error before any training (112.4)
for step in range(15):
    steepness = 0
    for x, y in zip(hours, scores):
        miss = y - line(x, w, 40)
        steepness = steepness + (-2 * x * miss / len(hours))
    w = w - eta * steepness      # a small step downhill
    errors.append(error_long(w))

print("\nerror after each step:", [round(e, 2) for e in errors[:5]], "...")
plt.plot(range(len(errors)), errors, marker="o", linewidth=3)
plt.title("The loss curve: training step across, error score up")
plt.xlabel("training step")
plt.ylabel("error score")
plt.grid(alpha=0.3)
plt.show()
