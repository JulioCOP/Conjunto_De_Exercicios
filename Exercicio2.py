#Fazer um programa para ler dois números inteiros M e N (máximo = 10). Em seguida, ler uma
# matriz de M linhas e N colunas contendo números reais. Gerar um vetor de modo que cada
# elemento do vetor seja a soma dos elementos da linha correspondente da matriz.
# Mostrar o vetor gerado.

m=int(input("Informe a quantidade de linhas da matriz: "))
n=int(input("Informe a quantidade de colunas: "))
mat: [[float]]=[[0 for x in range (n)] for x in range(m)]
vet_mat:[float]=[0 for x in range(m)]
for i in range (0,m):
    print(f"Digite os elmentos da  {i + 1}º linha da matriz:")
    for j in range (0,n):
        mat[i][j] = float(input(""))
print()
for i in range(m):
    soma_linha = 0
    for j in range(n):            #Para fazer a somatória das linhas da matriz, é necessário
        soma_linha+=mat[i][j]      #percorrer as colunas da matriz...Exemplo
    vet_mat[i]=soma_linha         #linha 0= soma todos os intens da coluna de 0 até N
print(f"VETOR GERADO {vet_mat}")

