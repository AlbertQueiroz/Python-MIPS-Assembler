from registersBank import reg
import dataMemory
import labels

#FORMAT FUNCTIONS
def breakline(s):
	s = s.split(',')
	s = ('').join(s)
	s = s.split()
	return s

def printReg ():
	print('================Registers==================')
	for items in reg:
   		print(items, ' = ', reg[items])
	print('================Registers==================')

def printMem():
	print("DATA MEMORY: ",dataMemory.mem)

#MIPS FUNCTIONS
def add (reg1, reg2):
    return reg1 + reg2

def addi (reg, immediate):
	return int(reg) + int(immediate)

def j(label):
	return labels.labels[label+':']

def beq (reg1, reg2, label):
	if reg1 == reg2:
		return j(label)

def lw(immediate, rs):
	adr = int(immediate) + int(rs)
	dataMemory.pc += 4
	return dataMemory.mem[adr]

def sw(immediate, rs, rt):
	adr = int(immediate) + int(rs)
	dataMemory.mem[adr] = rt
	dataMemory.pc += 4
