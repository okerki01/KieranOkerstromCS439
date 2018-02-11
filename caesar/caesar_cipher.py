'''Caesar cipher'''
#!/usr/bin/env python3
#encoding: UTF-8

with open("wordlist_english.txt", 'r', encoding="utf-8") as file_in:
    DICT_ENG = file_in.read().lower()     

def shift_by_n(word: str, shift: int, direction: int) -> str:
    decryption = ''
    
    for letter in word:
        if ord(letter) == 32:
            decryption = decryption + ' '
        elif ord(letter) == 44:
            decryption = decryption + ','
        elif ord(letter) == 44:
            decryption = decryption + ','
        else: 
            newletterval = ord(letter)
            for i in range(shift):
                if direction == 1:
                    newletterval += 1
                    if newletterval == 91:
                        newletterval = 65
                else:
                    newletterval -= 1
                    if newletterval == 91:
                        newletterval = 65                    
            
            decryption = decryption + chr(newletterval)
    
    return decryption

def encrypt(plaintext: str, shift: int, obfuscate=False) -> str:
    '''Encrypt and optionally obfuscate a string'''
    cipher = shift_by_n(plaintext, shift, 1).upper()  # 1 for encryption
    if obfuscate:
        punctuation = ";:,.!?'() \n\t"
        for symbol in punctuation:
            cipher = cipher.replace(symbol, '')
    return cipher

def encrypt_file(file_in_name: str, file_out_name: str, shift: int, obfuscate=False):
    '''Encrypt a file and write the cipher to a file'''
    with open(file_in_name, 'r', encoding="utf-8") as file_in:
        plaintext = file_in.read().lower()
    cipher = encrypt(plaintext, shift, obfuscate)
    with open(file_out_name, 'w', encoding="utf-8") as file_out:
        file_out.write(cipher)

def decrypt(cipher: str, shift: int) -> str:
    
    return shift_by_n(cipher, shift, 1)

def decrypt_file(file_in_name: str, file_out_name: str, shift: int):
    '''Decrypt a file that has not been obfuscated'''
    with open(file_in_name, 'r', encoding="utf-8") as file_in:
        cipher = file_in.read()
    plaintext = decrypt(cipher, shift)
    with open(file_out_name, 'w', encoding="utf-8") as file_out:
        file_out.write(plaintext)

def analyze_file(file_in_name: str, file_out_name: str, dictionary: set):
    with open(file_in_name, 'r', encoding="utf-8") as file_in:
        encString = file_in.read()
    
    for length in range(4,10):
        encWord = encString[0:length]
        for numShift in range(26):
            newWord = shift_by_n(encWord, numShift, 1)
            lowerNewWord = newWord.lower()
            if lowerNewWord in dictionary:
                print("the word " + newWord + " was found with a shift of " + str(numShift))
            

def main():
    decrypt_file('cipher_1.txt', 'plaintext_1.txt', 6)
    analyze_file('cipher_2.txt', 'plaintext_2.txt', DICT_ENG)
    decrypt_file('cipher_2.txt', 'plaintext_2.txt', 8)
    #print('---Over and out---')

if __name__ == '__main__':
    main()
