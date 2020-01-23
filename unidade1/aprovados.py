#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Percentagem de aprovados - Unidade: 1

print 'Análise da Turma'
print '==='

aprovados = int(raw_input('Número de aprovados? '))
reprovados = int(raw_input('Número de reprovados? '))

total_alunos = aprovados + reprovados
percentagem_aprovados = (aprovados * 100.0) / total_alunos
percentagem_reprovados = (reprovados * 100.0) / total_alunos

print '---'
print 'Total de alunos na turma: %d' % total_alunos
print 'Aprovados: %d = %.1f%%' % (aprovados, percentagem_aprovados)
print 'Reprovados: %d = %.1f%%' % (reprovados, percentagem_reprovados)
