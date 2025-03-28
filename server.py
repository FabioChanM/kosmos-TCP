import socket
import os
from dotenv import load_dotenv

load_dotenv() 

def iniciar_servidor():
    HOST = os.getenv('SERVER_HOST', 'localhost')  
    PORT = int(os.getenv('SERVER_PORT', '5000'))  
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor TCP escuchando en {HOST}:{PORT}")
        
        while True:
            conn, addr = s.accept()
            print(f"Nueva conexión desde {addr}")
            
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    
                    mensaje = data.decode().strip()
                    print(f"Mensaje recibido: {mensaje}")
                    
                    if mensaje.upper() == "DESCONEXION":
                        print(f"Desconexión solicitada por {addr}")
                        conn.sendall(b"Conexion cerrada por solicitud del cliente")
                        break
                    else:
                        respuesta = mensaje.upper()
                        conn.sendall(respuesta.encode())
                        print(f"Enviado: {respuesta}")
            
            print(f"Conexión con {addr} cerrada\n")

if __name__ == "__main__":
    iniciar_servidor()