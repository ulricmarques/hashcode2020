def solve(m, n, slices):

    total = 0
    pos = []

    for i in range(n - 1, -1, -1):
        if total + slices[i] <= m:
            total += slices[i]
            pos.append(i)

        if total == m:
            break

    pos.reverse()

    return pos


def process(fileName):

    inputFile = open("inputs/"  + fileName + ".in", "rt")

    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()

    M, N = list(map(int, firstLine.split()))

    slices = list(map(int, secondLine.split()))

    pizzasToOrder = solve(M, N, slices)  

    parsedOutputString = ""
    for pizza in pizzasToOrder:
        parsedOutputString = parsedOutputString + str(pizza) + " "
       
    outputFile = open("outputs/" + fileName + ".out", "w")
    outputFile.write(str(len(pizzasToOrder)) + "\n")
    outputFile.write(parsedOutputString)
    outputFile.close()


files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]

for file in files:  
    process(file)