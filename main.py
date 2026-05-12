from cipher import shifr, deshifr


alf_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alf_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


print('=' * 57)
print('Программа шифрования и дешифрования текста (шифр Цезаря)')
print('=' * 57)

choose = input('Что вы хотетите сделать шифрование/дешифрование: ')


if choose == 'шифрование':
    shifr(alf_EN, alf_RU)
else:
    deshifr(alf_EN, alf_RU)