
nota = float(input('informe uma nota entre 0 e 10:  '))

while nota <= 0 or nota >= 10:
    nota = float(input('Número inválido. favor informar entre 0 e 10:  '))
print (f'você escolheu a nota {nota}')
