# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Calcula Nome - Unidade 1

nome = str(raw_input("Nome? "))
letras = float(raw_input("Letra? R$ "))

quantidade_letras = len(nome)
orcamento = quantidade_letras * letras

print "Orçamento: R$ " + str(orcamento)
