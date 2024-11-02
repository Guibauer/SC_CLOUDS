def fib(posicao):
    if posicao <= 1:
        return posicao
    else: 
        return fib(posicao - 1) + fib(posicao - 2)

num = int(input("Digite a posição para o valor Fibonacci: "))    
while num < 0:
    print("Erro: A posição deve ser um número inteiro maior ou igual a zero.")
    num = int(input("Digite a posição para o valor Fibonacci: "))    
else:
    resultado = fib(num)
    print("Na %dª posição o valor é \033[1;033m%d" % (num, resultado))




