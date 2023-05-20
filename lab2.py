from itertools import permutations
import math

# funkcija za odredivanje tezine brida
def weight(a, b, k, l):
    return (a*k + b*l)*(a*k + b*l) + 1

def sum(graph, i, n):
    size = 0
    for j in range(n):
        if(j < n-1):
            size = size + graph[i[j]][i[j+1]]
        else:
            size = size + graph[i[n-1]][i[0]]
    return size

# funkcija racunanja najkrace duljine ciklusa grafa pohlepnim algoritmom
def pohlepniAlgoritam(n, graph):
    distance = 0
    head = 0
    tail = 1

    # trazimo brid najmanje tezine
    for rows in range(n):
        for columns in range(n):
            if(graph[rows][columns] < graph[head][tail] and graph[rows][columns] != 0):
                tail = columns
                head = rows

    distance = distance + graph[head][tail]

    visited = [0] * n
    visited[head] = 1
    visited[tail] = 1
    counter = 0
    headCounter = 0
    tailCounter = 0

    # trazimo najkrace sljedece korake
    while(visited != [1] * n):
        for i in range(n):
            if (visited[i] != 1):
                if (counter == 0):
                    shortestNext = i
                    counter = 1
                else:
                    if (graph[tail][i] < graph[tail][shortestNext]):
                        shortestNext = i
                        tailCounter = 1
                        headCounter = 0
                    elif (graph[head][i] < graph[head][shortestNext]):
                        shortestNext = i
                        headCounter = 1
                        tailCounter = 0

        if (graph[head][shortestNext] == min(graph[head][shortestNext], graph[tail][shortestNext])):
            headCounter = 1
            tailCounter = 0
        else:
            tailCounter = 1
            headCounter = 0

        if(tailCounter == 1):
            distance = distance + graph[tail][shortestNext]

            tail = shortestNext
            visited[shortestNext] = 1
            counter = 0
        else:
            distance = distance + graph[head][shortestNext]

            head = shortestNext
            visited[shortestNext] = 1
            counter = 0

    distance = distance + graph[tail][head]

    return distance

# funkcija racunanja najkrace duljine ciklusa grafa iscrpnom pretragom
def iscrpnaPretraga(n, graph):
    # definiram vrijednosti vrhova koje krecu od 0, zbog lakseg indeksiranja
    vertex = [0] * n
    for j in range(n):
        vertex[j] = j

    counter = 0
    counterOfVisited = 0
    numberOfPerm = math.factorial(n-1)

    # racunamo sve moguce kombinacije pomocu permutacije
    for i in permutations(vertex):
        if(counterOfVisited < numberOfPerm):
            counterOfVisited = counterOfVisited + 1
        else:
            break

        if(counter == 0):
            minValue = valueOfPath = sum(graph, i, n)
            counter = 1
        else:
            valueOfPath = sum(graph, i, n)

        if(valueOfPath < minValue):
            minValue = valueOfPath

    return minValue

# pocetak glavnog dijela programa
n, a, b = input("Unesite redom, odvojene razmakom, parametre n, a i b: ").split()

# castanje tipa int na vrijednosti varijabli
n = int(n)
a = int(a)
b = int(b)

# racunamo tezinski graf
graph = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(i < j):
            graph[i][j] = weight(a, b, (i+1), (j+1))
        elif(i == j):
            graph[i][j] = 0
        else:
            graph[i][j] = weight(a, b, (j+1), (i+1))

# poziv funkcija i spremanje vrijednosti
duljinaPohlepnogAlgoritma = pohlepniAlgoritam(n, graph)
duljinaIscrpnePretrage = iscrpnaPretraga(n, graph)

# ispis trazenih vrijednosti
print("Pohlepni algoritam nalazi ciklus duljine:", duljinaPohlepnogAlgoritma)
print("Iscrpni algoritam nalazi ciklus duljine:", duljinaIscrpnePretrage)

if(duljinaIscrpnePretrage == duljinaPohlepnogAlgoritma):
    print("Pohlepni algoritam na ovom grafu daje optimalno rješenje!")
else:
    print("Pohlepni algoritam na ovom grafu ne daje optimalno rješenje!")