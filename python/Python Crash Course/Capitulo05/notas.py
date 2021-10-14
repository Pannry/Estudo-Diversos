#if

a = 10
b = 15

print( a> b)

print( b > a )

print( ( a > b ) and ( b > a ) )

print( ( a > b ) or ( b > a ) )

############################################################

names = ['adam', 'brian', 'carmus', 'darius', 'eloin']
nm1 = "adam"
nm2 = "leon"

print( nm1 in names )
print( nm2 in names )

if nm1 in names:
    print(nm1.title()+ " pertence a lista")

if nm2 not in names:
    print(nm2.title()+ " não pertence a lista")


##################################################
"""
if:

elif:

elif:

else:

"""