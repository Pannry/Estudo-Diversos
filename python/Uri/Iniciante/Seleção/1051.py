total_inicial = float( input() )

# Taxas
t = ["Isento", 0.08, 0.18, 0.28]
# Rendas
r = [2000.00, 3000.00, 4500.00]

#////////////////////////////////////
def taxa1(total, minimo, taxa):
  total = total - minimo
  total_final = total*taxa
  print("R$ %.2f" %total_final )
  
#////////////////////////////////////
def taxa2(total, minimo, taxa):
  total = total - minimo 
  total_final = total*taxa + ( (r[1]-r[0])*0.08 )# e somar com 8% de 1000
  print("R$ %.2f" %total_final )
  
#////////////////////////////////////
def taxa3(total, minimo, taxa):
  total = total - minimo
  total_final = total*taxa + ( (r[1]-r[0])*0.08 ) + ( (r[2]-r[1])*0.18 )# e somar com 18% de 1500 + 8% de 1000
  print("R$ %.2f" %total_final )


#////////////////////////////////////
if total_inicial < r[0]:
  print( t[0] )
  
elif r[0] < total_inicial <= r[1]:
  taxa1(total_inicial, r[0], t[1])

elif r[1] < total_inicial <= r[2]:
  taxa2(total_inicial, r[1], t[2])
  
elif total_inicial > r[2]:
  taxa3(total_inicial, r[2], t[3])
