print('Verificando a média das notas')
media = 0
for i in range(1,4):
    nota = float(input(f'Qual a {i}ª nota? '))
    media += nota
    media_total = media / 3
    
if media_total >= 7:
    print(f'Parabens, você foi aprovado! Sua media {round(media_total,2)}')
elif media_total <= 7:
    print(f'Você está de recuperação! Sua media {media_total:.2f}')
else:
    print(f'Você foi reprovado! Sua media {round(media_total,2)}')
    

    