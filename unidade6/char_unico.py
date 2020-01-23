# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Char único - Unidade 6

def meu_in(letra, lista):
	for e in lista:
		if e == letra:
			return True
	return False

def char_unico(string):
	lista = []
	for letra in string:
		if meu_in(letra, lista) == False:
			lista.append(letra)

	soma = 0
	for e in lista:
		for i in range(len(string)):
			if string[i] == e:
				soma += 1
		if soma == 1:
			return e
		soma = 0
