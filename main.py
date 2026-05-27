import os

# Definición de la clase Médica para empaquetar los datos
class Medico:
    def __init__(self, licencia, especialidad, hospital, experiencia):
        self.licencia = licencia
        self.especialidad = especialidad
        self.hospital = hospital
        self.experiencia = experiencia

    # Método para convertir los datos del objeto en una línea de texto CSV
    def a_cadena(self):
        return f"{self.licencia},{self.especialidad},{self.hospital},{self.experiencia}\n"

# --- Funciones de Gestión de Archivos ---

def guardar_archivo(lista_medicos):
    """Sobrescribe el archivo con la información actual de la lista."""
    archivo = open("losdoctores.txt", "w")
    for med in lista_medicos:
        archivo.write(med.a_cadena())
    archivo.close()

def cargar_archivo():
    """Carga datos del archivo si existe; si no, inicia lista vacía."""
    lista_temp = []
    # Verificamos si el archivo físico existe en el disco [6]
    if os.path.exists("losdoctores.txt"):
        archivo = open("losdoctores.txt", "r")
        for linea in archivo:
            linea = linea.strip()
            if linea != "":
                datos = linea.split(",")
                # CORRECCIÓN: Usamos índices 0, 1, 2 y 3 para 4 columnas [4]
                if len(datos) == 4:
                    nuevo_med = Medico(datos[0], datos[1], datos[2], datos[3])
                    lista_temp.append(nuevo_med)
        archivo.close()
    return lista_temp

# --- Inicio del Programa Principal ---

# El programa inicia cargando el archivo o con una lista vacía
medicos = cargar_archivo()

while True:
    print("\n" + "="*40)
    print("   SISTEMA DE MÉDICOS (PERSISTENTE)   ")
    print("="*40)
    print("1. Agregar médico")
    print("2. Listar médicos (Tabla)")
    print("3. Actualizar médico")
    print("4. Borrar médico")
    print("5. Salir")
    print("-" * 40)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n-- Registro de Nuevo Médico --")
        lic = input("Licencia Profesional: ")
        esp = input("Especialidad: ")
        hos = input("Hospital de adscripción: ")
        exp = input("Años de experiencia: ")

        nuevo = Medico(lic, esp, hos, exp)
        medicos.append(nuevo) # Guardar en memoria RAM [11]
        guardar_archivo(medicos) # Guardar en archivo de texto [12]
        print("\n[!] Médico guardado correctamente en 'losdoctores.txt'.")

    elif opcion == "2":
        if len(medicos) == 0:
            print("\n[IA]: No hay datos registrados todavía.")
        else:
            print("\n" + "-"*85)
            print(f"{'LICENCIA':<15} | {'ESPECIALIDAD':<20} | {'HOSPITAL':<30} | {'EXP':<5}")
            print("-" * 85)
            for m in medicos:
                print(f"{m.licencia:<15} | {m.especialidad:<20} | {m.hospital:<30} | {m.experiencia:<5}")
            print("-" * 85)

    elif opcion == "3":
        busqueda = input("\nIngrese la licencia del médico a actualizar: ")
        encontrado = False
        for m in medicos:
            if m.licencia == busqueda:
                print(f"Modificando médico: {m.licencia}")
                m.especialidad = input("Nueva Especialidad: ")
                m.hospital = input("Nuevo Hospital: ")
                m.experiencia = input("Nuevos Años de experiencia: ")
                guardar_archivo(medicos) # Actualizar archivo tras el cambio [13]
                encontrado = True
                print("\n[!] Datos actualizados con éxito.")
                break
        if not encontrado:
            print("\n[Error]: Licencia no encontrada.")

    elif opcion == "4":
        busqueda = input("\nIngrese la licencia del médico a eliminar: ")
        i = 0
        encontrado = False
        while i < len(medicos):
            if medicos[i].licencia == busqueda:
                del medicos[i] # Borrar de la lista [14]
                guardar_archivo(medicos) # Reflejar borrado en el archivo [15]
                encontrado = True
                print("\n[!] Registro eliminado del sistema.")
                break
            i += 1
        if not encontrado:
            print("\n[Error]: No se encontró el registro.")

    elif opcion == "5":
        print("\nCerrando sistema médico... ¡Hasta pronto!")
        break

    else:
        print("\n[!] Opción no válida.")