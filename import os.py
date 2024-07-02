import os
import time

menu=1
descuento= 0
precios = 0

PR=0
OR=0
PVR=0
AER=0

PR=int(4500)
OR=int(5000)
PVR=int(5200)
AER=int(4800)

limpiar="cls"
os.system(limpiar)

while True:
    print(f'---------menu---------')
    print(f'Pikachu Roll:4500')
    print(f'Otaku Roll:5000')
    print(f'Pulpo Venenoso Roll:5200')
    print(f'Anguila Electrica Roll:4800')
    print(f'Volver al inicio')
    Orden= int(input("seleccione los rolls que desee"))
    if Orden==1:
        PR +=1
        print('Pikachu Roll se agregado a la lista')
        time.sleep(3)
        os.system(limpiar)
    elif Orden==2:
        OR +=1
        print('Otaku Roll se agrego a la lista')
        time.sleep(3)
        os.system(limpiar)
    elif Orden==3:
        PVR +=1
        print('Pulpo Venenoso Roll se agrego a la lista')
        time.sleep(3)
        os.system(limpiar)
    elif Orden==4:
        AER +=1
        print('Anguila Electrica roll se agrego a la lista ')
        time.sleep(3)
        os.system(limpiar)
    elif Orden==5:
        print('su oreden esta lista, crearemos su boleta')
        time.sleep(3)
        os.system(limpiar)
        break
    else:
        print("por favor, ingrese una opcion")
        time.sleep(3)
        os.system(limpiar)

TotalPedido=(PR + OR + PVR + AER)

while menu==2:
    codigo=print('ingrese su cupon de descuento (si no posee uno ponga "no")')
    if codigo== "soyotaku":
        descuento=0.10
        menu+=1
        time.sleep(3)
        os.system(limpiar)
    elif codigo== "no":
        menu +=1
        descuento= 0
        print("Deacuerdo,ingresando en la boleta")
        time.sleep(3)
        os.system(limpiar)
    else:
        print('por favor ingrese alguna opcion')
        time.sleep(3)
        os.system(limpiar)

Valordesc = (descuento* precios)   
Valorsindesc =(descuento - precios)

print(f'---------menu---------')
print(f'Pikachu Roll:{PR}')
print(f'Otaku Roll:{OR}')
print(f'Pulpo Venenoso Roll:{PVR}')
print(f'Anguila Electrica Roll:{AER}')
    