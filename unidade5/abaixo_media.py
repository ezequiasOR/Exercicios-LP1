# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Abaixo da média - Unidade 5

media = 0.0
cont = 0
lista_valores = []

while True:
	valor = str(raw_input())
	if valor == 'fim': break
	media += int(valor)
	cont += 1
	lista_valores.append(int(valor))

media /= cont

print '%.2f' % media

for i in range(len(lista_valores)):
	if lista_valores[i] < media:
		print '%d %d' % (i+1, lista_valores[i])
