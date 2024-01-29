# Steganography

The hiding of information in an image is called steganography.

In this we are first reading the binary data present in the input image and assigning it to to a bytearray. Since we are directly working on the binary data present in the image it would be easier to work with an bytearray.Here we are asking the user to input a key and performing XOR operation on the bytearray and writing this data to a new file which is the new encrypted image.For decryprting this we need to change the input file as encrypted image and enter the key which gives the original image back. Remember the point that performing XOR operations even number of times doesn't change the data 
