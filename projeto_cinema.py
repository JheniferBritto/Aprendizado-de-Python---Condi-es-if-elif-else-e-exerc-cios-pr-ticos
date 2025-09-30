print('Sistema de Classificação de Cinema')

nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))


if idade <= 12:
    print(f'{nome} sua entrada é gratuita!')
elif idade <= 17:
    print(f'{nome} pagará meia entrada')
elif idade <= 59:
    print(f'{nome} pagará inteira')
else:
    print(f'{nome} pagará meia entrada')
    
quantidade = int(input('Quantos ingressos você deseja comprar? '))

if quantidade  <= 0:
    print(f' {nome},  nenhum ingresso selecionado')
elif quantidade  <= 3:
    print(f'{nome}, a compra é  pequena')
else:
    print(f'{nome} a compra é  grande')

estudante = input('Você é estudante? (sim/não) ').strip().lower()

if estudante == 'sim':
    print(f' {nome} , você vai recebe 50% de desconto.')
else: 
    print( f' {nome}  , você não recebe desconto.')

print('Obrigado por usar o sistema de classificação de cinema!')



