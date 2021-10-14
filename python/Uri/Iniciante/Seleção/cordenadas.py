entrada = list(map(float, input().split()))

x = entrada[0]
y = entrada[1]

if x == 0 and y == 0:
    print("Origem")
elif x == 0 and y != 0:
    print("Eixo Y")
elif x != 0 and y == 0:
    print("Eixo X")
elif x>0 and y>0:
    print("Q1")
elif x>0 and y<0:
    print("Q4")
elif x<0 and y<0:
    print("Q3")
elif x<0 and y>0:
    print("Q2")
    
