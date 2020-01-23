# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Concurso - Unidade 3

escrita_cand1 = float(raw_input())      #Nota da escrita candidato 1
didatica_cand1 = float(raw_input())     #Nota da didática canditado 1
titulacao_cand1 = float(raw_input())    #Nota da titulacão candidato 1
idade_cand1 = int(raw_input())          #Idade do candidato 1

escrita_cand2 = float(raw_input())      #Nota da escrita candidato 2
didatica_cand2 = float(raw_input())     #Nota da didática candidato 2
titulacao_cand2 = float(raw_input())    #Nota da titulação candidato 2
idade_cand2 = int(raw_input())          #Idade do candidato 2

media_cand1 = (escrita_cand1 * 30 + didatica_cand1 * 40 + titulacao_cand1 * 30) / 100  #Média do candidato 1
media_cand2 = (escrita_cand2 * 30 + didatica_cand2 * 40 + titulacao_cand2 * 30) / 100  #Média do candidato 2

if media_cand1 > media_cand2:                                                  #Média candidato 1 é maior
	print 'O primeiro candidato foi aprovado com média %.1f.' % media_cand1
elif media_cand2 > media_cand1:                                                #Média candidato 2 é maior
	print 'O segundo candidato foi aprovado com média %.1f.' % media_cand2
elif media_cand1 == media_cand2:                                               #Média igual, idade desempata
	if idade_cand1 > idade_cand2:                                              #Idade candidato 1 é maior
		print 'O primeiro candidato foi aprovado com média %.1f.' % media_cand1
	elif idade_cand1 < idade_cand2:                                            #Idade candidato 2 é maior
		print 'O segundo candidato foi aprovado com média %.1f.' % media_cand2 
	elif idade_cand1 == idade_cand2:                                           #Idade dos candidatos é igual
		print 'Empate.'
