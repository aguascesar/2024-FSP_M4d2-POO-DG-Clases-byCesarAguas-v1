import os
import sys
op_sys = 'cls' if sys.platform == 'win32' else 'clear'

class Tea:
    #Atributos de Clase (Class Atribute)
    tipos = {
        "Negro": { 
            "tiempo": 3, 
            "recomendacion": "Se recomienda consumir al desayuno."},
        "Verde": {
            "tiempo": 5,
            "recomendacion": "Se recomienda consumir al medio día."},
        "Hierbas": {
            "tiempo": 6,
            "recomendacion": "Se recomienda consumir al atardecer."}
    }
    
    precios = {"300 gr": 3000, "500 gr": 5000 }


    @staticmethod
    def preparacion(sabor):
        match sabor:
            case 1:
                tipo= "Té negro"
                tiempo= Tea.tipos.get("Negro").get("tiempo")
                recomendacion= Tea.tipos.get("Negro").get("recomendacion")
            case 2:
                tipo= "Té verde"
                tiempo= Tea.tipos.get("Verde").get("tiempo")
                recomendacion= Tea.tipos.get("Verde").get("recomendacion")
            case 3:
                tipo = "Agua de hierbas"
                tiempo= Tea.tipos.get("Hierbas").get("tiempo")
                recomendacion= Tea.tipos.get("Hierbas").get("recomendacion")   

        return tipo, tiempo, recomendacion
    

    @staticmethod
    def precio(valor):
        match valor:
            case 1:
                tipo="300 gr"
                value=Tea.precios.get("300 gr")
            case 2:
                tipo="500 gr"
                value=Tea.precios.get("500 gr")

        return value,tipo

    @staticmethod
    def validador(opciones, eleccion):
        while eleccion not in opciones:
            print('Por favor ingrese una alternativa:', opciones)
            eleccion = input('Ingrese la alternativa: ').lower()
        return eleccion

    @staticmethod
    def clean():
        os.system(op_sys)
        