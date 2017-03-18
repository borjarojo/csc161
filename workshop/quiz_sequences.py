#Quiz stuff

#1.
s1 = "Live long"
s2 = "and prosper!"

def ai():
	print(s1 + s1[4] + s2)

def aii():
	print("Peace " + s2[0:3] + s2[3] + s1[5:9] + " life" + s2[-1])

def aiii():
	print(s1[:4] + "," + s2[3] + "be" + s1[4] + s2[4:-1] + "ous.")

def aiv():
	a = s1.split()
	print(a)
	b = s2.split()
	print(b)
	c = a + b
	print(c)

def bi():
	print("7" - ord("3"))

def bii():
	print("W" + "O" * 4 + "!")

def main():
	ai()
	aii()
	aiii()
	aiv()
	bi()
	bii()

main()