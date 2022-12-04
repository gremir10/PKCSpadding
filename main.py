"""CryptoPals set 2, challenge #9 :
 pad any block to a specific block length, by appending the number of bytes of padding to the end of the block.
 For instance,

"YELLOW SUBMARINE"
... padded to 20 bytes would be:

"YELLOW SUBMARINE\x04\x04\x04\x04"""

def pkcs7_padding(plainText, key):
    if key > len(plainText):
        padding_amount = key - len(plainText) % key
    else:
        padding_amount = 0
    return bytes(plainText.encode()) + (chr(padding_amount) * padding_amount).encode()

if __name__ == "__main__":
    input_text = input("Enter text to apply PKCS#7 padding to:")
    pad_amount = int(input("Enter number of bytes to pad text to:"))
    print(pkcs7_padding(input_text, pad_amount))

