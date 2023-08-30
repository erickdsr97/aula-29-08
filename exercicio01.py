# resolução exercício
n = int(input("Digite o número desejado:"))

indice = 1
somaTotal = 0

while indice <= n:
    # 1) somaTotal = 0 + 1
    # 2) somaTotal = 1 + 2
    # 3) somaTotal = 3 + 3
    somaTotal = somaTotal + indice

    print("indice:", indice)    
    print("soma parcial", somaTotal)
    print("-----------")
    
    indice = indice + 1
    
print("soma total:",somaTotal)
    