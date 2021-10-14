meses = ("Janeiro","Fevereiro","Março",
         "Abril","Maio","Junho","Julho",
         "Agosto","Setembro","Outubro",
         "Novembro","Dezembro")

mes1 = "março"

if mes1.title() in meses:
    print("Parabens!")

#################
#
#   next
#
#################

def fib(n):
    return (n in (0,1) and [n] or [fib(n-1) + fib(n-2)])[0]

sequence = [fib(i) for i in range(1,11)]
print( sequence )

n1 = 12
n2 = 13

if n1 in sequence:
    print(str(n1)+" está na lista!")

if n1 not in sequence:
    print(str(n1)+" não está na lista!")

if n2 in sequence:
    print(str(n2)+" é está na lista!")

if n2 not in sequence:
    print(str(n2)+" não está na lista!")