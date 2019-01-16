#trocando o valor de um índice
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'triumph'

print(motorcycles)

#adicionando um item à lista

motorcycles.append('ducati')

print(motorcycles)

othersMotorcycles = []
othersMotorcycles.append('harley-davidson')
othersMotorcycles.append('terere')

print(othersMotorcycles)

othersMotorcycles.insert(0, 'honda')

print(othersMotorcycles)

del othersMotorcycles[0]

print(othersMotorcycles)

popped = othersMotorcycles.pop()
print(othersMotorcycles)
print('Popped item '+popped)

motorcycles.remove('triumph')

print(motorcycles)