
# Definição das variaves de entrada
estds = input().split(" ")
alfabeto = input().split(" ")
transacoes = int(input())

afnd = {}

for estd in estds:
    afnd[estd] = {}

# Realiza a quantidade de transações a depender do valor do usuario
contador = 0
while (contador < transacoes):

    elementInicial, elementAtual, elementFinal = input().split(" ")
    if elementAtual not in afnd[elementInicial]:
        afnd[elementInicial][elementAtual] = [elementFinal]
    else:
        afnd[elementInicial][elementAtual].append(elementFinal)
    contador = contador + 1

#Armazena os valores dos estados iniciais, final e das palavras
estd_inicial = input()
estd_final = input().split(" ")
palavras = input().split(" ")

estds_finais = {}

for index in estd_final:
    estds_finais[index] = 1

for palavra in palavras:
    estdsAtuais = [estd_inicial]
    estdFinal = 0

    for letra in palavra:
        novosEstados = []

        for estd in estdsAtuais:
            if(afnd[estd].get(letra)):

                for novoEstado in afnd[estd][letra]:
                    if(novoEstado not in novosEstados):
                        novosEstados.append(novoEstado) # armazena um novo estado no array 

        estdsAtuais = novosEstados

    for estd in estdsAtuais:
        if(estds_finais.get(estd)):
            estdFinal = 1
 # Escreve 'S' se a palavra for aceita e 'N' se a apalvra não for aceita pelo AFND
    if(estdFinal == 1):
        print('S')
    else:
        print('N')