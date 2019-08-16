from reg import registers
from dataMemory import dMem as dataMemory
manipuladorIL = open('input', 'r')
instructionList = manipuladorIL.readlines()

manipuladorReg = open('registers', 'r')
regs = manipuladorReg.readlines()


instructionsVector = ['add', 'addi', 'lw', 'j', 'beq', 'sw'] #instruções aceitas
instructionIndexRI = [0, 1, 2, 5] #Index das instruções do tipo R e I
instructionIndexBranchs = [3, 4]
labels = {}

lineRead = 0

def executeRI(instructionLine, registers, instructionIndex, dataMemory):

    if (instructionIndex == 1):
        ctrl = registers[instructionLine[2]] + (int(instructionLine[3]))
    if (instructionIndex == 0):
        ctrl = registers[instructionLine[2]] + registers[instructionLine[3]]
    if (instructionIndex == 2):
        loadedWord = instructionLine[3]
        loadedWord = loadedWord[1:3]
        loadedWord = registers[loadedWord]
        loadedWord = loadedWord + int(instructionLine[2])
        print('loadedWord = {}'.format(loadedWord))
        ctrl = dataMemory[loadedWord][0]


    return ctrl
def executeBranchs(labels,instructionIndex,instructionLine,lineRead,registers):
    if(instructionIndex == 3):
        print(instructionLine[1])
        keyStr = instructionLine[1]
        keyStr = keyStr[:-1]
        keyToBeStored = keyStr
        ctrl = labels[keyStr]
    if (instructionIndex == 4):
        if (registers[instructionLine[1]] == registers[instructionLine[2]]):
            keyStr = instructionLine[3]
            keyStr = keyStr[:-1]
            ctrl = labels[keyStr]
        else:
            ctrl = lineRead
    return ctrl

def executeSw(instructionLine, registers, instructionIndex, dataMemory):
    adress = instructionLine[3]
    adress = adress[1:3]
    adress = registers[adress]
    adress = adress + int(instructionLine[2])
    content = registers[instructionLine[1]]
    return [adress, content]

lineRead = 0
while (True):
    if (lineRead == len(instructionList)):
        break
    instructionLine = instructionList[lineRead].split(' ')
    if (len(instructionLine) == 1):
        keyStr = instructionLine[0]
        keyStr = keyStr[:-2]
        keyToBeStored = keyStr
        labels[keyToBeStored] = lineRead
    lineRead+=1

print(labels)
lineRead = 0
while (True):
    print(instructionList[lineRead])
    instructionLine = instructionList[lineRead].split(' ')
    if (len(instructionLine) != 1):
        for x in instructionsVector:
            if(instructionLine[0] == x):
                instructionIndex = instructionsVector.index(x)
                break
        if (instructionIndex in instructionIndexRI):
            if (instructionIndex != 5):
                registers[instructionLine[1]] = executeRI(instructionLine, registers, instructionIndex, dataMemory)
            else:
                ctrlVector = executeSw(instructionLine, registers, instructionIndex, dataMemory)
                dataMemory[ctrlVector[0]][0] = ctrlVector[1]

        if(instructionIndex in instructionIndexBranchs):
            lineRead = executeBranchs(labels,instructionIndex,instructionLine,lineRead,registers)



    for z in registers:
        print('{} -> {}'.format(z, hex(registers[z])))
    lineRead += 1
    if (lineRead >= len(instructionList)):
        break
    input('Pressione qualquer tecla para pular para próxima iteração')