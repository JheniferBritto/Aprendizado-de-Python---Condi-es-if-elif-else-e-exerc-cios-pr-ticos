produto = int(input('Qual é a quantidade de produto comprado?'))
if produto < 0:
    print('Nenhum produto comprado')
elif produto  <=5:
    print('Compra pequena')
else:
    print('Compra grande')