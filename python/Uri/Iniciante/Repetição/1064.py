positivo = 0
media = 0

for i in range(0, 6):
  a= float(input())
  
  if a > 0:
    positivo +=1
    media += a

print(str(positivo)+" valores positivos")
try:
  print( "%.1f" %(media/positivo) )
except ZeroDivisionError:
  print("-non")