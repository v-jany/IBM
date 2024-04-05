import cv2
import os

img = cv2.imread("mypic.jpg")

msg = input("Enter secret message: ")
password = input("Enter password: ")

d = {}
C = {}

for i in range(255):
    d[chr(i)] = i
    C[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    m += 1
    if m == img.shape[1]:
        m = 0
        n += 1
        if n == img.shape[0]:
            n = 0
            z = (z + 1) % 3

cv2.imwrite("EncryptedImage.jpg", img)
os.system("start EncryptedImage.jpg")

message = ""
n = 0
m = 0
z = 0

pas = input("Enter password for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        message = message + C[img[n, m, z]]
        m += 1
        if m == img.shape[1]:
            m = 0
            n += 1
            if n == img.shape[0]:
                n = 0
                z = (z + 1) % 3

    print("Decrypted message:", message)
else:
    print("Not a valid key")
               
