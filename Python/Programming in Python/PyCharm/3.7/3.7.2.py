'''
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита,
на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом,
и ещё одна строка, которую нужно расшифровать.
----------------------
Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%
----------------------
Sample Output 1:
*d*%*d*#*d*
dacabac
----------------------
'''

#Функция создает словарь шифрования (на вход принимает строку и ее шифр)
def creat_dictionary(letters, substitute):
    dictionary = {}
    count = len(letters)
    for i in range(count):
        dictionary[letters[i]] = substitute[i]
    return dictionary

#Функция зашифровки (принимает слово для зашифровки и словарь для шифровки)
def encrypt(line_for_encrypt, dictionary):
    encrypted_line = ''
    for symbol in line_for_encrypt:
        encrypted_line += dictionary[symbol]
    return encrypted_line

#Функция для расшифровки (принимает слово для расшифровки и словарь для расшифровки)
def decode(line_for_decode, dictionary):
    decoded_line = ''
    for symbol in line_for_decode:
        for i in dictionary:
            if symbol == dictionary[i]:
                decoded_line += i
    return decoded_line


letters = input()
substitute = input()
line_for_encrypt = input()
line_for_decode = input()

dictionary_for_encryption = creat_dictionary(letters, substitute) #Создания словаря шифрования

print(encrypt(line_for_encrypt, dictionary_for_encryption))
print(decode(line_for_decode, dictionary_for_encryption))
