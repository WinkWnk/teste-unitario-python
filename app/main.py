from funcionario import Funcionario 
import os
f1 = Funcionario("Pedro", "Cafetão", 100000) 

# print(f1.dados())  

# print(f1.registrarPonto())

# f1.descontarSalario(2000)

# print(f1.dados())  

print (f1.promover("Pastor", 305000))

print(f1.calcularBonus())

os.system("cls") #limpando a tela
print(f1.calcularBonus())