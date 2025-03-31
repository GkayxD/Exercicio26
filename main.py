# Inicializar o vetor
numeros = []

# Ler 20 números inteiros do usuário
print("Por favor, insira 20 números inteiros:")
for i in range(20):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

# Ordenar os números em ordem crescente
numeros.sort()

# Exibir os números ordenados
print("\nNúmeros ordenados crescentemente:")
for numero in numeros:
    print(numero)