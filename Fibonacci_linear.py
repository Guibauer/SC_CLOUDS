def fib(posicao):
    if posicao <= 1:
        return posicao
    fib1, fib2 = 0, 1
    for _ in range(2, posicao + 1):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


num = int(input("Digite a posição para o valor Fibonacci: "))    
while num < 0:
    print("Erro: A posição deve ser um número inteiro maior ou igual a zero.")
    num = int(input("Digite a posição para o valor Fibonacci: "))    
else:
    resultado = fib(num)
    print("Na %dª posição o valor é \033[1;033m%d" % (num,resultado))