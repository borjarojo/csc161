def main():
	output = open("file.txt", "w")
	for i in range(10):
		output.write(str(i) + "\n")

	output.close()

main()