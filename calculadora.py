#entrada de dados

print ("calculadora eletrônica")

while True:


  num1 = input ("digite o primeiro número: ")
  num2 = input ("digite o segundo número: ")

#conversão para float
  num1=float (num1)
  num2=float (num2)


  op= input ("escolha a operação")

  if op == ("+"):
        print (num1 + num2)
  elif op== ("-"):
        print (num1 - num2)
  elif op== ("*"):
        print (num1 * num2)
  elif op== ("/"):
    if num2==0:
        print ("não é possivel dividir por zero")
    else:
        print (num1 / num2)
  else:
      print ("operação invalida")

  outra_op = input ("deseja fazer outra operação? s/n: ").strip().lower()

  if outra_op != "s":
      print ("obrigado por usar a calculadora eletrônica")
      break
