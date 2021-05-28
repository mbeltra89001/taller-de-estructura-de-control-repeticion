dividendo=int(input("Dividendo es: "))
divisor=int(input("Divisor es: "))
if dividendo>0 and divisor>0:
  coc=0
  residuo=dividendo
  while (residuo>=divisor):
    residuo-=divisor
    coc+=1
print(residuo)
print(coc)