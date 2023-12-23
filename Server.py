import socket
import threading

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("localhost", 9090))

socket.listen()

client, address = socket.accept()

done = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done = True
    else:
        print(msg)
    client.send(input("Message: ").encode('utf-8'))
    
client.close()
socket.close()