entrada = list( map( float, input().split() ) )

media = ( entrada[0]*2 + entrada[1]*3 + entrada[2]*4 + entrada[3]*1 ) /10

if media >= 7:
    print("Media: %.1f\nAluno aprovado." %media)
elif media < 5:
    print("Media: %.1f\nAluno reprovado." %media)
else:
    print("Media: %.1f\nAluno em exame." %media)
    try:
        qtd = float( input() )
    except:
        pass
    else:
        print("Nota do exame: %.1f" %qtd)
        media = (media+qtd)/2
        if media >= 5:
            print("Aluno aprovado.\nMedia final: %.1f" %media)
        else:
            print("Aluno reprovado.\nMedia final: %.1f" %media)
        