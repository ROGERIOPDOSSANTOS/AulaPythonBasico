operacao = input("Digite a operação (soma, sub, mult, div). Digite sair para encerrar: ")
while operacao != 'sair':
  n1 = input("Digite o primeiro numero: ")
  n2 = input("Digite o segundo numero: ")
  if operacao == "soma":
    resultado = int(n1) + int(n2)
    print("O resultado da soma é: %d"%resultado)
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


