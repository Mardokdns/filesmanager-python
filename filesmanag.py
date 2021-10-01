#Program created by Mardok Security

import os

print('''
[1] Criar arquivo.
[2] Deletar arquivo.
[3] Ler arquivo.
[4] Escrever dentro de um arquivo.
''')

method = input('O que deseja fazer? ')

if method == '1':
    file_name = input('Nome do arquivo: ')
    file = open(f'{file_name}', 'a')
    print(f'Arquivo {file_name} criado.')
elif method == '2':
    file_name = input('Nome do arquivo: ')
    if os.path.exists(f'{file_name}'):
        os.remove(f'{file_name}')
        print(f'Arquivo {file_name} deletado.')
    else:
        print(f'O arquivo {file_name} não existe.')
elif method == '3':
    file_name = input('Nome do arquivo: ')
    if os.path.exists(f'{file_name}'):
        file = open(f'{file_name}', 'r')
        lines = [1,2,3,4,5,6,7,8,9,10]
        for i in lines:
            print(f'{file.readlines(i)}')
elif method == '4':
    file_name = input('Nome do arquivo: ')
    if os.path.exists(f'{file_name}'):
        file = open(f'{file_name}', 'a')
        line_string = input('O que deseja escrever?\nR: ')
        file.write(f'{line_string}')
else:
    print('Esta opção não existe.')
    exit()