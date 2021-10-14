def msg(qtd):
    print("Total: R$ %.2f" %qtd)

def cardapio(menu, qtd):
    if menu == 1:
        qtd = 4.00*qtd
        msg(qtd)
    elif menu == 2:
        qtd = 4.50*qtd
        msg(qtd)
    elif menu == 3:
        qtd = 5.00*qtd
        msg(qtd) 
    elif menu == 4:
        qtd = 2.00*qtd
        msg(qtd)
    elif menu == 5:
        qtd = 1.50*qtd
        msg(qtd)



entrada = list( map( float, input().split() ) )

a = cardapio(entrada[0], entrada[1])