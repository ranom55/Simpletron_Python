READ = 10
WRITE = 11
LOAD = 20
STORE = 21
ADD = 30
SUBTRACT = 31
DIVIDE = 32
MULTIPLY = 33
MODULOS = 34
BRANCH = 40
BRANCHNEG = 41
BRANCHZERO = 42
HALT = 43
arq_name = input("Digite o nome do arquivo: ")
try:
    file = open(arq_name, "r")
except FileNotFoundError:
    print("No such file or directory:", arq_name)
    exit(0)
data = file.readlines()
file.close()
variables = []
accumulator = 0
i = 0
for z in range(99):
    variables.insert(0, 0)

print("***RUNNING THE PROGRAM***")
while i < len(data):
    operationCode = int(data[i]) // 100
    operand = int(data[i]) % 100

    if operationCode == READ:
        variables.insert(operand, float(input("Valor: ")))
    if operationCode == WRITE:
        print(variables[operand])
    if operationCode == ADD:
        accumulator += variables[operand]
    if operationCode == SUBTRACT:
        accumulator -= variables[operand]
    if operationCode == MULTIPLY:
        accumulator *= variables[operand]
    if operationCode == DIVIDE:
        if accumulator != 0 and variables[operand] != 0:
            accumulator /= variables[operand]
        else:
            print("***Error: DIVISION BY ZERO***\n***BAD HALTING***")
    if operationCode == MODULOS:
        accumulator %= variables[operand]
    if operationCode == BRANCH:
        if (operand < len(data) - 1):
            i = operand
            continue
    if operationCode == BRANCHZERO:
        if (operand < len(data) - 1) and accumulator == 0:
            i = operand
            continue
    if operationCode == BRANCHNEG:
        if (operand < len(data) - 1) and accumulator < 0:
            i = operand
            continue
    if operationCode == LOAD:
        accumulator = variables[operand]
    if operationCode == STORE:
        variables[operand] = accumulator
    if operationCode == HALT:
        print("***SHUTTING DOWN***")
        break

    i += 1