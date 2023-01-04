def caesarCipherEncryptor(string, key):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    newKey = key % 26 # To wrap larger key value
    new_str = []

    for item in string:
        index = alphabet.index(item)
        new_char_index = index+newKey
        new_str.append(alphabet[new_char_index % 26])

    return ''.join(new_str)