x=0
Qimpares=0
Qpares=0
x=int(input("Digite um conjunto de numeros: "))
while x!=9999:
  if x % 2 != 0:
    Qimpares= Qimpares + 1
      
  else:
    Qpares = Qpares + 1
  x=int(input("Digite um conjunto de numeros: "))

print(f"Quantidade de numeros impares: {Qimpares}")
print(f"Quantidade de numeros pares: {Qpares}")