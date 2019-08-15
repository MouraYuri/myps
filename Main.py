from reg import registers
from dataMemory import dMem as dataMemory
manipuladorIL = open('input', 'r')
instructionList = manipuladorIL.readlines()

manipuladorReg = open('registers', 'r')
regs = manipuladorReg.readlines()


instructionsVector = ['add', 'addi', 'lw', 'j', 'beq'] #instruções aceitas
instructionIndexRI = [0, 1, 2] #Index das instruções do tipo R e I
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
        ctrl = labels[instructionLine[1]]
    if (instructionIndex == 4):
        if (registers[instructionLine[1]] == registers[instructionLine[2]]):
            ctrl = labels[instructionLine[3]]
        else:
            ctrl = lineRead
    return ctrl

while (True):
    print(instructionList[lineRead])
    instructionLine = instructionList[lineRead].split(' ')
    if (len(instructionLine) != 1):
        for x in instructionsVector:
            if(instructionLine[0] == x):
                instructionIndex = instructionsVector.index(x)
                break
        if (instructionIndex in instructionIndexRI):
            registers[instructionLine[1]] = executeRI(instructionLine, registers, instructionIndex, dataMemory)
        if(instructionIndex in instructionIndexBranchs):
            lineRead = executeBranchs(labels,instructionIndex,instructionLine,lineRead,registers)

    else:
        keyToBeStored = instructionLine[0]
        keyToBeStored = keyToBeStored[:3]
        labels[keyToBeStored] = lineRead




    for z in registers:
        print('{} -> {}'.format(z, hex(registers[z])))
    lineRead += 1
    if (lineRead >= len(instructionList)):
        break
    input('Pressione qualquer tecla para pular para próxima iteração')