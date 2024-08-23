#!/usr/bin/env python3
import socket
import threading

def client_thread(client_socket, clients, usernames):
    
    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username
    
    print(f"\n[+] El usuario {username} se ha conectado al chat")
    
    for client in clients:
        if client is not client_socket:
            client.sendall(f"\n[+] El usuario {username} ha entrado al chat\n\n".encode())
            
    while True:
        try:
            message = client_socket.recv(1024).decode()
            
            if not message:
                break
            
            if message == "!usuarios":
                client_socket.sendall(f"\n[+] Listado de usuarios disponibles: {', '.join(usernames.values())}\n\n".encode())
                continue
                
            for client in clients:
                if client is not client_socket:
                    message.sendall(f"{message}\n".encode())
                
        except:
            break 
        
    client_socket.close() # Cerramos el socket del cliente que cierra la ventana
    clients.remove(client_socket) 
    del usernames[client_socket] # para eliminar al usuario del diccionario de usuarios
         

def server_program():
    
    host = 'localhost'
    port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TIME_WAIT
    server_socket.bind((host,port))
    server_socket.listen() # para ponernos en escucha de conexiones entrantes
    
    print(f"\n[+] El servidor está en escucha de conexiones entrantes...")    
    
    clients = []
    usernames = {}
    
    while True:
        
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        
        print(f"\n[+] Se ha conectado un nuevo cliente: {address}")
    
        thread = threading.Thread(target=client_thread, args=(client_socket, clients, usernames)) # Para que acepte nuevas conexiones de clientes
        thread.daemon = True # Esto es como ponerlo en segundo plano y cuando se cierra el programa este no se quede como colgado
        thread.start()
        
    server_socket.close()

if __name__ == '__main__':
    server_program()