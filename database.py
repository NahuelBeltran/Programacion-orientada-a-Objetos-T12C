import json
import csv
import os

class Database:
    def __init__(self, nombre_base):
        self.nombre_base=nombre_base

    def read_text (self):
        try:
            with open(self.nombre_base, 'r') as file:
                content:file.read() # type: ignore
                return content
        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception as e:
            print(f"Error al leer archivo:{e}")
    
    def write_text (self,content):
        try:
            with open(self.nombre_base, 'w') as file:
                file.write(content)
                print(f"archivo{self.nombre_base} escrito con exito")
        except Exception as e:
            print(f"error al escribir el archivo: {e}")

    def read_json(self):
        try:
            with open(self.nombre_base, 'r') as file:
                content:file.read() # type: ignore
                return content
        except FileNotFoundError:
            print("Archivo no encontrado")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo JSON")
        except Exception as e:
            print(f"Error al leer archivo:{e}")
    
    def write_json (self,data):
        try:
            with open(self.nombre_base, 'w') as file:
                json.dump(data,file,indent=4)
                print(f"archivo JSON {self.nombre_base} escrito con exito")
        except Exception as e:
            print(f"error al escribir el archivo: {e}")
    