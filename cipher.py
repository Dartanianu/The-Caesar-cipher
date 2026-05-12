alf_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alf_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def shifr(alf_EN, alf_RU):
    lang = input('Выберите язык RU/EN: ')

    mes = input('Введите сообщение: ').upper()
    while any(c.isdigit() for c in mes):
        print('Ошибка! Сообщение не должно содержать цифры.')
        mes = input('Введите сообщение: ').upper()

    smesh = int(input('Введите параметр сдвига: '))
    end = ''

    if lang == 'RU':
        for i in mes:
            mesto = alf_RU.find(i)
            new_mesto = mesto + smesh
            if i in alf_RU:
                end += alf_RU[new_mesto]
            else:
                end += i
    else:
        for i in mes:
            mesto = alf_EN.find(i)
            new_mesto = mesto + smesh
            if i in alf_EN:
                end += alf_EN[new_mesto]
            else:
                end += i
    print(end)


def deshifr(alf_EN, alf_RU):
    lang = input('Выберите язык RU/EN: ')

    mes = input('Введите сообщение: ').upper()
    while any(c.isdigit() for c in mes):
        print('Ошибка! Сообщение не должно содержать цифры.')
        mes = input('Введите сообщение: ').upper()

    smesh = int(input('Введите параметр сдвига: '))
    end = ''

    if lang == 'RU':
        for i in mes:
            mesto = alf_RU.find(i)
            new_mesto = mesto - smesh
            if i in alf_RU:
                end += alf_RU[new_mesto]
            else:
                end += i
    else:
        for i in mes:
            mesto = alf_EN.find(i)
            new_mesto = mesto - smesh
            if i in alf_EN:
                end += alf_EN[new_mesto]
            else:
                end += i
    print(end)
