class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.ativo = False 
               
                 
    def somar_numeros(self):
        return self.numero1 + self.numero2

    def subtrair_numeros(self):
        return self.numero1 - self.numero2
    
    def multiplicacao_numeros(self):
        return self.numero1 * self.numero2
    
    def divisao_numero(self):
        if self.numero2 == 0:
            return "Não e possivel dividir por 0"
        else:
            return self.numero1 / self.numero2      
  
                         
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
        
guarda_numero = Calculadora(numero1, numero2)

operador = str(input('Escolha Soma, Subtração, Multiplicação e Divisão, para fazer o calculo: \n'))
if operador == '+':
 print("Soma:", guarda_numero.somar_numeros())        
elif operador == '-':
 print("Subtração:", guarda_numero.subtrair_numeros())
elif operador == '*':
 print("Multiplicação:", guarda_numero.multiplicacao_numeros()) 
elif operador == '/':
 print("Divisão:", guarda_numero.divisao_numero())
 