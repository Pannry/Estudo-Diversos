def ave():
  a = input()
  if a == "carnivoro":
    print("aguia")
          
  elif a == "onivoro":
    print("pomba")

def mamifero():
  a = input()
  if a == "onivoro":
    print("homem")
          
  elif a == "herbivoro":
    print("vaca")


def vertebrado():
  a = input()
  if a == "ave":
    ave()
    
  elif a == "mamifero":
    mamifero()
    
#####################################################
def inseto():
  a = input()
  if a == "hematofago":
    print("pulga")
          
  elif a == "herbivoro":
    print("lagarta")

def anelideo():
  a = input()
  if a == "hematofago":
    print("sanguessuga")
          
  elif a == "onivoro":
    print("minhoca")


def invertebrado():
  a = input()
  if a == "inseto":
    inseto()
    
  elif a == "anelideo":
    anelideo()

#####################################################

def arvore0():
  a = input()
  if a == "vertebrado":
    vertebrado()
  
  elif a == "invertebrado":
    invertebrado()
    
arvore0()