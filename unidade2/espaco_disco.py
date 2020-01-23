# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Espaço em Disco Simplificado - Unidade 2

login1 = str(raw_input())
espaco1 = int(raw_input())
login2 = str(raw_input())
espaco2 = int(raw_input())
login3 = str(raw_input())
espaco3 = int(raw_input())

espaco_disco1 = (espaco1 / 1024.0) / 1024.0 
espaco_disco2 = (espaco2 / 1024.0) / 1024.0
espaco_disco3 = (espaco3 / 1024.0) / 1024.0
espaco_ocupado = espaco_disco1 + espaco_disco2 + espaco_disco3
espaco_medio_ocupado = espaco_ocupado / 3.0

print 'SPLab - Espaço utilizado pelos usuários'
print '---------------------------------------------'
print 'Nr., Usuário, Espaço Utilizado'
print
print '1, %s, %.2f MB' % (login1, espaco_disco1)
print '2, %s, %.2f MB' % (login2, espaco_disco2)
print '3, %s, %.2f MB' % (login3, espaco_disco3)
print
print 'Espaço total ocupado: %.2f MB' % espaco_ocupado
print 'Espaço médio ocupado: %.2f MB' % espaco_medio_ocupado
