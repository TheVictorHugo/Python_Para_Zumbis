'''
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
total de dias.
'''

x = int(input('Digite a quantidade de cigarros fumados por dia: '))
y = int(input('Digite quantos anos que fuma: '))

cal = x * (y * 365)

cal2 = cal / 10

print("A pessoa tem %f minuto de vida ", cal2)