class Carro():
    def __init__(self,
                matricula:str,
                marca:str,
                kilometros:float,
                gasolina:float):
        self.matricula = matricula
        self.marca = marca
        self.kilometros = kilometros
        self.gasolina = gasolina
    
    def avanzar(self):
        kilo = float(input("Cuantos Kilometros avanzaste: "))
        kilometros_1 = self.kilometros + kilo
        gasolina_1 = self.gasolina - kilo
        if kilo >= self.gasolina and kilo>self.kilometros:
            print("GASOLINA OUT")
        
        else:
            print(f"Kilometros: {kilometros_1}")
            print(f"gasolina: {gasolina_1}") 
    
carrito = Carro("ISJ890","Ford",100,200)
carrito.avanzar()