# funckija koja provjerava je li sigurno dati boju
def safeToColour(graph, vertex, colours, colour, n):
    for j in range(n):
        if(graph[vertex][j] == 1 and colour == colours[j]):
            return False
    return True

# funckija za bojanje grafa
def graphColoring(graph, m, colours, vertex, n):
    if(vertex == n):
        return True
    
    for colour in range(1, m+1):
        if(safeToColour(graph, vertex, colours, colour, n)):
            colours[vertex] = colour
            if(graphColoring(graph, m, colours, vertex+1, n)):
                return True
            colours[vertex] = 0
    return False

# otvaranje i zatvaranje datoteke
filename = input("Unesite ime datoteke: ")
with open(filename, "r") as file:
    n = int(file.readline())
    m = int(file.readline())
    S = file.readline().split()

file.close()

# promjena tipa podataka unutar liste iz stringa u integer
S = list(map(int, S))

# punjenje matrice grafa vrijednostima 1 koje oznacavaju susjedne vrhove
graph = [[0]*n for _ in range(n)]
for k in range(n):
        for l in range(n):
            value = k - l
            if(value in S):
                graph[k][l] = 1
                graph[l][k] = 1

colours = [0] * 20
chromaticNumber = 1

# racunanje kromatskog broja
while(graphColoring(graph, chromaticNumber, colours, 0, n) == False):
    chromaticNumber = chromaticNumber + 1

# ispis rjesenja
print("Kromatski broj zadanog grafa je", chromaticNumber)