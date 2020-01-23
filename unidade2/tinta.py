# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Tinta - Unidade 2

altura = float(raw_input())
largura = float(raw_input())

area = altura * largura
litros_de_tinta = (area * 3.6) / 50

print '%.2f l' % litros_de_tinta
