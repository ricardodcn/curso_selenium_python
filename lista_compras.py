lista_compras = []
resposta = ''

while resposta !='acabou':
    resposta = input ('Preencha a sua lista de compras:  ')
    if resposta != 'acabou':
        lista_compras.append(resposta)
print (lista_compras)
