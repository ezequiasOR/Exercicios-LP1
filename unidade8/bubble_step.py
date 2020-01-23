#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Bubble Step - Unidade 8

while True:
	sequencia = str(raw_input()).split()
	if sequencia[0] == 'fim': break
	
	for i in range(len(sequencia)-1):
		if int(sequencia[i]) > int(sequencia[i+1]):
			sequencia[i], sequencia[i+1] = sequencia[i+1], sequencia[i]
	
	saida = ''
	for indice in range(len(sequencia)):
		if indice == len(sequencia)-1:
			saida += sequencia[indice]
		else:
			saida += sequencia[indice] + ' '
			
	print saida
