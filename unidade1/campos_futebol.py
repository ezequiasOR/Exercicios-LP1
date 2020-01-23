# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Campos de Futebol - Unidade 1

#Recebe 3 medidas das áreas em m2
area1 = float(raw_input())
area2 = float(raw_input())
area3 = float(raw_input())

#converte as áres de m2 para campos de futebol e calcula a média
campos1 = area1 / 4000
campos2 = area2 / 4000
campos3 = area3 / 4000
media = (campos1 + campos2 + campos3) / 3

print "%.2f" % campos1
print "%.2f" % campos2
print "%.2f" % campos3
print "%.2f" % media
