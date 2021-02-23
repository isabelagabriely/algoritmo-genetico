import random

def criar_individuo (min, max, tamanho_individuo):
    individuo = []

    for i in range(tamanho_individuo):
        individuo.append(random.randint(min,max))

    return individuo


def criar_populacao (tamanho_populacao):
    populacao = []

    for i in range(tamanho_populacao):
        populacao.append(criar_individuo(0,9,4))

    return populacao


def aptidao (individuo, modelo_individuo):
    apto = 0

    for i in range(len(individuo)):
        distancia = modelo_individuo[i] - individuo[i]

        if distancia < 0:
            distancia*=-1

        apto+=distancia
        distancia = 0

    return apto


def pontuacao (populacao, modelo_individuo):
    pontuados = []

    for i in range(len(populacao)):
        pontuados.append([aptidao(populacao[i], modelo_individuo), populacao[i]])

    pontuados.sort()

    return pontuados


def torneio (pontuados, tamanho_populacao):
    selecionados = []
    m = 3

    for i in range(tamanho_populacao):
        mais_apto = random.choice(pontuados)

        for i in range(m-1):
            cromossomo = random.choice(pontuados)

            if cromossomo[0] < mais_apto[0]:
                mais_apto = cromossomo

        selecionados.append(mais_apto)

    return selecionados


def cruzamento (individuo1, individuo2):
    ponto = random.randint(1,3)
    filhos = []

    filhos.append(individuo1[:ponto]+individuo2[ponto:])
    filhos.append(individuo2[:ponto]+individuo1[ponto:])

    return filhos


def mutacao (individuo):
    ponto = random.randint(0,3)
    individuo[ponto] = random.randint(0,9)

    return individuo


#modelo
print('Digite 4 numeros de 0-9')
m1, m2, m3, m4 = input().split(" ")
modelo = []
modelo.append(int(m1))
modelo.append(int(m2))
modelo.append(int(m3))
modelo.append(int(m4))

#população inicial
populacao1 = criar_populacao(6)
print("populacao criada:",populacao1)
print("\n")

x = -1

while (x != 0):

    pontuacao1 = pontuacao(populacao1, modelo)
            
    torneio1 = torneio(pontuacao1, 6)

    populacao1.clear()

    #cruzamento
    for i in range(3):
        individuo1 = random.choice(torneio1)
        torneio1.remove(individuo1)
        individuo2 = random.choice(torneio1)
        torneio1.remove(individuo2)

        filho = cruzamento(individuo1[1], individuo2[1])

        populacao1.append(filho[0])
        populacao1.append(filho[1])

    #mutação
    for i in range(2):
        mutado = random.choice(populacao1)
        mutacao(mutado)

    print("populacao criada:",populacao1)
    print("\n")

    #verificação se há um individuo igual ao modelo
    for i in range(6):
        if populacao1[i] == modelo:
            individuo_modelo = []
            individuo_modelo = populacao1[i]
            x = 0

print("MODELO DE INDIVIDUO INICIAL ENCONTRADO", individuo_modelo)