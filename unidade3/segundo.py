# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Segundo - Unidade 3

n1 = int(raw_input())
n2 = int(raw_input())
n3 = int(raw_input())
n4 = int(raw_input())

lista = [n1, n2, n3, n4]
lista.sort()

print 'Considerando os números %d, %d, %d e %d' % (n1, n2, n3, n4)
print 'O segundo menor número é %d' % lista[1]
print 'O segundo maior número é %d' % lista[2]
