# Using a for loop, generate a list of squares of only the odd numbers from 1 to 20.
squares = []
for num in range(1, 21):
    if num % 3 != 0:
        sq = num ** 2
        squares.append(sq)
print("Squares of odd numbers from 1 to 20:", squares)

