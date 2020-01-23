# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Classifica Corredor - Unidade 3

km_percorrido = float(raw_input())
tempo_horas = float(raw_input())

km_por_hora = km_percorrido / tempo_horas

if km_por_hora < 10.0:
	print 'Velocidade: %.1fkm/h. Corredor amador.' % km_por_hora
elif 10 <= km_por_hora <= 15.0:
	print 'Velocidade: %.1fkm/h. Corredor aspirante.' % km_por_hora
else:
	print 'Velocidade: %.1fkm/h. Corredor profissional.' % km_por_hora
