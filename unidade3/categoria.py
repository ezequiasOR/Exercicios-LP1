# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Categoria - Unidade 3

nome = str(raw_input())
idade = int(raw_input())

if 5 <= idade <= 7:
	print '%s, %d anos, Infantil A.' % (nome, idade)
elif 8 <= idade <= 10:
	print '%s, %d anos, Infantil B.' % (nome, idade)
elif 11 <= idade <= 13:
	print '%s, %d anos, Juvenil A.' % (nome, idade)
elif 14 <= idade <= 17:
	print '%s, %d anos, Juvenil B.' % (nome, idade)
elif idade >= 18:
	print '%s, %d anos, Senior.' % (nome, idade)
else:
	print '%s, %d anos, Não pode competir.' % (nome, idade)
