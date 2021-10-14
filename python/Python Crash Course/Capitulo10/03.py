#10.6 10.7
'''
while True:
    var = input("Digite um número para saber seu quadrado: (q para sair)")
    if var == 'q':
        break
    try:
        var = int(var)*int(var)
    except ValueError:
        print("Digita essa porra direito, seu noob!")
    else:
        print( "O número digitado foi: "+ str(var) )
'''

#10.8
'''
def read_file_texts(file):
    print("\nLendo arquivos: "+ file)
    print("==========================")

    try:
        with open(file) as f:
            text = f.read()
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    else:
        print(text)


file = 'dogs.txt'
read_file_texts(file)

file = 'cats.txt'
read_file_texts(file)
'''
#10.9
'''
def read_file_texts(file):

    try:
        with open(file) as f:
            text = f.read()
    except FileNotFoundError:
        pass
    else:
        print("\nLendo arquivos: "+ file)
        print("==========================")
        print(text)


file = 'dogs.txt'
read_file_texts(file)

file = 'cats.txt'
read_file_texts(file)
'''
#10.10

def read_file_texts(file):

    try:
        with open(file) as f:
            text = f.read()

    except FileNotFoundError:
        pass
    else:
        print("\nLendo arquivos: "+ file)
        print("==========================")
        print( str( text.lower().count('the') ) +" palavras 'the' no arquivo " + file )


file = '1661.txt'
read_file_texts(file)