# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Avaliação Docente - Unidade 3

semestres = int(raw_input())
atv_ensino = int(raw_input())
prod_intelectual = int(raw_input())
atv_orientacao = int(raw_input())
administrativas = int(raw_input())

media = (atv_ensino + prod_intelectual + atv_orientacao + administrativas) / 4.0

if semestres >= 4.0 and atv_ensino >= 320.0 and prod_intelectual >= 100.0 and atv_orientacao >= 20.0 and media > 140.0:
	print 'Promoção deferida. Parabéns!'
elif semestres < 4.0:
	print 'Promoção indeferida. Número de semestres insuficiente.'
elif atv_ensino < 320.0 or prod_intelectual < 100.0 or atv_orientacao < 20:
	print 'Promoção indeferida. Pontuação mínima não alcançada.'
else: 
	print 'Promoção indeferida. Média insuficiente.'
