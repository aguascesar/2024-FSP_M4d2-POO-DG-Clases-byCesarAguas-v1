#pip install tqdm
from time import sleep
from tqdm import tqdm
import os
import sys
from te import Tea

def pago(teatype, gramos):
    while True:

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Como desea cancelar su Té?")
        print()
        print(f"1 - Efectivo ")
        print(f"2 - Debito ")
        print(f"3 - Credito ")
        print(f"4 - Cheque ")

        pagar = int(input("\nElija una de las opciones [1/2/3/4]"))
        valido = Tea.validador([1, 2, 3, 4], pagar)
        Tea.clean()

        #   Ejecucion de rutinas
        nombre, cuantos, recomendacion = Tea.preparacion(teatype)
        precio, tipo = Tea.precio(gramos)

        if valido != "":
            #   Mostrar resultados
            print("_____") 
            print(" \_&_/ Ticket de compra")
            print(" (n_n) No valido como boleta")
            print("<) )\_")
            print(f" | |   Total Pedido: $ {precio}")
            print(f" |_|_  \n")
            print()

            for i in tqdm(range(5)):
                sleep(1)

            Tea.clean()
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print(f"Preferencia  : {nombre}")
            print(f"Formato : {tipo}")
            print(f"Precio : $ {precio}")
            print(f"Preparación  : {cuantos} minutos")
            print(f"Recomendación: {recomendacion}")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print()
            print("\n ¡Provecho!")
            print()
            print("  \_(n_n)_/")      
            print()

            break
        else:
            print(f"Por favor elija una forma de pagar, adecuada.")


