# client.py

import sys
import socket

def client_controller(server_ip, server_port):
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect((server_ip, server_port))
  try:
    while True:
      msg = input(">>> ")
      if msg.lower() == '#quit':
        break
      client_socket.sendall(msg.encode())
  finally:
    client_socket.close()

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python client.py <server_ip> <server_port>")
    sys.exit(1)
  
  server_ip = sys.argv[1]
  server_port = int(sys.argv[2])
  client_controller(server_ip, server_port)