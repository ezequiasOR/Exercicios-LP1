# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Eleições - Unidade 3

votos_candidato_a = int(raw_input())
votos_candidato_b = int(raw_input())
votos_candidato_c = int(raw_input())

soma_votos = votos_candidato_a + votos_candidato_b + votos_candidato_c
porcentagem_a = votos_candidato_a * 100 / float(soma_votos)
porcentagem_b = votos_candidato_b * 100 / float(soma_votos)
porcentagem_c = votos_candidato_c * 100 / float(soma_votos)

if porcentagem_a > porcentagem_b and porcentagem_b > porcentagem_c:
	if porcentagem_a > 50:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato A, segundo turno = Não' % (porcentagem_a, porcentagem_b, porcentagem_c)
	else:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato A, segundo turno = Sim' % (porcentagem_a, porcentagem_b, porcentagem_c)

elif porcentagem_a > porcentagem_c and porcentagem_c > porcentagem_b:
	if porcentagem_a > 50:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato A, segundo turno = Não' % (porcentagem_a, porcentagem_b, porcentagem_c)
	else:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato A, segundo turno = Sim' % (porcentagem_a, porcentagem_b, porcentagem_c)

elif porcentagem_b > porcentagem_a and porcentagem_a > porcentagem_c:
	if porcentagem_b > 50:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato B, segundo turno = Não' % (porcentagem_a, porcentagem_b, porcentagem_c)
	else:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato B, segundo turno = Sim' % (porcentagem_a, porcentagem_b, porcentagem_c)

elif porcentagem_b > porcentagem_c and porcentagem_c > porcentagem_a:
	if porcentagem_b > 50:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato B, segundo turno = Não' % (porcentagem_a, porcentagem_b, porcentagem_c)
	else:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato B, segundo turno = Sim' % (porcentagem_a, porcentagem_b, porcentagem_c)
	
elif porcentagem_c > porcentagem_a and porcentagem_a > porcentagem_b:
	if porcentagem_c > 50:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato C, segundo turno = Não' % (porcentagem_a, porcentagem_b, porcentagem_c)
	else:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato C, segundo turno = Sim' % (porcentagem_a, porcentagem_b, porcentagem_c)

else:
	if porcentagem_c > 50:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato C, segundo turno = Não' % (porcentagem_a, porcentagem_b, porcentagem_c)
	else:
		print 'candidato A = %.2f%%, candidato B = %.2f%%, candidato C = %.2f%%, o candidato mais votado é o Candidato C, segundo turno = Sim' % (porcentagem_a, porcentagem_b, porcentagem_c)
