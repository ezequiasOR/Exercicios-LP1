#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Planilha de Notas - Unidade 3

planilha = str(raw_input()).split(',')

faltas = int(planilha[0])
nota_primeiro_estagio = float(planilha[1])
nota_segundo_estagio = float(planilha[2])
nota_terceiro_estagio = float(planilha[3])
nota_final = float(planilha[4])

media_parcial = (nota_primeiro_estagio * 3.0 + nota_segundo_estagio * 3.0 + nota_terceiro_estagio * 4.0) / 10.0
media_final = (media_parcial * 6.0 + nota_final * 4.0) / 10.0

if faltas < 8:
	if media_parcial >= 7.0:
		print 'média parcial: %.1f' % media_parcial
		print 'média final: %.1f' % media_parcial
		print 'status final: aprovado por média'
		
	elif  media_parcial <= 4.0:
		print 'média parcial: %.1f' % media_parcial
		print 'média final: %.1f' % media_parcial
		print 'status final: reprovado por média'
	
	else:
		if media_final > 5.0:
			print 'média parcial: %.1f' % media_parcial
			print 'média final: %.1f' % media_final
			print 'status final: aprovado na final'
		
		elif 4.0 <= media_final <= 5.0:
			print 'média parcial: %.1f' % media_parcial
			print 'média final: %.1f' % media_final
			print 'status final: reprovado na final'
			print '(aluno tem direito a RER)'
		else:
			print 'média parcial: %.1f' % media_parcial
			print 'média final: %.1f' % media_final
			print 'status final: reprovado na final'

else:
	if media_parcial >= 7.0:
		print 'média parcial: %.1f' % media_parcial
		print 'média final: %.1f' % media_parcial
		print 'status final: reprovado por faltas'
		
	elif  media_parcial <= 4.0:
		print 'média parcial: %.1f' % media_parcial
		print 'média final: %.1f' % media_parcial
		print 'status final: reprovado por faltas'
	
	else:
		if media_final > 5.0:
			print 'média parcial: %.1f' % media_parcial
			print 'média final: %.1f' % media_final
			print 'status final: reprovado por faltas'
		
		elif 4.0 <= media_final <= 5.0:
			print 'média parcial: %.1f' % media_parcial
			print 'média final: %.1f' % media_final
			print 'status final: reprovado por faltas'
		else:
			print 'média parcial: %.1f' % media_parcial
			print 'média final: %.1f' % media_final
			print 'status final: reprovado por faltas'

