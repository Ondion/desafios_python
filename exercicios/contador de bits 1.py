# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary
# representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def countBits(n):
    n = int(n) # convertendo a entrada em inteiros
    if n < 0: # Evitando a entrada de valores negativos
        n = -1 * n

    count_a = bin(n) # convertendo para binario
    count_b = 0
    for x in count_a: # varrendo a lista com o valor binario e buscando apenas os valores '1'
        if x == '1':
            count_b += 1 # para cada '1' o contador B é incrementado
    return count_b # retornando a resposta
