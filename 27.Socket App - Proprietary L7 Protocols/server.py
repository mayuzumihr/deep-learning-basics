# server.py

import sys
import socket
import threading

def client_worker(conn, client_ip):
  print(f"Connected by {client_ip}")
  try:
    while True:
      data = conn.recv(1024)
      if not data:
        break
      msg = data.decode()
      print(msg)
  finally:
    conn.close()
    print(f"Connection with {client_ip} closed.")

def server_controller(server_port):
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind(('0.0.0.0', server_port))
  server_socket.listen()
  print(f"Server listening on port {server_port}")
  try:
    while True:
      conn, client_ip = server_socket.accept()
      client_thread = threading.Thread(target=client_worker, args=(conn, client_ip))
      client_thread.start()
  finally:
    server_socket.close()

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python server.py <port>")
    sys.exit(1)
  
  server_port = int(sys.argv[1])
  server_controller(server_port)