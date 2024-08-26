from te import Tea
from time import sleep
from tqdm import tqdm
from pagos import pago


te = Tea()
te.clean()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print('@          My Flavour Tea              @')
print('@      Bienvenido al asistente.        @')
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print()
tipo = int(input('''Por favor, elija su preferencia?
    1 - Té negro
    2 - Té verde
    3 - Infusión de hierbas    
> '''))

teatype = te.validador([1, 2, 3], tipo)
te.clean()

cantidad = int(input('''Por favor, elija su preferencia?
    1 - 300 gr
    2 - 500 gr    
> '''))

gramos = te.validador([1, 2], cantidad)
te.clean()

pago(teatype, gramos)