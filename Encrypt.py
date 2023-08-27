file = open('Image.jpg',"rb")

image = file.read()
file.close()

image  = bytearray(image)

key=int(input("Enter a Key: "))

for i,j in enumerate(image):
    image[i] = j^key


file = open("encrypted.jpg","wb")
file.write(image)
file.close()