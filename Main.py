#
#
#
#

from reg import registers

manipuladorIL = open('input', 'r')
instructionList = manipuladorIL.readlines()

manipuladorReg = open('registers', 'r')
regs = manipuladorReg.readlines()

#print(registers)

instructionsVector = ['add', 'addi', 'lw', 'j', 'beq']

PC = hex(0)
lineRead = 0

def execute(instructionLine, registers, instructionIndex):

    if (instructionIndex == 1):
        ctrl = registers[instructionLine[2]] + (int(instructionLine[3]))


    return ctrl



while True:
    print(instructionList[lineRead])
    instructionLine = instructionList[lineRead].split(' ')
    print('InstructionLine = {}'.format(instructionLine))
    for x in instructionsVector:
        if (instructionLine[0] == x):
            instructionIndex = instructionsVector.index(x)
            break
    print('Index of Instruction = {}'.format(instructionIndex))
    registers[instructionLine[1]] = execute(instructionLine,registers, instructionIndex)

    print(registers)
    break
    lineRead += 1
    if (lineRead >= len(instructionList)):
        break