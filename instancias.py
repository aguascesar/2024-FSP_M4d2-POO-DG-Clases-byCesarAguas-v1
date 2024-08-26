from te import Tea

instancia=type(Tea())
objeto=type(Tea())


if instancia == objeto :
    print(f"Instancias Iguales: {instancia}, {objeto}")
else:
    print("Objetos distintos")