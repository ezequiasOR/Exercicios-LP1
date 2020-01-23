# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Acima do Limite - Unidade 5

limite = int(raw_input())
lista_maior = []

while True:	
	soma = 0
	lista_secundaria = []
	valores = str(raw_input()).split()
	
	if valores[0] == '-': break
	
	for i in range(len(valores)):
		soma += int(valores[i])
		lista_secundaria.append(valores[i])
	
	if soma >= limite:	
		lista_secundaria.append(soma)
		lista_maior.append(lista_secundaria)
	
	if soma > (5 * limite): break

for i in range(len(lista_maior)):
	sequencia = ''
	
	for c in range(len(lista_maior[i])):
		
		if c == len(lista_maior[i])-2:
			sequencia += str(lista_maior[i][c]) + ' ' + '=' + ' '
		elif c == len(lista_maior[i])-1:
			sequencia += str(lista_maior[i][c])
		else:
			sequencia += str(lista_maior[i][c]) + ' ' + '+' + ' '
			
	print sequencia
