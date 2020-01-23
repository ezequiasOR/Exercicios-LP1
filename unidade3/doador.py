# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Doador - Unidade 3

tipo1 = str(raw_input()).upper()
rh1 = str(raw_input())
tipo2 = str(raw_input()).upper()
rh2 = str(raw_input())

paciente = tipo1 + rh1
doador = tipo2 + rh2

if paciente == 'AB+':
	if doador == 'AB+' or doador == 'A+' or doador == 'B+' or doador == 'O+' or doador == 'AB-' or doador == 'A-' or doador == 'B-' or doador == 'O-':
		print 'compatível'
	
elif paciente == 'A+':
	if doador == 'A+' or doador == 'A-' or doador == 'O+' or doador == 'O-':
		print 'compatível'
	else:
		print 'incompatível'
	
elif paciente == 'B+':
	if doador == 'B+' or doador == 'B-' or doador == 'O+' or doador == 'O-':
		print 'compatível'
	else:
		print 'incompatível'
	
elif paciente == 'O+':
	if doador == 'O+' or doador == 'O-':
		print 'compatível'
	else:
		print 'incompatível'
	
elif paciente == 'AB-':
	if doador == 'AB-' or doador == 'A-' or doador == 'B-' or doador == 'O-':
		print 'compatível'
	else:
		print 'incompatível'
		
elif paciente == 'A-':
	if doador == 'A-' or doador == 'O-':
		print 'compatível'
	else:
		print 'incompatível'
	
elif paciente == 'B-':
	if doador == 'B-' or doador == 'O-':
		print 'compatível'
	else:
		print 'incompatível'
	
elif paciente == 'O-':
	if doador == 'O-':
		print 'compatível'
	else:
		print 'incompatível'

