from supabase import create_client
import os
from dotenv import load_dotenv
from Supabase_lib import EstadoActualDB, MedidasDB, SensoresDB
class Estado_actual:
    def __init__():
        pass
    

# Reemplaza con tus credenciales de Supabase
# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener URL y clave desde las variables de entorno
url = os.getenv("SUPABASE_URL")  # URL de la API de Supabase
key = os.getenv("SUPABASE_KEY")  # Clave pública de la API (anon key)
tabla_estado = EstadoActualDB(url, key)
tabla_medidas = MedidasDB(url, key)
tabla_sensores = SensoresDB(url, key)
# Crear el cliente de Supabase
estado = tabla_estado.leer_estado()["estado_id"]
medidas = tabla_medidas.leer_medidas_entre_timestamps("2025-03-25 00:00:00")
# result = tabla_sensores.insertar_sensor("caudalimetro_2", "Caudalimetro de la olla 1 a la olla 2/3")
# print(result)
result = tabla_medidas.insertar("caudalimetro_2", 0.5, "L/min")
print(result)
print(medidas)
print(estado)
# supabase = create_client(url, key)

# # Ejemplo de consulta: Leer datos desde una tabla llamada "personas"
# def leer_datos():
#     response = supabase.table('Estado_actual').select('*').execute()
#     print(response.data)  # Imprime los datos leídos de la tabla

# # Ejemplo de consulta: Insertar datos en una tabla llamada "personas"
# def insertar_datos(estado):
#     response = supabase.table('Estado_actual').insert([
#         {'estado_id': estado}
#     ]).execute()
#     print(response.data)  # Imprime la respuesta después de insertar

# # Llamadas de ejemplo
# leer_datos()
# insertar_datos(1)
