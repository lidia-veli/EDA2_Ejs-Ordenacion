'''Eres profesor de una clase de la que te piden que pases asistencia. Cada alumno, según
llega a clase, confirma su asistencia y en la lista aparece su número identificador como un
entero. Sin embargo, el sistema es algo nuevo y a ratos vuelve a aparecer por error en la
lista un alumno ya registrado.
Tu objetivo es, dada la lista de identificadores A con longitud n, obtener el número de
identificadores únicos en ella sin hacer uso de estructuras adicionales (sets, listas, etc).'''

def contar_identificadores_unicos(lista, long):
    cont_unicos = long  # suponemos que todos son unicos
    cont_repetidos = 0  # contador de identificadores repetidos
    i = 0  # indice para recorrer la lista
    while i < long and cont_repetidos <= 1:  # para cada identificador de la lista
    # CONDICIONES
    # i < long: que no se salga de la lista
    # contador<=1: que no haya mas de un identificador repetido
    
        # buscamos si hay identificadore repetidos en el resto de la lista
        for j in range(i+1, long):
            if lista[i] == lista[j]:  # si hay alguno que coincide
                cont_repetidos += 1  # lo contamos
        i += 1  # pasa al siguiente identificador
    
    # salimos del while porque hay algún identificador repetido
    return cont_unicos-cont_repetidos


# CODIGO EJECUTABLE -------------------------------------------------------------------------

t = int(input())  # numero de casos de prueba
for _ in range(1, t*2, 2):
    n = int(input())  # numero de identificadores
    A = list(map(int, input().split()))  # lista de identificadores
    print(f'Hay {contar_identificadores_unicos(A, n)} identificadores únicos')
