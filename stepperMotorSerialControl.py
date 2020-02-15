import serial
import time
import struct

#team written module
import LineAlg as lineAlg
import resizeImage as resizeImage

currX = 0
currY = 0

test = True

if (not test):
	serialData = serial.Serial('/dev/tty.usbmodem1421', baudrate=9600)
time.sleep(2) # wait for intialize

# resizeImage.resize("test.jpeg")

def drawLine(nextX, nextY):
	global currX
	global currY
	instructions = lineAlg.drawLine(currX, currY, nextX, nextY)
	currX = nextX
	currY = nextY
	for instruct in instructions:

		#str_pass = b''
		#str_pass += struct.pack('!B',instruct)
		chrPass = ''
		if (instruct == 0):
			chrPass = '0'
		if (instruct == 1):
			chrPass = '1'
		if (instruct == 2):
			chrPass = '2'
		if (instruct == 3):
			chrPass = '3'
		if (not test):
			serialData.write(str(chrPass).encode())
		time.sleep(0.09)
		print(chrPass)
		#serialData.write(str.encode(chrInterp))
		#serialData.write(struct.pack(">ii",instruct,1));



# print("---" , str(currX) + "," + str(currY))
# drawLine(5,0)
# print("---" , str(currX) + "," + str(currY))
# drawLine(5,5)
# print("---" , str(currX) + "," + str(currY))
# drawLine(0,0)
# print("---" , str(currX) + "," + str(currY))

def testLine(x, y):
	if currY == 0 and currX == 0:
		print("---" , str(currX) + "," + str(currY))

	drawLine(x,y)
	print("---" , str(currX) + "," + str(currY))
