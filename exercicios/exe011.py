# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pinta-la. Sabendo que casa litro de tinta pinta uma área de 2m².

print('===== DESAFIO 11 =====\n')

parede_altura = float(input('Altura da parede: '))
parede_largura = float(input('Largura da parede: '))

print(f'Area da parede é: {parede_altura * parede_largura}m e serão necessários '
      f'{((parede_altura * parede_largura) / 2):.2f} litros de tinta para pintar, visto que a cada litro, pitamos '
      f'2 metros de parede.')
