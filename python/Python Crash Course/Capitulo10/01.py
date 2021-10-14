'''
#10.1

file = 'learning_python.txt'

with open(file) as f:
    lines = f.read()
    print(lines)

print("###########")

with open(file) as g:
    for line in g:
        print(line)

print("###########")

with open(file) as h:
    lines = h.readlines()

for line in lines:
    print(line)
'''
#10.2

file = 'learning_python.txt'

with open(file) as f:
    lines = f.read()
    print( lines.replace('Python','C') )
