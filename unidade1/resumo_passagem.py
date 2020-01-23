#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Resumo Passagem - Unidade 1


identificador = raw_input()
horario = raw_input()
assento = raw_input()
portao = raw_input()
preco_sem_imposto = float(raw_input())
preco_total = float(raw_input())

porcentagem_de_imposto = ((preco_total - preco_sem_imposto) * 100.0) / preco_total

print '### Cartão de Embarque ###'
print 'Identificador do voo: %s. Horário: %s. Assento: %s. Portão: %s.' % (identificador, horario, assento, portao)
print 'Total de Imposto: %.1f%%.' % (porcentagem_de_imposto)
