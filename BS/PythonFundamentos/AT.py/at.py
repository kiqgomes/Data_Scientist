from datetime import date, datetime

import colorama

# A variável "hoje" contém a data de hoje.
# Para o dia do mês, use:  hoje.day
# Para o mês, use:         hoje.month
# Para o ano, use:         hoje.year
hoje = date.today()

name_list = ['Kaique', 'Kaique', 'Kaique']
surname_list = ['Gomes', 'Viana', 'Gomes']
cpf_list = ['11111111111', '11111111111', '11111111111']
birth_list = ['24/09/2002', '24/09/2002', '24/09/2002']


# Perdão por fazer dessa forma, porém a vida ta lotada de coisas e eu não conseguiria entregar.
def age_days(date_birth: int):
    """
    Def to calc the age days of a person
  """
    diff = hoje - datetime.strptime(date_birth, '%d/%m/%Y').date()
    return diff.days


while True:
    print(" Welcome ".center(50, '*'))
    print("Type some number to continue\n".center(50, ' '))
    print('1.Inserir novo cadastro\n')
    print('2.Alterar CPF\n')
    print('3.Trocar sobrenomes\n')
    print('4.Remover cadastro\n')
    print('5.Listar todos os cadastros\n')
    print('6.Encerrar\n')
    opc = input("Your choice: ")

    # Bloco de escolhas
    if opc == '1':
        name = input("Type your Name and Surname (ex: Kaique Gomes): ").split(
            ' ')
        if len(name) != 2:  # Validação da entrada de nome
            print(colorama.Fore.RED + "Name different that specified")
            break
        else:
            name_list.append(name[0].title())
            surname_list.append(name[1].title())
        cpf = input("Type your CPF (Just numbers): ")
        if len(cpf) != 11:  # Validação da entrada de CPF
            print(colorama.Fore.RED + "CPF different than 11 digits")
            break
        else:
            cpf_list.append(cpf)
        birth_list.append(input("Type your date of birth (ex: 24/09/2002): "))
        print(colorama.Fore.GREEN + "Success!!\n" + colorama.Style.RESET_ALL)
    elif opc == '2':
        cpf_list[int(
            input('Person id that you want to change the CPF: '))] = input(
                'New CPF: ')  # Entrada de um novo CPF
    elif opc == '3':  # Troca de sobrenomes
        id1 = int(input('Person one ID: '))
        id2 = int(input('Person two ID: '))
        tmp = surname_list[id1]
        surname_list[id1] = surname_list[id2]
        surname_list[id2] = tmp
    elif opc == '4':  # Bloco de deleção
        id = int(input('Person ID to delete: '))
        if id < len(name_list):  # Validação do input de id para deleção
            del name_list[id]
            del surname_list[id]
            del cpf_list[id]
            del birth_list[id]
        else:
            print(colorama.Fore.RED + "ID don't exists")
    elif opc == '5':  # Print de todos os itens e com o bloco de dias.
        for n, s, c, b in zip(name_list, surname_list, cpf_list, birth_list):
            print(
                f'Nome: {n} {s} ; CPF: {c} ; Birth Date: {b}; Age in Days: {age_days(b)}'
            )
        print('\n')
    elif opc == '6':
        break
