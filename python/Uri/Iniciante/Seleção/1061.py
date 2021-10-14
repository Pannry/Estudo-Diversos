def calcula_dia():
  a = input()
  a = list(a)
  tam = len(a)

  if tam == 5:
    b = int(a[4])
    b = b*24*60*60
  elif tam == 6:
    a[4] = int(a[4]) 
    a[5] = int(a[5])
    b = a[4]*10+a[5]
    b = b*24*60*60
  return b

def calcula_horas():
  a = input()
  a = list(a)

  a[0] = int(a[0]) 
  a[1] = int(a[1])
  b = a[0]*10+a[1]
  b = b*60*60
  
  a[5] = int(a[5]) 
  a[6] = int(a[6])
  c = a[5]*10+a[6]
  c = c*60
  
  a[10] = int(a[10]) 
  a[11] = int(a[11])
  d = a[10]*10+a[11]
  
  b = b + c+ d

  return b


a = calcula_dia()
b = calcula_horas()
c = calcula_dia()
d = calcula_horas()

final = (c+d)-(a+b)

#########################################################

aux= final
final = int(final/(24*60*60))

print(str(final)+" dia(s)")

final = aux - final*(24*60*60)


#aaaaaaaaaaaa

aux = final
final = int(final/(60*60))

print(str(final)+" hora(s)")

final = aux - (final*60*60)

#aaaaaaaaaaaa

aux = final
final = int(final/(60))

print(str(final)+" minuto(s)")

final = aux - (final*60)

print(str(final)+" segundo(s)")