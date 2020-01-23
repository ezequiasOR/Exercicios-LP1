# coding: utf-8

#UFCG - Programação I - 2018.1
#Aluno: Ezequias Rocha
#Questão: Operadores - Unidade 1

num1 = int(raw_input())
num2 = int(raw_input())

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2
exponenciacao = num1 ** num2

print '===== Operadores ====='
print 'A = %s' % num1
print 'B = %s' % num2
print 'Adição = %s' % soma
print 'Subtração = %s' % subtracao
print 'Multiplicação = %s' % multiplicacao
print 'Divisão = %s' % divisao
print 'Resto = %s' % resto
print 'Exponenciação = %s' % exponenciacao
print 'Negação de A = %s' % -(num1)
print 'A é igual a B? %s' % (num1 == num2)
print 'A é diferente de B? %s' % (num1 != num2)
print 'A é maior que B? %s' % (num1 > num2)
print 'B é maior que A? %s' % (num1 < num2)
print 'A é menor ou igual a B? %s' % (num1 <= num2)
