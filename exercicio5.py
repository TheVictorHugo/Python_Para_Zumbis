'''
Solicite o preço de uma mercadoria e o percentual de desconto. 
Exiba o valor do desconto e o preço a pagar.
'''
x = int(input('Digite o preco da mercadoria: '))
y = int(input('Digite o percentual de desci=onto: '))

d = x * (y/100)
p = x - d

print('O novo preco da mercadoria é: %i' %p)