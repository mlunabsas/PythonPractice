# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from TestCases.FirstTest import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
global KM
KM = 11
exec(open("./TestCases/FirstTest.py").read())


printGlobal()
print(sum(3,9))


class Persona():

    apellido = "Febornete"

    def __init__(self,nombre):
        self.nombre = nombre
        self.peso = 23

    def saluda(self):
        print("Hello friend!")


p1 = Persona("Alberto")
p2 = Persona("Roberto")
#p1.apellido="Gomez"
#p2.apellido="Nuñez"
#Persona.apellido="Ramirez"
print(p1.nombre)
print(p1.apellido)
print(p1.peso)

print(p2.nombre)
print(p2.apellido)