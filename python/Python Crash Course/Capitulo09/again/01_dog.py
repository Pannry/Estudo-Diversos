def Classe():
    """Classes:
        -Uma função que faz parte de uma classe é um metodo.
        -O parametro self é obrigatorio e deve estar antes de qualquer parametro.
        -Qualquer variavel prefixada em self está disponivel a todos os métodos da classe.
        -Variaveis acessiveis por meio de instâncias, são chamadas de atributos.
    """

class Dog():
    """Uma tentativa simples de modelar um cachorro."""

    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando"""
        print(self.name.title()+" rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog name is "+ my_dog.name.title()+'.')
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()

print("My dog name is "+ your_dog.name.title()+'.')
print("My dog is "+str(your_dog.age)+" years old.")
your_dog.sit()