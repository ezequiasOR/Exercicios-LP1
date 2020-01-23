#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Primeiro e Último - Unidade 1

numero = int(raw_input())

primeiro_digito = numero / 1000
ultimo_digito = numero % 10.0

print '%d %d' % (primeiro_digito, ultimo_digito)
