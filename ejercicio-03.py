'''Se está dando lugar el Festival de Cine de San Sebastián. 
Tienes el abono completo y quieres ver tantas películas como puedas. 
Dispones de todos los horarios con la hora a la que empieza y acaba cada película. 
¿Cuántas películas puedes ver como máximo?'''

# definiciones previas
def contar_pelis(lista_horarios):
    lista_horarios.sort()  # ordenamos la lista de horarios
    contador = 0  #  las pelis que vemos
    h = 0  # variable donde vamos a ir guardando las horas de fin
    for h_inicio, h_fin in lista_horarios:
        if h_inicio >= h:  # si h_inicio es después de la h_fin de la anterior peli
            contador += 1  # podemos verla
            h = h_fin  # actualizamos la hora de fin
            
    return contador


# CODIGO EJECUTABLE ------------------------------------------------------------------
n = int(input())  # numero de peliculas

horarios_pelis = []

for i in range(n):
    a, b = map(int, input().split())  # a: hora de inicio, b: hora de fin
    horarios_pelis.append( (a, b) )

print(f'Va poder ver {contar_pelis(horarios_pelis)} películas')
    
