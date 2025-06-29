# ## problema 4
# una tupla

if not datos_estudiantes:
        return None, None  #  diccionario vacío

    promedios = {}
    for estudiante, notas in datos_estudiantes.items():
        if notas:  # Asegurarse de que la lista de notas no esté vacía
            promedios[estudiante] = sum(notas) / len(notas)
        else:
            promedios[estudiante] = 0  # O asignar un valor predeterminado si no hay notas

    estudiante_mas_alto = max(promedios, key=promedios.get)
    estudiante_mas_bajo = min(promedios, key=promedios.get)

    return estudiante_mas_alto, estudiante_mas_bajo

    # ## problema 5

       resultados = []
    for alumno in listado_alumnos:
        if nombre_buscado.lower() in (alumno['nombre'] + " " + alumno['apellido']).lower():
            # Calcular promedio
            promedio = sum(alumno['notas']) / len(alumno['notas']) if alumno['notas'] else 0
            # Crear un nuevo diccionario con el promedio
            alumno_con_promedio = alumno.copy()
            alumno_con_promedio['promedio'] = promedio
            resultados.append(alumno_con_promedio)
    return resultados
