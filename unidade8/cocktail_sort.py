#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Cocktail Sort - Unidade 8

lista = [3, 4, 2, 0, 5, 6, 7,1]

def cocktailSort(lista):
	lista_saida = []
	lista_aux = []
	
	lista_aux += lista
	lista_saida.append(lista_aux)
	
	trocou = True
	
	while trocou:
		trocou = False
		lista_aux = []
		
		for i in range(len(lista)-1):
			if lista[i] > lista[i+1]:
				lista[i], lista[i+1] = lista[i+1], lista[i]
				trocou = True
		
		for j in range(len(lista)-1, 0, -1):
			if lista[j] < lista[j-1]:
				lista[j], lista[j-1] = lista[j-1], lista[j]
				trocou = True
		
		lista_aux += lista
		lista_saida.append(lista_aux)
	
	lista_saida.pop(-1)
	return lista_saida
	
print cocktailSort(lista)
