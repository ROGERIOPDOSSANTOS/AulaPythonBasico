# Converte distancia
def mettocent(met):
    cent = met * 100
    return cent
def centtomet(cent):
    met = cent / 100
    return met
def mettokil(met):
    kil = met / 1000
    return kil
def kiltomet(kil):
    met= kil * 1000
    return met
def centtokil(cent):
    kil = cent / 100000
    return kil
def kiltocent(kil):
    cent = kil * 100000
    return cent

escolha = True

while escolha == True:
    print('Escolha uma opção de conversão:')
    print('1 Metros para centimetros\n2 Centimetros para metros\n3 Metros para quilometros')
    print('4 Quilometros para metros\n5 Centimetros para quilometros\n6 Quilometros para centimetros\n')
    escolha = int(input())

    if escolha > 6:
        print("Opção inválida, digite novamente")
        continue
    dist = float(input("Digite a distância a ser convertida:"))

    if escolha == 1:
        print(mettocent(dist), "centimentros")
        break
    elif escolha == 2:
        print(centtomet(dist), "metros")
        break
    elif escolha == 3:
        print(mettokil(dist), "quilometros")
        break
    elif escolha == 4:
        print(kiltomet(dist), "metros")
        break
    elif escolha == 5:
        print(centtokil(dist), "quilometros")
        break
    elif escolha == 6:
        print(kiltocent(dist), "centimentros")
        break

print("Confirmação de senha")
senha1 = input("Digite a senha: ")
senha2 = input("Confirme a senha: ")
while senha1 != senha2:
    print("Senha errada, digite novamente.")
    senha1 = input("Digite a senha: ")
    senha2 = input("Confirme a senha: ")
print("senha confirmada, parabéns!")

#Faça um programa em Python que leia n números inteiros a partir do teclado,
# até que o usuário digite 0. Ao final, mostre a soma de todos os números digitados
total=0
numero=int(input("Digite um número: "))
while numero != 0:
    total+=numero
    numero=int(input("Digite um número:: "))
print("Soma dos números= ",total)


# Define a lista
nums = []
# O laço será executado enquanto o tamanho da lista nums for menor que 4
while len(nums) < 4:
    # Pede ao usuário uma entrada e a armazena em uma variável como número inteiro.
    user_input = int(input("Insira um número inteiro: "))
    # Se a entrada for um número par, é adicionada à lista
    if user_input % 2 == 0:
        nums.append(user_input)

#A primeira linha define um laço while True - enquanto for verdadeira
# que será executado indefinidamente até que uma instrução break seja encontrada
while True:
  numero = int(input("Entre com numero inteiro:"))
  if numero % 2 != 0:
      print("O numero é Impar")
      break
  else:
     print("O numero é Par")

operacao = input("Digite a operação (soma, sub, mult, div). Digite sair para encerrar: ")
while operacao != 'sair':
  n1 = input("Digite o primeiro numero: ")
  n2 = input("Digite o segundo numero: ")

  if operacao == "soma":
    resultado = int(n1) + int(n2)
    print("O resultado da soma é: %d" %resultado)
    operacao = input ("Digite a operação (soma, sub, mult, div). Digite sair para encerrar: ")
  elif operacao == "sub":
    resultado = int(n1) - int(n2)
  elif operacao == "mult":
    resultado = int(n1) * int(n2)
  elif operacao == "div":
    resultado = int(n1) / int(n2)

  else:
    resultado = "operador não suportado, use soma, sub, mult ou div."
  print("O resultado da operação é: " + str(resultado))
  print("---------------------------------------")