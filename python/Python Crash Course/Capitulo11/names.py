from name_function import get_formatted_name

print("Digite 'q' para sair")
while True:
    first =  input("Primeiro nome: ")
    if first == q:
        break
    last =  input("Ultimo nome: ")
    if last == q:
        break
    
    formatted_name = get_formatted_name(first, last)
    print("Nome formatado: "+formatted_name+".")