ingresso = int(input('Digite a quantidade de ingressos que deseja comprar: '))
if ingresso < 0:
    print('Quantidade inválida')
elif ingresso == 0:
    print('Nenhum ingresso selecionado')
elif ingresso <=3:
    print('Compra pequena')
else:
    print('Compra grande')