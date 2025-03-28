import socket
import os
from dotenv import load_dotenv

load_dotenv()  

def ejecutar_cliente():
    HOST = os.getenv('SERVER_HOST', 'localhost')  
    PORT = int(os.getenv('SERVER_PORT', '5000'))
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print(f"Conectado al servidor {HOST}:{PORT}")
            print("Escribe 'DESCONEXION' para terminar la conexión\n")
            
            while True:
                mensaje = input("Ingresa tu mensaje: ")
                s.sendall(mensaje.encode())
                
                if mensaje.upper() == "DESCONEXION":
                    print("Solicitando desconexión...")
                    break
                
                data = s.recv(1024)
                print(f"Respuesta del servidor: {data.decode()}")
                
        except ConnectionRefusedError:
            print("Error: No se pudo conectar al servidor. ¿Está ejecutándose?")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    ejecutar_cliente()