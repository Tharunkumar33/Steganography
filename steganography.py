import cv2
import os

img_path = "mypic.jpg"
img = cv2.imread(img_path).copy()

msg = input("Enter secret message: ")
password = input("Enter password: ")

if len(password) == 0 or len(msg) == 0:
    print("No password or message provided.")
    exit()


encrypted_msg = [ord(char) ^ ord(password[i % len(password)]) for i, char in enumerate(msg)]
for i, val in enumerate(encrypted_msg):
    img[0, i, 2] = val


encrypted_img_path = "Encryptedmsg.jpg"
cv2.imwrite(encrypted_img_path, img)
os.startfile(encrypted_img_path)


input_password = input("Enter password for Decryption: ")

if password == input_password:

    decrypted_msg = [chr(img[0, i, 2] ^ ord(password[i % len(password)])) for i in range(len(encrypted_msg))]
    print("Decrypted message: ", ''.join(decrypted_msg))
else:
    print("Invalid password")
