from supabase import create_client
from datetime import datetime

class BaseSupabaseDB:
    def __init__(self, url, key):
        """Inicializa una única conexión a Supabase"""
        self.supabase = create_client(url, key)

    def leer(self, tabla, filtro, valor):
        """Lee un registro filtrado por un campo específico"""
        try:
            response = self.supabase.table(tabla).select('*').eq(filtro, valor).execute()
            return response.data if response.data else None
        except Exception as e:
            print(f"Error al leer en {tabla}: {e}")
            return None

    def insertar(self, tabla, datos):
        """Inserta un nuevo registro en la tabla"""
        try:
            response = self.supabase.table(tabla).insert([datos]).execute()
            return response.data
        except Exception as e:
            print(f"Error al insertar en {tabla}: {e}")
            return None

    def eliminar(self, tabla, filtro, valor):
        """Elimina un registro filtrado por un campo específico"""
        try:
            response = self.supabase.table(tabla).delete().eq(filtro, valor).execute()
            return response.count
        except Exception as e:
            print(f"Error al eliminar en {tabla}: {e}")
            return 0


class EstadoActualDB(BaseSupabaseDB):
    def __init__(self, url, key):
        super().__init__(url, key)  # Usa el cliente Supabase de la clase base
        self.tabla = "Estado_actual"

    def leer_estado(self):
        try:
            response = self.supabase.table(self.tabla).select('*').order("created_at", desc=True).limit(1).execute()
            # json = response.data[0].json()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Error al leer la última fila de {self.tabla}: {e}")
            return None

    def insertar_estado(self, estado_id):
        return self.insertar(self.tabla, {"estado_id": estado_id})

    def eliminar_estado(self, id):
        return self.eliminar(self.tabla, "id", id)
    
class MedidasDB(BaseSupabaseDB):
    def __init__(self, url, key):
        super().__init__(url, key)
        self.tabla = "Medidas"
    
    def leer_medidas_entre_timestamps(self, timestamp_inicio, timestamp_fin=None):
        """Lee medidas entre dos timestamps en la tabla 'medidas'."""

        if timestamp_fin is None:
            timestamp_fin = datetime.utcnow().isoformat()  # Timestamp actual en formato ISO 8601

        try:
            response = (
                self.supabase.table(self.tabla)
                .select('*')
                .gte("created_at", timestamp_inicio)  # Mayor o igual al inicio
                .lte("created_at", timestamp_fin)  # Menor o igual al fin
                .order("created_at", desc=False)  # Orden ascendente
                .execute()
            )
            return response.data if response.data else []
        except Exception as e:
            print(f"Error al leer medidas entre {timestamp_inicio} y {timestamp_fin} en {self.tabla}: {e}")
            return []
        
    def insertar(self, sensor, medida, unidad = None):
        response = (self.supabase.table("Sensores")
                     .select('id')
                     .eq("Nombre", sensor)
                     .execute())
        if not response.data:
            print(f"Error: Sensor '{sensor}' no encontrado.")
            return None
        id_sensor = response.data[0]["id"]
        datos = {
            "id_sensor": id_sensor,
            "Medida":float(medida),
            "Unidad": unidad
        }
        return super().insertar(self.tabla, datos)
    

class SensoresDB(BaseSupabaseDB):
    def __init__(self, url, key):
        super().__init__(url, key)
        self.tabla = "Sensores"
    
    def insertar_sensor(self, nombre, descripcion):
        datos = {
            "Nombre": nombre,
            "Descripción": descripcion
        }
        return super().insertar(self.tabla, datos)
