# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Greve - Unidade 1

abstencao = int(raw_input())
a_favor = int(raw_input())
contra = int(raw_input())

soma_votos = float(abstencao + a_favor + contra)
porc_abstencao = (100 * abstencao) / soma_votos
porc_favor = (100 * a_favor) / soma_votos
porc_contra = (100 * contra) / soma_votos

print 'Resultado da Votação'
print
print '%d abstenções (%.2f%%)' % (abstencao, porc_abstencao)
print '%d a favor (%.2f%%)' % (a_favor, porc_favor)
print '%d contra (%.2f%%)' % (contra, porc_contra)
