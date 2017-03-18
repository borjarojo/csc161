def main():
	inFile = open("inFile.txt", "r")
	lines = inFile.readlines()
	lines.reverse()
	outFile = open("outFile.txt", "w")
	for i in lines:
		outFile.write(i)

main()
