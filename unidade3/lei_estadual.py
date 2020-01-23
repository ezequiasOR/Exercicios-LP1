#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Lei Estadual - Unidade 3

idade = int(raw_input('Idade? '))

if idade < 12:
	print 'criança (meia entrada)'
	
elif idade >= 65:
	print 'idoso (meia entrada)'
else:
	estudante = str(raw_input('Estudante? '))
	if estudante == 's':
		rede_publica = str(raw_input('Rede Pública? '))
		if rede_publica == 's':
			print 'estudante da rede pública (isento)'
		else:
			print 'estudante (meia entrada)'
	else:
		print 'adulto (inteira)'
