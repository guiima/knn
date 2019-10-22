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

    # transforma o vetor de string para inteiro
    for x in range(tamanhoInstancia):
        instanciaAInt.append(int(instanciaA[x]))

    # calcula a distanciaEuclidiana
    for x in range(tamanhoInstancia - 1):
        soma += ((instanciaAInt[x] - instanciaB[x]) ** 2)

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
    elif(classe1 < classe2):
        print("valor pertence a classe 2")
    else:
        print("empate")

    return distanciasOrdenadas


vet = [1, 2, 1, 2]

x = classificarAmostra(conteudo, vet, 4, tamanhoInstancia)
print(x)
