# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Acima da média - Unidade 5

media_estabelecida = float(raw_input())
lista = []

while True:
	media = 0.0
	lista_aux = []
	valores_dia = str(raw_input()).split()
	
	if valores_dia[0] == 'fim': break
	
	for i in range(len(valores_dia)):
		media += float(valores_dia[i])
		lista_aux.append(valores_dia[i])
	
	media /= len(valores_dia)

	if media * 2 < media_estabelecida: break
	if media > media_estabelecida:
		lista.append(lista_aux)

for i in range(len(lista)):
	saida = ''
	
	for c in range(len(lista[i])):
		if c == len(lista[i])-1:
			saida += str(lista[i][c])
		else:
			saida += str(lista[i][c]) + ' '
	
	print saida
