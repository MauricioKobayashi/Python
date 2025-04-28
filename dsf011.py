l=float(input('Insira a largura em metros da parede: '))
a=float(input('Insira a altura em metros da parede: '))
area = l * a
tinta = area / 2
print('Parede de {} metros de largura e {} metros de altura:\nArea={}\nQuantidade de tinta={} litros'.format(l,a,area,tinta))