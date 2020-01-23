# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Media Final - Unidade 1

media_parcial = float(raw_input())
nota_prova = float(raw_input())

media = ((60 * media_parcial) + (40 * nota_prova)) / 100

print 'Média final: %.1f' % media
