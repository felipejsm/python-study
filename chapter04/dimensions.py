# Tuples are immutable lists!
dimensions = (200, 50) # () != []
print(dimensions[0])
print(dimensions[1])


[print(dimension) for dimension in dimensions]

dimensions = (400, 100)
print("\nNovos valores para a Tupla")

[print(dimension) for dimension in dimensions]