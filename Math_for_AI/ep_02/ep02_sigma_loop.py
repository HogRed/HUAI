"""
Math for AI  |  Episode 0.2: "Sigma is just a for loop"
"""

# The same five students from Episode 0.1
hours = [1, 2, 3, 4, 5]          # x_1 ... x_5
scores = [49, 56, 65, 71, 82]    # y_1 ... y_5
n = len(hours)                   # n = 5, HOW MANY students

# 1. Sigma of the scores:   sum_{i=1}^{5} y_i
total = 0                              # start the total at zero
for i in range(n):                     # i = 0, 1, 2, 3, 4   (Python counting)
    total = total + scores[i]          # add on this student's score
    print(f"after student {i + 1}: total = {total}")   # i + 1 = math counting

print("Sigma of y_i =", total)         # 323

# 2. The average:   y_bar = (1/n) * sum_{i=1}^{n} y_i
y_bar = total / n
print("y-bar (the average score) =", y_bar)          # 64.6

# 3. Sigma of the squares:   sum_{i=1}^{5} x_i^2
#    Same loop, we just change WHAT we add each time.
total_sq = 0
for i in range(n):
    total_sq = total_sq + hours[i] ** 2    # ** means "to the power of"
print("Sigma of x_i squared =", total_sq)  # 55

# 4. Episode 0.1's error formula, read straight off the symbols:
#       Error = (1/n) * sum_{i=1}^{n} (y_i - y_hat_i)^2
#    with the first guess from Episode 0.1:  y_hat = 5x + 40
w, b = 5, 40
total_err = 0
for i in range(n):
    y_hat = w * hours[i] + b               # y-hat sub i: the prediction
    miss = scores[i] - y_hat               # y sub i minus y-hat sub i
    total_err = total_err + miss ** 2      # ...squared, and added to the total
error = total_err / n                      # one over n: the average
print("Error at w = 5 =", error)           # 112.4 (same as Episode 0.1!)

# Python's built-in sum() does the exact same loop for us
print("check with sum():", sum(scores), sum(x ** 2 for x in hours))

# YOUR CHALLENGE (answer in Episode 0.3):
#     Compute  sum_{i=1}^{5} x_i * y_i   by hand.
#     Then check it: copy loop 1 above into a new block down here, and
#     change   scores[i]   to   hours[i] * scores[i]   (* means "times")
