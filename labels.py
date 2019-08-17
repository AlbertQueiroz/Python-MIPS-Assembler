import functions

archive = open('./exampleMipsCode.asm', 'r')

#STORING LABELS TITLES AND LINE NUMBERS
labels = {}
labelsCount = 0

archiveList = archive.readlines()
archiveList = ('').join(archiveList)
archiveList = archiveList.split('\n')

for x in range(len(archiveList)):
	labelsCount += 1
	line = functions.breakline(archiveList[x])
	if line[0].find(':') != -1:
		labels[line[0]] = labelsCount		
		del line[0]
archive.close()