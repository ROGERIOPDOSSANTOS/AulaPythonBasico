# Capítulo 10: Estruturas de Controle - Repetição While e For

# Primeira estrutura de controle: If
nome = input("Digite aqui seu nome: ")

if nome == "Felipe":
  print("Olá, %s" % nome)

if nome == "Felipe":
  print("Olá, %s" % nome)
else:
  print("Olá, visitante")

if nome == "Felipe":
  print("Olá, Felipe")
elif nome == "Maria":
  print("Oi, Maria")
elif nome == "Carlos":
  print("E aí, Carlos?")
else:
  print("Olá, visitante")

# Iterando com for sobre listas
lista = ["Alfredo", "Mario", "José", "Carolina", "Joana", "Luiza"]
for nome in lista:
  print(nome)

# Contextualização 1 - Slides estrutura de Repetição
qtd_refri = int(input("Informe a quantidade de refrigerantes vendidos"))
total = qtd_refri * 4.00
print("Foram vendidos R$ %.2f de refrigerantes"%total)

# Contextualização 2
qtd_refri1 = int(input("Informe a quantidade de refrigerantes vendidos ontem"))
qtd_refri2 = int(input("Informe a quantidade de refrigerantes vendidos antes de ontem"))
qtd_refri3 = int(input("Informe a quantidade de refrigerantes vendidos 3 dias atrás"))

total1 = qtd_refri1 * 4.00
total2 = qtd_refri2 * 4.00
total3 = qtd_refri3 * 4.00

totat_geral = total1 + total2 + total3

print("Foram vendidos R$ %.2f de refrigerantes ontem"%total1)
print("Foram vendidos R$ %.2f de refrigerantes antes de ontem"%total2)
print("Foram vendidos R$ %.2f de refrigerantes 3 dias atrás"%total3)
print("Foram vendidos R$ %.2f de refrigerantes nos 3 dias"%total_geral)

# Contextualização while 1
total_geral = 0
i = 1
while i < 3:
    qtd_refri = int(input("Informe a quantidade de refrigerantes vendidos %d dias atrás" %i))
    total = qtd_refri * 4.00
    print("Foram vendidos R$ %.2f de refrigerantes"%total)
    i = i + 1

# Contextualização while 2
total_geral = 0
i = 1
while i <= 3:
    qtd_refri = int(input("Informe a quantidade de refrigerantes vendidos %d dias atrás" %i))
    total = qtd_refri * 4.00
    print("Foram vendidos R$ %.2f de refrigerantes"%total)
    total_geral = total_geral + total
    i = i + 1
    print ("Foram vendidos total geral de %.2f de refrigerantes" % total_geral)

# Contextualização For 1
for i in range(10):
    print(i)

# Contextualização For 2
for i in range(1,4):
    qtd_refri = int (input ("Informe a quantidade de refrigerantes vendidos %d dias atrás" % i))
    total = qtd_refri * 4.00
    print ("Foram vendidos R$ %.2f de refrigerantes" % total)

# Contextualização For 3
total_geral = 0
for i in range(1,4):
    qtd_refri = int (input ("Informe a quantidade de refrigerantes vendidos %d dias atrás" % i))
    total = qtd_refri * 4.00
    print ("Foram vendidos R$ %.2f de refrigerantes" % total)
    total_geral = total_geral + total
print("Foram vendidos R$ %.2f de refrigerantes no %d dias." % (total_geral, i))

# Iterando com for sobre dicionários
aluno = {"nome": "Maria", "idade": 20, "nota": 9.2}

print("Exemplo 1a - iterando sobre chaves")
for chave in aluno:
  print(chave)

print("\nExemplo 1b - iterando sobre chaves")
for chave in aluno.keys():
  print(chave)

print("\nExemplo 2 - iterando sobre valores")
for valor in aluno.values():
  print(valor)

print("\nExemplo 3 - iterando sobre ambos")
for chave, valor in aluno.items():
  print(chave + " - " + str(valor))

# Utilizando range para criar um intervalo de números
print("Range com 1 parâmetro")
for i in range(10):
  print(i)

print("Range com 2 parâmetros")    
for i in range(3,10):
  print(i)

# Break e continue em loops
print("Exemplo break")
for i in range(1,11):
    if i % 5 == 0:
        break
    print(i)
    
print("Exemplo continue")
for i in range(1,11):
  if i % 5 == 0:
      continue
  print(i)

# Exemplo do loop while
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1

# Exemplo com condição while true e break
while True:
  nome = input("Digite seu nome ou sair para terminar o programa: ")
  if nome == "sair":
    break
  else:
    print("Olá, %s" % nome)