#Ordem Precêdencia
#1 - ()
#2 - **
#3 - * / // %
#4 - + -

# nome = str(input('Qual é o seu nome? '))
# print('Prazer em te conhecer {:>20}!'.format(nome))
# print('Prazer em te conhecer {:<20}!'.format(nome))]
# print('Prazer em te conhecer {:^20}!'.format(nome))
# print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, o produto é {} e a divisão é {:.3f}'.format(s,m,d), end=' ')
print('Divisão inteira {} \nE a potência {}'.format(di,e))

