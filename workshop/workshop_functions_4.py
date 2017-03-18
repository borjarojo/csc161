from math import pi

def sphereArea(radius):
	return 4 * pi * radius**2

def sphereVolume(radius):
	return (4 / 3) * pi * radius**3

def main():
	for i in range(10):
		print(sphereVolume(i))

main()
