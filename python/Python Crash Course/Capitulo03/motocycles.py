#Lista vazia, útil para o usuário adicionar as informações
motocycles = []

#
#   INSERÇÃO NA LISTA
#

#.append(string_value) -> adicionar elementos no final da lista 
motocycles.append("Honda")
motocycles.append("Yamaha")


print(motocycles)

#.insert(position, value) -> adiciona um valor em uma posição determinada 
motocycles.insert(1, "Suzuki")
motocycles.insert(3, "Dukati")

print(motocycles)

#
#   DELEÇÃO NA LISTA
#

# del variable[indice] -> deleta o valor de uma lista, sem armazena-lo   

del motocycles[2]
print(motocycles)

# .pop() -> Remove elemento com armazanamento
    # sem parametros: remove o ultimo elemento da lista.
    # com parametros: remove elemento em determinada posição

motocycles = ['Honda', 'Suzuki', 'Yamaha', 'Dukati'] 

motocycles.pop()
motocycles.pop(2)

print(motocycles)

#.remove(value) -> Remove um elemento pelo valor dentro da lista

motocycles = ['Honda', 'Suzuki', 'Yamaha', 'Dukati']
print(motocycles)

too_expensive = 'Dukati'

motocycles.remove(too_expensive)
print(motocycles)

print(too_expensive+" is too expensive for me")

#OBS: .remove(value) apenas remove o primeiro elemento do vetor
#para remover todos, precisa ser executado dentro de um loop

#.sort()        -> organiza lista permanentemente
#sorted(value)  -> retorna a lista organizada temporariamente
#.reverse()     -> troca os valores da lista
#len(variable)  -> retorna o tamanho da lista

