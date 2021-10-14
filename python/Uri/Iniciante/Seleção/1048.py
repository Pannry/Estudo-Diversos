n = float( input() )

def printmsg(ns, re, pp):
  print("Novo salario: %.2f" %ns )
  print("Reajuste ganho: %.2f" %re )
  print("Em percentual: "+str(int(pp))+" %")


if 0 <= n <= 400.00:
  pp = 0.15
  i = n*pp
  ns = n + i
  printmsg(ns, i, pp*100)
  
if 400.00 < n <= 800.00:
  pp = 0.12
  i = n*pp
  ns = n + i
  printmsg(ns, i, pp*100)

if 800.00 < n <= 1200.00:
  pp = 0.10
  i = n*pp
  ns = n + i
  printmsg(ns, i, pp*100)

if 1200.00 < n <= 2000.00:
  pp = 0.07
  i = n*pp
  ns = n + i
  printmsg(ns, i, pp*100)

if n > 2000.00:
  pp = 0.04
  i = n*pp
  ns = n + i
  printmsg(ns, i, pp*100 )