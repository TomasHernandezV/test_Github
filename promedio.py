Matriz=[
    [85,45,1,7,9],
    [12,52,9,151,56],
    [76,10,56,99,9] 
    ]

for lista in Matriz:
    maximo= max(lista)
    i_max= lista.index(maximo)
    minimo=min(lista)
    i_min=lista.index(minimo)
    print(f"El maximo es {maximo} que se encuentra en la columna {i_max}")
    print(f"El minimo es{minimo} que se encuentra en la columna {i_min}\n")

def calcular_promedio(lista):
    total=sum(lista)
    cantidad=len(lista)
    return total/ cantidad

mi_lista=[10,20,30,40,50]
promedio=calcular_promedio(mi_lista)
print(f"El promedio es: {promedio:.2f}")
