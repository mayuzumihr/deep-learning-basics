# server.py

import sys
import socket
import threading

def client_worker(conn, client_ip):
  print(f"Connected by {client_ip}")
  try:
    data = conn.recv(1024).decode()
    print(data)
    payload = "Server : Message received successfully.\r\n"
    response = (
      f"HTTP/1.1 200 OK\r\n"
      f"Content-Type: text/plain\r\n"
      f"Content-Length: {len(payload)}\r\n"
      f"Connection: close\r\n"
      f"\r\n"
      f"{payload}"
    )
    conn.sendall(response.encode())
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