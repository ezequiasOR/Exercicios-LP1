#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Aprovados e Reprovados - Unidade 4

n = int(raw_input())          #Número de alunos da turma

aprovados = 0                 #Contador para os aprovados
reprovados = 0                #Contador para os reprovados
media_reprovados = 0.0
media_aprovados = 0.0

for i in range(0, n):
	nota = float(raw_input())

	if nota >= 7.0:
		media_aprovados += nota
		aprovados += 1
	else:
		media_reprovados += nota
		reprovados += 1

if reprovados > 0:
	media_repr = media_reprovados / reprovados
	print 'Reprovados: %d' % reprovados
	print 'Média: %.1f' % media_repr
else:
		print 'Reprovados: %d' % reprovados

print
		
if aprovados > 0:
	media_apro = media_aprovados / aprovados
	print 'Aprovados: %d' % aprovados
	print 'Média: %.1f' % media_apro
else:
	print 'Aprovados: %d' % aprovados
