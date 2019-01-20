squares = []
# for beginners
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# simple functions
digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits))
print(max(digits))
print(sum(digits))

# for advanced
squares = [value ** 2 for value in range(1,5)]
print(squares)