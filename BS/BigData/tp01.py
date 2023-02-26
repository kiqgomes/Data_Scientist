# Realize operações matemáticas em Python.
# Desenvolva o programa Python utilizando diversos tipos de dados.
# Utilize o recurso de concatenação de String e formatação do Python.

import sys

num_1 = float(sys.argv[1])
num_2 = float(sys.argv[2])
name = sys.argv[3]


print('Hey' , name)
print('Your numbers ' + str(num_1) + ' and ' + str(num_2))
print(f'\nSum -> {(num_1+num_2):.0f}\
    \nSub -> {num_1-num_2}\n\
    Mult -> {num_1*num_2}\n\
    Div -> {(num_1/num_2 if num_1 != 0 else num_2/num_1):.2f}\n')
