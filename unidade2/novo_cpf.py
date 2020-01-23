#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Novo CPF - Unidade 2

parte1 = int(raw_input())
parte2 = int(raw_input())
parte3 = int(raw_input())

parte4 = (parte3 / 100) + ((parte3 % 100)/10) + ((parte3 % 100)%10)

print '%03d.%03d.%03d-%02d' % (parte1, parte2, parte3, parte4)
