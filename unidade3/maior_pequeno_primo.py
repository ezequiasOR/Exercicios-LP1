#coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Maior pequeno primo - Unidade 3

n = int(raw_input())

if n % 29 == 0:
	mult = n / 29
	print '%d não tem fatores primos menores que 10' % n
elif n % 23 == 0:
	mult = n / 23
	print '%d não tem fatores primos menores que 10' % n
elif n % 19 == 0:
	mult = n / 19
	print '%d não tem fatores primos menores que 10' % n
elif n % 17 == 0:
	mult = n / 17
	print '%d não tem fatores primos menores que 10' % n
elif n % 13 == 0:
	mult = n / 13
	print '%d não tem fatores primos menores que 10' % n
elif n % 11 == 0:
	mult = n / 11
	print '%d não tem fatores primos menores que 10' % n
elif n % 7 == 0:
	mult = n / 7
	print '7 * %d = %d' % (mult, n)
elif n % 5 == 0:
	mult = n / 5
	print '5 * %d = %d' % (mult, n)
elif n % 3 == 0:
	mult = n / 3
	print '3 * %d = %d' % (mult, n)
elif n % 2 == 0:
	mult = n / 2
	print '2 * %d = %d' % (mult, n)
else:
	print '%d não tem fatores primos menores que 10' % n
