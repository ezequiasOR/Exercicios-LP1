#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Orçamento Construção - Unidade 1

preco_unidade_tijolo = float(raw_input('Digite o preço da unidade do tijolo (Em reais): '))
altura_tijolo = float(raw_input('Digite a altura do tijolo (Em metros): '))
comprimento_tijolo = float(raw_input('Digite o comprimento do tijolo (Em metros): '))
altura_paredes = float(raw_input('Digite a altura das paredes (Em metros): '))
comprimento_paredes = float(raw_input('Digite o comprimento das paredes (Em metros): '))

num_tijolos_altura = altura_paredes / altura_tijolo
num_tijolos_largura = comprimento_paredes / comprimento_tijolo

num_tijolos_total = num_tijolos_altura * num_tijolos_largura
orcamento_final = num_tijolos_total * preco_unidade_tijolo

print 'O número total de tijolos é %.1f e o orçamento final é de R$ %.1f' % (num_tijolos_total, orcamento_final)
