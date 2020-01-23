# coding: utf-8

# UFCG - Programação I - 2018.1
# Aluno: Ezequias Rocha
# Questão: Mega Tripla - Unidade 2

num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

resto_num1 = num1 % 11
resto_num2 = num2 % 11
resto_num3 = num3 % 11

print '%02d-%02d-%02d' % (resto_num1, resto_num2, resto_num3)
