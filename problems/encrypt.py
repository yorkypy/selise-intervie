#Encryption
import string

def encrypt(plain_text, n):
    alphabets = list(string.ascii_lowercase)
    encrypted=[]
    for i in plain_text:
        if n>0:
            char_index=alphabets.index(i)
            char_index+=n
            charAt=alphabets[char_index]
            encrypted.append(charAt)
        elif n<0:
            char_index=alphabets.index(i)
            char_index-=n
            charAt=alphabets[char_index]
            encrypted.append(charAt)
        else:
            print('Not encrypetd')
            break
    return ''.join(encrypted)

        

#Solution II
def shift_n(char, n):
    if char not in string.ascii_lowercase:
        return char
    new_char = ord(char)+n
    while new_char > ord("z"):
        new_char -= 26
    while new_char < ord("a"):
        new_char += 26
    return chr(new_char)

def enCrypt(message, n):
    enc_list = [shift_n(char, n) for char in message]
    return ''.join(enc_list)

#Driver Code
if __name__ == "__main__":
    print(encrypt('abcd',2))
    print(enCrypt('ddd', -3))

