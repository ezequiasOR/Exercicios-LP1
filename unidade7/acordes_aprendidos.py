# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Acordes Aprendidos - Unidade 7

def meu_in(e, lista):
	for i in range(len(lista)):
		if e == lista[i]:
			return True
	return False

def acordes(musica_1, musica_2):
	acordes_aprendidos = []

	for e in musica_1:
		if meu_in(e, acordes_aprendidos) == False:
			acordes_aprendidos.append(e)

	for e in musica_2:
		if meu_in(e, acordes_aprendidos) == False:
			acordes_aprendidos.append(e)
	
	return acordes_aprendidos
