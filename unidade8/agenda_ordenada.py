#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Agenda Ordenada - Unidade 8

def ordena_agenda(agenda):
	for elemento in agenda:
		for i in range(len(agenda)-1):
			if agenda[i] > agenda[i+1]:
				agenda[i], agenda[i+1] = agenda[i+1], agenda[i]

def print_agenda(agenda):
	for e in agenda:
		if e == nome:
			print '*', e
		else:
			print e
	
	print '----'

agenda = []

while True:
	nome = str(raw_input())
	if nome == '####':
		break
	agenda.append(nome)
	
	ordena_agenda(agenda)
	print_agenda(agenda)
