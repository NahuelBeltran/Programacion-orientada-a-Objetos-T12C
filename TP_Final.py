# main.py
from importlib.resources import contents
from database import Database
import json
import csv

def mostrar_menu():
    print("\n--- Base de Datos Documental ---")
    print("1. Crear colección")
    print("2. Importar CSV a colección")
    print("3. Consultar documento en colección")
    print("4. Eliminar documento de colección")
    print("5. Listar todos los documentos en colección")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    db = Database("MiBaseDeDatos")
    class coleccion:
        def __init__(self, nombre_coleccion):
            if nombre_coleccion not in self.coleccion:
                self.nombre_coleccion=nombre_coleccion
                self.documentos={}
            else:
                print("Esa coleccion ya existe.")

        def agregar_documento(self, documento):
            self.documentos[documento.id] = documento

        def obtener_documento(self, doc_id):
            return self.documentos.get(doc_id, None)
        
        def eliminar_documento(self, doc_id):
                if doc_id in self.documentos:
                    del self.documentos[doc_id]

        def import_csv(self, ruta_csv):
            try:
                with open(ruta_csv, mode='r', newline='', encoding='utf-8') as archivo:
                    lector_csv = csv.DictReader(archivo)
                    for fila in lector_csv:
                        id_documento = fila['id']
                        documento = Documento(id_documento, contents)
                        self.agregar_documento(documento)
                print(f"CSV importado exitosamente a la colección '{self.nombre_coleccion}'.")
            except FileNotFoundError:
                print(f"Error: No se encontró el archivo '{ruta_csv}'.")
            except Exception as e:
                print(f"Error al importar el archivo CSV: {e}")

    class Documento:
                def __init__(self, id, contenido=None):
                    self.id = id
                    self.contenido = contenido if contenido is not None else {}
                
                def __str__(self):
                    return f"documento(id={self, id}, contenido={self.contenido})"

    def Input_Issue():
        NUUM:input
        try:
            numero=int(NUUM)
            return numero
        except ValueError:
            try:
                numero=float(NUUM)
                return numero
            except ValueError:
                return "error"

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            db.create_collection(nombre_coleccion)
            print(f"Colección '{nombre_coleccion}' creada.")
        
        elif opcion == "2":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            collection = db.get_collection(nombre_coleccion)
            ruta_csv = input("Ingrese la ruta del archivo CSV: ")
            collection.import_csv(nombre_coleccion, ruta_csv)

        
        elif opcion == "3":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            doc_id = input("Ingrese el ID del documento: ")
            coleccion = db.get_collection(nombre_coleccion)
            if coleccion:
                documento = coleccion.get_document(doc_id)
                if documento:
                    print("Documento encontrado:")
                    print(documento)
                else:
                    print("Documento no encontrado.")
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
        elif opcion == "4":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            doc_id = input("Ingrese el ID del documento a eliminar: ")
            coleccion = db.get_collection(nombre_coleccion)
            if coleccion:
                coleccion.delete_document(doc_id)
        
        elif opcion == "5":
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.get_collection(nombre_coleccion)
            if coleccion:
                documentos = coleccion.list_documents()
                if documentos:
                    print("\n--- Lista de Documentos ---")
                    for doc in documentos:
                        print(doc)
                        print("-----------")
                else:
                    print("No hay documentos en la colección.")
        
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()