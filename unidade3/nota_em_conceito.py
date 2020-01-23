#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Conversão de Nota em Conceito - Unidade 3

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
nota4 = float(raw_input())

media_anual = (nota1 + nota2 + nota3 + nota4) / 4.0

if media_anual >= 9.0:
	print 'Conceito A.'

elif 7.5 <= media_anual < 9.0:
	print 'Conceito B.'

elif 6.0 <= media_anual < 7.5:
	print 'Conceito C.'

elif 4.0 <= media_anual < 6.0:
	print 'Conceito D.'

else:
	print 'Conceito E.'
