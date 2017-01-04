'''
Pergunte a velociade de um carro, supondo um valor inteiro.
Caso ultrapasse 110 km/h, exiba uma mensagem dizendo que o usuário foi multado.
Neste caso, exiba o valor da multa, cobrando R$ 5,00 km acima de 110
'''

x =int(input('Digite a velocidade de um carro: '))

if x > 110:
	print('Receberar multa')
	cal = x - 110
	cal2 = cal * 5
	print('será multadodo com taxa de : %i R$' %cal2)
else:
	print('Não receberar multa')