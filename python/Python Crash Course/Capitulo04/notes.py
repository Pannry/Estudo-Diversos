# for em strings
strings = ["Aaaaa", "Bbbbb", "Ccccc"]

for string in strings:
    print( string )

#for em numeros
nums = [1,2,3]

for num in nums:
    print(num)

#range(start, stop, step) -> Exemplos da função range

numbers = list( range(1,6) )
print( numbers )
# ?- [1, 2, 3, 4, 5]

numbers = list( range( 1, 11, 3 ) )
print( numbers )
# ?- [1, 4, 7, 10] 

#List comprehensions
squares = [ value**2 for value in range(1,11) ]
print (squares)

min(lista)  #menor numero da lista
max(lista)  #maior numero da lista
sum(lista)  #soma dos  numeros da lista


# Lista comum se da na forma:
strings = ["Aaaaa", "Bbbbb", "Ccccc"]

#Tuplas se dao na forma:
strings = ("Aaaaa", "Bbbbb", "Ccccc")
#uma tupla é uma lista que nao se da para alterar na vida do programa, 
#ele gera uma mensagem de erro.

#Apenas da para alterar os valores se alterar toda a tupla
strings = ("Ddddd", "Eeeee", "Fffff")