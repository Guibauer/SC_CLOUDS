def primos_linear(p): 
    if p > 1:
        for contador in range(2, int(p**0.5) + 1):
            if p % contador == 0:
                return False
        return True
    
def primos_seq(p):
    primos = []
    for num in range(2, p + 1):
        if primos_linear(num):
            primos.append(num)
    return primos

p = int(input("Digite um número inteiro maior que \033[33m 1 \033[0m para gerar todos os primos até ele: "))

while p < 2:
    print("Erro: O número deve ser um número inteiro maior que 1. ")
    p = int(input("Digite um número inteiro maior que \033[33m 1 \033[0m: "))

resultado = primos_seq(p)
print(f"Números primos até {p}: \033[33m{resultado}\033[0m")
