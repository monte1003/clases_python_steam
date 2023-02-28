from banco import Banco
felipe = Banco("Felipe")
felipe.ingresar_dinero(5)
print(felipe.monto_persona)
print(felipe.monto)
isaac = Banco("Felipe")
isaac.ingresar_dinero(5)
print(felipe.monto)