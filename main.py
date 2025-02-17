import socket # this is used to connect between client and host
import time 
# class socket(
#     family: AddressFamily | int = -1, this is used to transfer -- ipv4 address
#     type: SocketKind | int = -1, -- synchronize concepts
#     proto: int = -1,
#     fileno: int | None = None
# )

socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) # this is used reuse address allow endpoint to reuse after socket  closed
# socket_server.setblocking(False)
server_host = "0.0.0.0"
server_port = 1730


# http - hyper text transfer protocol - 80
# https - hyper text transfer protocol traffic - 443 

socket_server.bind((server_host,server_port))  # this port can access any network
socket_server.listen(5) # this particular accepts the connection
print(f"listening the port {server_port} ...")

while True:
    
    client_socket, client_addr = socket_server.accept()
    # client_socket.sendall()
    req = client_socket.recv(1500).decode()
    # print(client_socket) #('127.0.0.1', 64760)
    # print(client_addr)
    # print(req)
    headers = req.split('\n')
    first_header_comp = headers[0].split()
    http_method = first_header_comp[0]
    path = first_header_comp[1]
    if http_method == 'GET':
        if path == '/':
            fin = open('index.html')
        elif path == '/book':
            fin = open('book.json')
        content = fin.read()
        fin.close() 
        response = 'HTTP/1.1 200 OK\n\n' + content       
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\nAllow: GET'


    client_socket.sendall(response.encode())
    client_socket.close()



socket_server.close()