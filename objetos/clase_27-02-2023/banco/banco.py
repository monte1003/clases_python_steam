class Banco():
    monto = 0
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.monto_persona = 0
    def ingresar_dinero(self,dinero):
        self.monto = self.monto + dinero
        self.monto_persona = self.monto_persona + dinero
        
