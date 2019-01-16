cars = ['bmw','audi','toyota','subaru']
# função sort altera o valor da variável
#cars.sort() | param reverse determina a ordem alfabética de forma reversa
cars.sort(reverse=True)
print(cars)

# função sorted não altera o valor da variável

cars2 = ['volks', 'ford', 'jac', 'fiat']

print('Utilizando sorted: '+ str(sorted(cars2)))
print('Valor original: '+ str(cars2))
cars2.reverse
print('Valor original em ordem reversa: ' + str(cars2))
tamanhoLista = len(cars2)
print(tamanhoLista)