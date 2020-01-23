# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Distribuição de alunos - Unidade 3

unidade = int(raw_input())
deseja_pular = str(raw_input())
questoes_feitas = int(raw_input())

if unidade == 4 and deseja_pular == 'sim':
	if questoes_feitas > 0:
		print 'O aluno deve assistir aula com o prof Dalton.'
	else:
		print 'O aluno deve assistir aula com o prof João.'
	
elif 1 <= unidade <= 4 and deseja_pular == 'não':
	print 'O aluno deve assistir aula com o prof João.'
	
elif 5 <= unidade <= 8 and deseja_pular == 'não':
	print 'O aluno deve assistir aula com o prof Dalton.'

elif unidade == 8 and deseja_pular == 'sim':
	if questoes_feitas > 0:
		print 'O aluno deve assistir aula com o prof Jorge.'
	else:
		print 'O aluno deve assistir aula com o prof Dalton.'	

elif 1 <= unidade <= 3 and deseja_pular == 'sim':
	print 'O aluno deve assistir aula com o prof João.'

elif 5 <= unidade <= 7 and deseja_pular == 'sim':
	print 'O aluno deve assistir aula com o prof Dalton.'

elif unidade >= 9:
	print 'O aluno deve assistir aula com o prof Jorge.' 
