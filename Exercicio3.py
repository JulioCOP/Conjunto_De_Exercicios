#Ler dois números M e N (máximo = 10), e depois ler uma matriz MxN de números inteiros.
# Em seguida, mostrar na tela somente os números negativos da matriz.

m=int(input("Informe quantidade de linhas da matriz: "))
n=int(input("Informe a quantidade de colunas da matriz: "))

mat:[[int]]=[[0 for x in range(0,n)]for x in range (0,m)]

for i in range(m):
    for j in range(n):
        mat[i][j]= int(input(f"ELEMENTO [{i}], [{j}]: "))

print("VALORES NEGATIVOS")
for i in range(m):
    for j in range(n):
        if mat[i][j]<0:
            print(mat[i][j])



