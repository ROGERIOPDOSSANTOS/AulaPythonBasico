# Variáveis 
#  Definição das primeiras variáveis e constantes

a = 3
b = 7
print(a+b)
print((a+b)+(a+b))
print((a-b)*(a+b))
print((a-b)*(a+b))

# Mudança de tipo de uma variável
a = "Agora eu entendi tudo"
b = "Graças ao meu querido professor"
print(a)
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
nome = input("Olá, qual o seu nome?")
print("Olá,", nome)

# Captação de input do valor
valor = float(input("Digite um Valor"))
print(valor)

#Fazendo um calculo e usando condições lógicas de Sequencia
Soma = valor*5.5
print(Soma)
if Soma > 7:
  print("Valor Maior que 7")
else:
   print("Valor Menor que 7")
print("O Valor é,", Soma)

#Competição
# Crie um software que você entre com dois numero aleatórios e apresente em tela a subração desses 2 numeros
#N1= int(input("Digite o 1 numero?"))
#N2= int(input("Digite o 1 numero?"))
#RES = (N1*N2)
#print(RES)
# Crie um software que calcule a área (com numero aleatorios)
#BASE = float(input("Digite o n da Base"))
#ALTURA = float(input("Digite o n da altura"))
#AREA = BASE*ALTURA
#print("O resultado da área é",AREA,"m2")

#Elabore um algoritmo a ler 4 notas de um aluno (de 1 a 10).
# Após calcular a média das notas”
#NOTA1 = float(input("Digite a 1 nota"))
#NOTA2 = float(input("Digite a 2 nota"))
#NOTA3 = float(input("Digite a 3 nota"))
#NOTA4 = float(input("Digite a 4 nota"))
#MEDIA = ((NOTA1+NOTA2+NOTA3+NOTA4)/4)
#print("A MEDIA DO ALUNO É", MEDIA)

#Faça um algoritmo que leia o nome, idade e o endereço de uma pessoa e mostre essas informações
#nome = input("Digite o nome")
#idade = int(input("Digite o idade"))
#end = input("Digite o endereço")
#print(nome,idade,end)
