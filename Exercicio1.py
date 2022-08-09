#Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N n
# úmeros inteirose armazene-os em um vetor. Em seguida, mostrar na tela todos os
# números negativos lidos.
vetc=0
n=int(input("Informe um número inteiro até 10: "))
vet: [float]=[0 for x in range (n)]  #nomeação do vetor dentro de um intervalo de números reais
for x in range(0,n):    #condição for para um intervalo conhecido de 0 ao valor digitado pelo usuário
    vet[x]=float(input("Digite um número: "))   #vetor ao qual será lançado os valores correspondentes do intervalo de N
print("Os numeros inteiros negativos:")
for x in range (n):  #para o intervalo o valor x (de 0 ao valor de N) será mostrado
    if vet[x]<0:    #os valores do vetor, se o mesmo for menor do 0, sendo ele negativo.
        print(f"{vet[x]}")