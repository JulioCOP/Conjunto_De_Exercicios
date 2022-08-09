#Fazer um programa para ler duas matrizes de números inteiros A e B, contendo de
#M linhas e N colunas cada (M e N máximo = 10). Depois, gerar uma terceira matriz
#C onde cada elemento desta é a somados elementos correspondentes das matrizes
#originais. Imprimir na tela a matriz gerada

m=int(input("INFORME O NÚMERO DE LINHAS: "))
n=int(input("INFORM O NÚMERO DE COLUNAS: "))
matA:[[int]]=[[0 for x in range (n)]for x in range(m)]
matB:[[int]]=[[0 for x in range (n)]for x in range(m)]
matC:[[int]]=[[0 for x in range(n)]for x in range(m)]
print("DIGITE OS VALORES DA MATRIZ A")
for i in range(m):
    for j in range(n):
        matA[i][j]=int(input(f"ELEMENTO [{i},{j}]: "))
print("DIGITE OS VALORES DA MATRIZ B")
for i in range(m):
    for j in range(n):
        matB[i][j]=int(input(f"ELEMENTO [{i},{j}]: "))
for i in range(m):
    for j in range(n):
        matC[i][j]= matA[i][j] + matB[i][j]

print("O VALOR DA SOMA DAS MATRIZES DE A E B É: ")
for i in range (m):
    for j in range(n):
        print(f"{matC[i][j]}", end=" ")
    print()