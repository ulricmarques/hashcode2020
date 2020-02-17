def solve(M, N, slices):

    total = 0
    pizzasToOrder = []

    for i in range(N - 1, -1, -1):
        if total + slices[i] <= M:
            total += slices[i]
            pizzasToOrder.append(i)

        if total == M:
            break

    pizzasToOrder.reverse()

    return pizzasToOrder


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