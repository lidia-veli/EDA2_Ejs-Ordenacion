'''Hay n niños que quieren subir a una noria, 
y tu tarea es encontrar una góndola para cada niño.
Cada góndola puede tener uno o dos niños, y además, 
el peso total en una góndola no puede exceder x. Conoces el peso de cada niño.
¿Cuál es el número mínimo de góndolas necesarias para los niños?'''

# definiciones previas
def asignar_gondolas(lista_p, p_max):
    '''empareja a los niños en gondolas de forma que el peso de cada gondola no supere el peso maximo
    Vamos a rodenar la lista de menor a mayor y a ir emparejando por los extremos, 
    con la condición de que siempre el peso total sea inferior al peso maximo de la góndola.
    Si hay alguno que no puede ir en pareja, va solo.
    '''
    list = lista_p.copy()  # copiamos la lista de pesos
    list.sort()  # ordenamos la lista de pesos
    lista_g = []  # lista de gondolas

    for x in list:
        for y in list[::-1]:
            if x + y <= p_max:  # si la suma de los pesos es menor que el peso maximo
                lista_g.append( (x, y) )  # pueden ser pareja
                # y los quitamos de la lista
                list.remove(x)
                list.remove(y)
                break  # pasamos ala siguiente iteracion del primer for

            else:  # si no pueden ser pareja, sabemos que es porque 'y' es grande, entonces va solo
                lista_g.append(y)
                list.remove(y)

    if len(list) > 0: # si queda algún niño suelto, que vaya solo
        lista_g.append(list[0])

    return len(lista_g)  # devolvemos el numero de gondolas que se van a usar



# CÓDIGO EJECUTABLE ---------------------------------------------------------------

n, x = map(int, input().split())
    # n: numero de niños
    # x: peso maximo de la gondola
pesos = list(map(int, input().split()))  # lista de pesos de los niños

print(f'Debe haber un mínimo de {asignar_gondolas(pesos, x)} góndolas')

