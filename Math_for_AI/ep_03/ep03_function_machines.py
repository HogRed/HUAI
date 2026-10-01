"""
Math for AI  |  Episode 0.3: "Functions as Machines"
"""

# 0. Last episode's challenge:   sum_{i=1}^{5} x_i * y_i
hours = [1, 2, 3, 4, 5]          # x_1 ... x_5   (hours studied)
scores = [49, 56, 65, 71, 82]    # y_1 ... y_5   (test scores)

total = 0
for i in range(len(hours)):
    total = total + hours[i] * scores[i]     # side by side in math means multiply
print("Challenge answer:", total)            # 1050


# 1. Build our first machine:   f(x) = 2x + 1
def f(x):
    """Double it, then add 1."""
    return 2 * x + 1


print("f(3)  =", f(3))       # 7
print("f(10) =", f(10))      # 21

# Same input, same output. Every single time.  (That's the rule for a function.)
print("f(3) again =", f(3))  # still 7


# 2. A table of inputs and outputs: feed the machine one input at a time
print("\nx | f(x)")
print("--+-----")
for x in [0, 1, 2, 3, 4]:
    print(x, "|", f(x))          # input, then what the machine sends out


# 3. Episode 0.1's model is a machine with KNOBS
#       y_hat = f(x) = w*x + b
#    x is the INPUT (hours).  w and b are knobs (parameters) we can turn.
def predict(x, w, b):
    """Predicted test score for someone who studied x hours."""
    return w * x + b


print("\nPrediction for 3 hours, w = 5:   ", predict(3, 5, 40))     # 55
print("Prediction for 3 hours, w = 8.18:", round(predict(3, 8.18, 40), 2))   # 64.54
# (round(..., 2) keeps 2 decimals; computers store decimals slightly imperfectly)
# Same input (3 hours). Turning the knob w changed the output.
# Training an AI = turning the knobs until the outputs get as close
# to the real scores as they can.


# 4. A machine with TWO input slots (made-up knobs, just to see the idea)
#       f(x1, x2) = w1*x1 + w2*x2 + b
def predict2(x1, x2):
    w1, w2, b = 4, 3, 20       # made-up knob settings
    return w1 * x1 + w2 * x2 + b


print("\n3 hours studied, 8 hours of sleep:", predict2(3, 8))       # 56


# 5. Chaining machines: the output of one becomes the input of the next
def g(x):
    """Square it."""
    return x * x


print("\ng(f(3)) =", g(f(3)))    # f first: 3 -> 7,  then g: 7 -> 49
print("f(g(3)) =", f(g(3)))      # g first: 3 -> 9,  then f: 9 -> 19
# Read the INSIDE first. Order matters!


# 6. ReLU: a tiny machine used inside real neural networks
#       ReLU(z) = max(0, z):  zero or negative in, zero out; otherwise pass it through
#    (z is just the input's name. Any letter works.)
def relu(z):
    if z < 0:
        return 0
    return z


print()
for z in [-3, -1, 0, 2, 5]:
    print("ReLU(" + str(z) + ") =", relu(z))     # str() turns a number into text


# 7. The error is a machine too:  put in a knob setting w, get out how wrong we are
#       E(w) = (1/n) * sum of (y_i - (w*x_i + b))^2
#    It uses hours and scores from section 0, and predict() from section 3.
#    The students' data stays fixed, and b stays at 40. Only w goes in.
def error_score(w):
    b = 40
    total = 0
    for i in range(len(hours)):                  # same loop style as section 0
        miss = scores[i] - predict(hours[i], w, b)   # one student's miss
        total = total + miss ** 2                # squared, then added on
    return total / len(hours)                    # divided by n


print()
for w in [2, 5, 8, 8.18, 11]:
    print("E(" + str(w) + ") =", round(error_score(w), 1))   # round to 1 decimal place
# E(5) = 112.4 is Episode 0.1's starting point.
# The output is smallest near w = 8.18: the bottom of the valley.
