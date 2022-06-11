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