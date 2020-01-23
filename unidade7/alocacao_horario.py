# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Alocação Horário - Unidade 7

def meu_in(e, lista2):
	for i in range(len(lista2)):
		if lista2[i] == e:
			return True
	return False

def meu_count(e, disciplinas):
	cont = 0
	for i in range(len(disciplinas)):
		horarios = disciplinas[i].split('-')
		if e == horarios[1]:
			cont += 1
	
	return cont

def get_choque_horario(disciplinas):
	lista2 = []

	for e in disciplinas:
		periodos = e.split('-')
		
		for j in range(len(disciplinas)):
			horarios = disciplinas[j].split('-')
			
			if periodos[1] == horarios[1] and meu_count(periodos[1], disciplinas) > 1:
				if meu_in(disciplinas[j], lista2) == False:
					lista2.append(disciplinas[j])
			
	return lista2
