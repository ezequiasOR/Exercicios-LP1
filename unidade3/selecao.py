# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Seleção Projeto - Unidade 3

cre = float(raw_input())
meses = int(raw_input())
entrevista = int(raw_input())

if cre < 7 and meses < 6:
	print 'Candidato eliminado. CRE e experiência abaixo do limite.'
elif cre < 7:
	print 'Candidato eliminado. CRE abaixo do limite.'
elif meses < 6:
	print 'Candidato eliminado. Experiência abaixo do limite.'
else:
	if entrevista <= 3:
		print 'Candidato classificado.'
	else:
		print 'Candidato aprovado.'
