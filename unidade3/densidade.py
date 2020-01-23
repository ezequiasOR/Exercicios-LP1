# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Densidade - Unidade 3

massa1 = float(raw_input())
vol1 = float(raw_input())
massa2 = float(raw_input())
vol2 = float(raw_input())
massa3 = float(raw_input())
vol3 = float(raw_input())

dens1 = massa1 / vol1
dens2 = massa2 / vol2
dens3 = massa3 / vol3

if dens1 < dens2 and dens2 < dens3:
	print 'O líquido 1, com densidade %.2f, irá ocupar a parte de cima do recipiente.' % dens1
elif dens1 < dens3 and dens3 < dens2:
	print 'O líquido 1, com densidade %.2f, irá ocupar a parte de cima do recipiente.' % dens1
elif dens2 < dens1 and dens1 < dens3:
	print 'O líquido 2, com densidade %.2f, irá ocupar a parte de cima do recipiente.' % dens2
elif dens2 < dens3 and dens3 < dens1:
	print 'O líquido 2, com densidade %.2f, irá ocupar a parte de cima do recipiente.' % dens2
elif dens3 < dens2 and dens2 < dens1:
	print 'O líquido 3, com densidade %.2f, irá ocupar a parte de cima do recipiente.' % dens3
else:
	print 'O líquido 3, com densidade %.2f, irá ocupar a parte de cima do recipiente.' % dens3
