# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Embarque Passageiros - Unidade 3

primeira_classe = int(raw_input())                    #Quantidade de passageiros da primeira classe
segunda_classe = int(raw_input())                     #Quantidade de passageiros da segunda classe

if primeira_classe > 10:                              #Remanejados para outro voo da primeira classe
	voo2_prim_clas = primeira_classe - 10
else:
	voo2_prim_clas = 0
		
if segunda_classe > 100 and primeira_classe >= 10:    #Remanejados para outro voo da segunda classe:
	voo2_seg_clas = segunda_classe - 100
else:
	voo2_seg_clas = 0
	
if segunda_classe > 100 and primeira_classe < 10:     #Remanejados para outro voo ou para primeira classe
	vagas_prim_clas = 10 - primeira_classe
	remanejados = segunda_classe - 100
	if remanejados > vagas_prim_clas:
		voo2_seg_clas = remanejados - vagas_prim_clas
		remanejados_prim_clas = remanejados - voo2_seg_clas
	else:
		remanejados_prim_clas = remanejados
else:
	remanejados_prim_clas = 0

passageiros_embarcados = (primeira_classe - voo2_prim_clas) + (segunda_classe - voo2_seg_clas)
	

print '%d passageiro(s) da primeira classe remanejado(s) para outro voo.' % voo2_prim_clas
print '%d passageiro(s) da econômica remanejado(s) para a primeira classe.' % remanejados_prim_clas
print '%s passageiro(s) da econômica remanejado(s) para outro voo.' % voo2_seg_clas
print '%d passageiros embarcados.' % passageiros_embarcados
