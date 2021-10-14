names = ['igor', 'adam', 'brian', 'kraw', 'carmus', 'hector', 'eloin', 'Mardoc'] 

print("O boss matou todo mundo, so restaram dois na pt")

popped_player = names.pop(5)
print(popped_player+ ", vocẽ morreu.")

popped_player = names.pop(5)
print(popped_player+ ", vocẽ morreu.")

popped_player = names.pop()
print(popped_player+ ", vocẽ morreu.")

popped_player = names.pop(0)
print(popped_player+ ", vocẽ morreu.")

popped_player = names.pop(2)
print(popped_player+ ", vocẽ morreu.")

popped_player = names.pop(1)
print(popped_player+ ", vocẽ morreu.")

print(names)

print("O boss pegou "+names[0]+" e "+names[1]+" na saida")
del names[0]
del names[0]

print(names)

