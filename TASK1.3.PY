from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Read the original image
with open('E:/COPIED FROM E/Desktop/python files/ciphers/pic_original.bmp', 'rb') as f:
    original_content = f.read()

# Extract the header and the image data
header = original_content[:54]
image_data = original_content[54:]

# Encryption key and IV
key = b'abcdefghijklmnop'  # 16 bytes key
iv = b'1234567890abcdef'  # 16 bytes Initialization Vector

# Encrypt using ECB
cipher_ecb = AES.new(key, AES.MODE_ECB)
cipher_ecb_text = cipher_ecb.encrypt(pad(image_data, 16))

# Encrypt using CBC
cipher_cbc = AES.new(key, AES.MODE_CBC, iv=iv)
cipher_cbc_text = cipher_cbc.encrypt(pad(image_data, 16))

# Save the ECB encrypted image
with open('pic_ecb_encrypted.bmp', 'wb') as f:
    f.write(header + cipher_ecb_text)

# Save the CBC encrypted image
with open('pic_cbc_encrypted.bmp', 'wb') as f:
    f.write(header + cipher_cbc_text)
