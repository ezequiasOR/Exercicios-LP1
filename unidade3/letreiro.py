#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Letreiro - Unidade 3

palavra1 = str(raw_input())
palavra2 = str(raw_input())
palavra3 = str(raw_input())

letreiro_palavras = [palavra1, palavra2, palavra3]
letreiro_palavras.sort()
palavra1 = letreiro_palavras[0]
palavra2 = letreiro_palavras[1]
palavra3 = letreiro_palavras[2]

print palavra1, palavra2, palavra3
