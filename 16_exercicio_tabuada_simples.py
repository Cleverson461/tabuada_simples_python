# Receba un número inteiro do usuário e mostre a tabuada desse número. 

numero = int(input('Digite qual número deseja saber a tabuada:  '))

i = 1
while i<= 10:
  print(f'Numero: {numero} x {i} = {numero * i}')
  i +=  1