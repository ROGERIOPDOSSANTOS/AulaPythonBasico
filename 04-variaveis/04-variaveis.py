# Variáveis 
#  Definição das primeiras variáveis e constantes
a = 3
b = 7

c= (a+b)-(b+a)


print(c)

print((a+b)-(b+a))


print((a-b)*(a+b))
print((a-b)*(a+b))
# Mudança de tipo de uma variável
a = "Agora eu entendi tudo"
b = "Graças ao meu querido professor"
print(a + b)

print(b)
# Definindo uma variável com base no valor atual de outra
c = a+b
print(c)
# Definição de múltiplas variáveis com valores iguais
x = y = z = 10
print(x)
print(y)
print(z)

# Definição de múltiplas variáveis com valores diferentes
x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

# Captação de input do usuário
nome = str(input("Olá, qual o seu nome?"))
print("Olá,", nome)

# Captação de input com idade

idade = float(input("Digite sua idade"))
print()
if idade < 12:
    print('crianca',idade)
elif idade < 18:
    print('adolescente',idade)
elif idade < 60:
    print('adulto',idade)
else:
    print('idoso')

# Captação de input com media de uma nota
#Crie um algoritmo onde vc entra com dois valores de nota de um aluno e Calcula a media
#Apresenta se esta Aprovado, Reprovado ou Recuperação
valor1 = float(input("Digite 1 valor"))
valor2 = float(input("Digite 2 valor"))
media = (valor1+valor2)/2
if media > 7:
    print('Aprovado!',media)
elif media < 5:
    print('Reprovado!',media)
else:
    print('Em Recuperação',media)
#Competição
# Crie um software que você entre com dois numero aleatórios e apresente em tela a subtração desses 2 numeros
N1= int(input("Digite o 1 numero?"))
N2= int(input("Digite o 2 numero?"))
RES = (N1-N2)
print(RES)

# Crie um software que calcule a área - entre com os valores

BASE = float(input("Digite o n da Base"))
ALTURA = float(input("Digite o n da altura"))
AREA = BASE*ALTURA
print("O resultado da área é",AREA,"m2")

#Elabore um algoritmo a ler 4 notas de um aluno (de 1 a 10).
# Após calcular a média das notas”
NOTA1 = float(input("Digite a 1 nota"))
NOTA2 = float(input("Digite a 2 nota"))
NOTA3 = float(input("Digite a 3 nota"))
NOTA4 = float(input("Digite a 4 nota"))
MEDIA = ((NOTA1+NOTA2+NOTA3+NOTA4)/4)
print("A MEDIA DO ALUNO É", MEDIA)

#Faça um algoritmo que leia o nome, idade e o endereço de uma pessoa e mostre essas informações
nome = input("Digite o nome")
idade = int(input("Digite o idade"))
end = input("Digite o endereço")
print(nome,idade,end)


#Crie um algoritmo que controle as permissoes do um usuario
# Se for admin permita a entrada como administrador
# Se for user permita entrada como usuario
# caso nenhum dos dois negue suas entradas dizendo senha invalida para acesso

# Captação de input com senha de usuario
senha = str(input("Digite a senha de entrada"))
if (senha == "admin"):
    print("Olá administrador")
elif (senha == "user"):
    print("Olá usuario")
else:
   print("Acesso negado. Verifique sua senha")



letra = input("Digite um caractere: ")
if(letra == "a" or letra == "A" or letra == "b" or letra == "B" or letra == "c" or letra == "C" or letra == "d" or letra == "D" or \
    letra == "e" or letra == "E"):
    print ("Vogal")
else:
    print("Consoante")

letra = str(input("Digite um caractere: "))
if(letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or \
    letra == "I" or letra == "o" or letra == "O" or \
    letra == "u" or letra == "U"):
    print ("Vogal")
elif(letra==int):
    print("Número")
else:
    print("Consoante")


letra = input("Digite um caractere: ")
if (letra in ('aeiou') or letra in ('AEIOU')):
    print ("Vogal")
elif (letra.isnumeric()):
    print("Número")
else:
    print("Consoante")


"""Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),se digitar outro valor deve aparecer valor inválido.
"""
dia_int = int(input("Digite o número do dia da semana: "))
dia_str = ""
if dia_int == 1:
    dia_str = "Domingo"
elif dia_int == 2:
    dia_str = "Segunda"
elif dia_int == 3:
    dia_str = "Terça"
elif dia_int == 4:
    dia_str = "Quarta"
elif dia_int == 5:
    dia_str = "Quinta"
elif dia_int == 6:
    dia_str = "Sexta"
elif dia_int == 7:
    dia_str = "Sábado"
if dia_str == "":
    print("Valor inválido")
else:
    print(f"O dia correspondente é {dia_str}")

