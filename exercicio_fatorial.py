#calcule o fatoril de dez

i = 1
fat = 1
n = int(input('Digite um número: '))

while i <= n:
	fat = fat * i
	i = i + 1
print(fat)