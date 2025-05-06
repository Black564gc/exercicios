def soma_numeros(lista):
    soma = 0
    for i in lista:
        soma += i

    return soma
    
numeros = [10, 8, 5, 3]

print(soma_numeros(numeros))