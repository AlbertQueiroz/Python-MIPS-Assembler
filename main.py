from registersBank import reg
import labels
import functions

#READING ARCHIVE AND SAVING ON A LIST
archive = open('./exampleMipsCode.asm', 'r')

archiveList = archive.readlines()
archiveList = ('').join(archiveList)
archiveList = archiveList.split('\n')

lineCounter = 0

#WHILE THE LINE COUNTER IS DIFERENT FROM THE ARCHIVE LENGTH
while lineCounter != len(archiveList):

	#FORMATING LINE
	line = functions.breakline(archiveList[lineCounter])

	#PRINTING CURRENT LINE AND REGISTER BANK
	functions.printReg()
	functions.printMem()
	print("CURRENT LINE:\n",archiveList[lineCounter])
	
	
	#DELETING LABELS IDENTIFIERS
	if line[0].find(':') != -1:		
		del line[0]

	#INCREMENTING 'WHILE' COUNTER
	lineCounter += 1

	#FUNCT IDENTIFIER
	funct = line[0]

	#SELECTING FUNCTION
	if funct == 'add':
		#REGISTERS IDENTIFIERS
		reg1 = line[1]
		reg2 = line[2]
		reg3 = line[3]
		#ENTERING FUNCTION
		reg[reg1] = functions.add(reg[reg2], reg[reg3])
	elif funct == 'addi':
		#REGISTERS AND IMMEDIATE IDENTIFIERS
		reg1 = line[1]
		reg2 = line[2]
		immediate = line[3]
		#ENTERING FUNCTION
		reg[reg1] = functions.addi(reg[reg2], immediate)
	elif funct == 'j':
		label = line[1]
		#GOING BACK TO THE LINE WHERE THE LABEL STARTS
		lineCounter = functions.j(label)
	elif funct == 'beq':
		reg1 = line[1]
		reg2 = line[2]
		label = line[3]
		#GOING BACK TO THE LINE WHERE THE LABEL STARTS
		lineCounter = (functions.beq(reg[reg1],reg[reg2],label))
	elif funct == 'lw':
		line[2] = line[2].split('(')
		rt = line[1]
		rs = ('').join(line[2][1][0:3])
		immediate = line[2][0]
		reg[rt] = functions.lw(immediate, reg[rs])
	elif funct == 'sw':
		line[2] = line[2].split('(')
		rt = line[1]
		rs = ('').join(line[2][1][0:3])
		immediate = line[2][0]
		functions.sw(immediate, reg[rs], reg[rt])

functions.printReg()

archive.close()