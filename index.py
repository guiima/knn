import math


def lerArquivo(url):
    arquivo = open(url)

    conteudo = []

    for line in arquivo:
        # pega uma linha do arquivo e atribui em aux1
        aux1 = line.split('\n')

        # separa todos os atributos desta linha e atribui em aux2
        aux2 = aux1[0].split(',')

        # armazena o tamanho da instancia para saber quantos atributos tem
        tamanhoInstancia = len(aux2)

        # cada posição do vetor conteudo tem uma instancia formatada ex: conteudo[0] contém ['1', '2', '3', ..., 'n']
        conteudo.append(aux2)

    return conteudo, tamanhoInstancia


conteudo, tamanhoInstancia = lerArquivo('dataset.txt')


def distanciaEuclidiana(instanciaA, instanciaB, tamanhoInstancia):
    soma = 0
    instanciaAInt = []
    instanciaBInt = []

    # transforma o vetor de string para inteiro
    for x in range(tamanhoInstancia):
        instanciaAInt.append(int(instanciaA[x]))

    for x in range(tamanhoInstancia):
        instanciaBInt.append(int(instanciaB[x]))

    # calcula a distanciaEuclidiana
    for x in range(tamanhoInstancia - 1):
        soma += ((instanciaAInt[x] - instanciaBInt[x]) ** 2)

    return soma ** (1/2)


def classificarAmostra(conteudo, novaInstancia, k, tamanhoInstancia):
    distancias = []
    instaciaComparada = []
    classe1 = 0
    classe2 = 0

    # força o k a ser impar
    if(k % 2 == 0):
        k -= 1
        print(k)
        if(k <= 0):
            k = 1

    qtd_instancias = len(conteudo)

    if(k > qtd_instancias):
        return print("valor de K maior que a quantidade de instancias")

    for x in range(qtd_instancias):

        # atribui a distanciaEuclidiana ao vetor "instanciaCompara"
        instaciaComparada.append(distanciaEuclidiana(
            conteudo[x], novaInstancia, tamanhoInstancia))

        # atribui a classe ao vetor "instanciaCompara"
        instaciaComparada.append(int(conteudo[x][tamanhoInstancia - 1]))

        # atribui o conjunto com a distancia e a classe no vetor de distancias
        distancias.append(instaciaComparada)

        instaciaComparada = []

    distanciasOrdenadas = sorted(distancias)

    for x in range(k):
        if(distanciasOrdenadas[x][1] == 1):
            classe1 += 1
        else:
            classe2 += 1

    if(classe1 > classe2):
        print("valor pertence a classe 1")
        return 1
    elif(classe1 < classe2):
        print("valor pertence a classe 2")
        return 2
    else:
        print("empate")
        return 0

    # return distanciasOrdenadas


# vet = [1, 2, 1, 2]

# x = classificarAmostra(conteudo, vet, 4, tamanhoInstancia)
# print(x)


def treinamento(conteudo, k):
    numero_acertos = 0
    qtd_instancias = len(conteudo)
    conteudo_treinamento = []
    conteudo_teste = []

    # 70% de treinamento e 30% de teste (math.ceil arrendoda pra cima o valor obtido)
    qtd_treinamento = math.ceil(qtd_instancias * 0.7)
    qtd_teste = qtd_instancias - qtd_treinamento

    # coloca as instancias de treinamento em um vetor separado
    for x in range(qtd_treinamento):
        conteudo_treinamento.append(conteudo[x])

    # coloca as instancias de teste em um vetor separado
    cont = qtd_treinamento
    while(cont < qtd_instancias):
        conteudo_teste.append(conteudo[qtd_treinamento])
        cont += 1

    # realiza os teste e anota a quantidade de acertos
    for x in range(qtd_teste):
        classse = classificarAmostra(
            conteudo_treinamento, conteudo_teste[x], k, tamanhoInstancia)

        classe_esperada = int(conteudo_teste[x][tamanhoInstancia - 1])

        if(classe_esperada == classse):
            numero_acertos += 1
        print("numero de acertos: ", numero_acertos)


treinamento(conteudo, 3)
