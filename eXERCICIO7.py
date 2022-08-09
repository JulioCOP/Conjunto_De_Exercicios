#Ler uma matriz quadrada de ordem N (máximo = 10), contendo números reais. Em seguida,
# fazer as seguintes ações:
# a) calcular e imprimir a soma de todos os elementos positivos da matriz.
# b) fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos
# os elementos desta linha.
# c) fazer a leitura do índice de uma coluna da matriz e, daí, imprimir todos
# os elementos desta coluna.
# d) imprimir os elementos da diagonal principal da matriz.
# e) alterar a matriz elevando ao quadrado todos os números negativos da mesma. Em seguida imprimir
# a matriz alterada.
import math
n= int(input("Informe a ordem de uma matriz quadrada: "))
mat:[[float]]=[[0 for x in range(n)]for x in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j]=float(input(f"ELEMENTO: [{i},{j}]: "))
print("\033[1;31mSOMA DOS Nºs POSITIVOS:\033[m")
soma=0
for i in range(n):
    for j in range(n):
        if mat[i][j]>0:
            soma+= mat[i][j]
print(f"\033[1;32m{soma:.1f}\033[m")
print()
escolha_linha = int(input("Escolha uma linha de acordo com a ordem informada: "))
print("\033[1mLINHA ESCOLHIDA: \033[m",end=" ")
for i in range(n):
    print(f"\033[1;32m{mat[escolha_linha][i]:.1f}\033[m", end=" ")
print()
escolha_coluna= int(input("\nEscolha uma coluna de acordo com a ordem informada: "))
print("\033[1mCOLUNA ESCOLHIDA: \033[m", end=" ")
for i in range(n):
    print(f"\033[1;32m{mat[i][escolha_coluna]:.1f}\033[m", end=" ")
print()
print("\n\033[1mA diagonal principal é: \033[m")
for i in range(n):
    for j in range(n):
        if i==j:
            print(f"\033[1;31m{mat[i][j]}\033[m", end=" ")
for i in range(n):
    for j in range(n):
        if mat[i][j]<0:
            mat[i][j]= math.pow(mat[i][j],2)
print("\nMatriz alterada: ")
for i in range(n):
    for j in range(n):
        print(f"\033[1;36m{mat[i][j]}\033[m", end=" ")
    print()


