import math


def normalizacao(dado, minimo, maximo):
    resultado = int(((dado - minimo) / (maximo - minimo)))
    return resultado


def lerArquivo(url):
    arquivo = open(url)

    maximo = 0
    minimo = 99999

    conteudo = []

    for line in arquivo:
        # pega uma linha do arquivo e atribui em aux1
        aux1 = line.split('\n')

        # separa todos os atributos desta linha e atribui em aux2
        aux2 = aux1[0].split(',')

        for x in range(len(aux2)):
            if(float(aux2[x]) > maximo):
                maximo = float(aux2[x])
            if(float(aux2[x]) < minimo):
                minimo = float(aux2[x])

        # armazena o tamanho da instancia para saber quantos atributos tem
        tamanhoInstancia = len(aux2)

        # cada posição do vetor conteudo tem uma instancia formatada ex: conteudo[0] contém ['1', '2', '3', ..., 'n']
        conteudo.append(aux2)

    # ===========   normalizacao   =======================

    # for x in range(len(conteudo)):
    #     for y in range(tamanhoInstancia - 1):
    #         conteudo[x][y] = normalizacao(
    #             float(conteudo[x][y]), minimo, maximo)

    # ===========   normalizacao   =======================

    return conteudo, tamanhoInstancia


conteudo, tamanhoInstancia = lerArquivo('dataset2.txt')


def distanciaEuclidiana(instanciaA, instanciaB, tamanhoInstancia):
    soma = 0
    instanciaAInt = []
    instanciaBInt = []

    # transforma o vetor de string para inteiro
    for x in range(tamanhoInstancia - 1):
        instanciaAInt.append(float(instanciaA[x]))

    for x in range(tamanhoInstancia - 1):
        instanciaBInt.append(float(instanciaB[x]))

    # calcula a distanciaEuclidiana
    for x in range(tamanhoInstancia - 1):
        soma += ((instanciaAInt[x] - instanciaBInt[x]) ** 2)

    return soma ** (1/2)


def classificarAmostra(conteudo, novaInstancia, k, tamanhoInstancia):
    distancias = []
    instaciaComparada = []
    classe1 = 0
    classe2 = 0
    classe3 = 0

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
        elif (distanciasOrdenadas[x][1] == 2):
            classe2 += 1
        elif(distanciasOrdenadas[x][1] == 3):
            classe3 += 1

    if(classe1 > classe2):
        if(classe1 > classe3):
            print("valor pertence a classe 1")
            return 1
    elif(classe2 > classe1):
        if(classe2 > classe3):
            print("valor pertence a classe 2")
            return 2
    else:
        print("valor pertence a classe 3")
        return 3

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
        conteudo_teste.append(conteudo[cont])
        cont += 1

    # realiza os teste e anota a quantidade de acertos

    for x in range(qtd_teste):
        classe = classificarAmostra(
            conteudo_treinamento, conteudo_teste[x], k, tamanhoInstancia)
        classe_esperada = int(conteudo_teste[x][tamanhoInstancia - 1])
        if(classe_esperada == classe):
            numero_acertos += 1

    print("\nnumero de instancias: ", qtd_instancias)
    print("numero de treinamento: ", qtd_treinamento)
    print("numero de teste: ", qtd_teste)
    print("numero de acertos: ", numero_acertos)


k = int(input("\ninsira o valor de k: "))

treinamento(conteudo, k)

# // 1 = Iris-setosa
# // 2 = Iris-Versicolor
# // 3 = Iris-Virginica


while(1):
    amostra = input('\ninsita a nova amostra: ')
    amostra = amostra.split(',')
    classificarAmostra(conteudo, amostra, k, tamanhoInstancia)
