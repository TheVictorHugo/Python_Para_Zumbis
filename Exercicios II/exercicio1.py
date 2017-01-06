'''
Faça um Programa que peça os três lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, 
se o mesmo é: equilátero, isósceles ou escaleno.
'''
x = int(input("Digite um lado: "))
y = int(input("Digite um outro lado: "))
z = int(input("Digite um outro lado: "))

if x > 0 and y > 0 and z > 0:
	print('E um triangulo')
	if x == y == z:
		print('Triangulo equilátero')
	elif x == y or y == z or x == z:
		print('Triangulo isóceles')
	elif x != y and y != z and x != z:
		print("Triangulo Escaleno")

else:
	print('As medidas não formão um triangulo')