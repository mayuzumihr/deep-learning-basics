# client.py

import sys
import socket

def client_controller(server_ip, server_port):
  try:
    while True:
      user_id = input("ユーザー名を入力してください >>> ")
      if (user_id == "#quit"):
        break
      password = input("パスワードを入力してください >>> ")
      if (password == "#quit"):
        break
      
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client_socket.connect((server_ip, server_port))

      payload = f"user_id={user_id}&password={password}"

      request = (
        f"POST /result HTTP/1.1\r\n"
        f"Host: {server_ip}:{server_port}\r\n"
        f"User-Agent: AI-Web HTTP Practice\r\n"
        f"Accept-Encoding: gzip, deflate\r\n"
        f"Accept: */*\r\n"
        f"Connection: close\r\n"
        f"Content-Length: {len(payload)}\r\n"
        f"Content-Type: text/plain\r\n"
        f"\r\n"
        f"{payload}"
      )

      client_socket.sendall(request.encode())
      print("Client : Request message has been sent.\r\n")

      response = client_socket.recv(1024).decode()
      print(response)

      client_socket.close()

  except Exception as err:
    print(err.args)

if __name__ == "__main__":
  if len(sys.argv) != 3:
      print("Usage: python client.py <server_ip> <server_port>")
      sys.exit(1)
  
  server_ip = sys.argv[1]
  server_port = int(sys.argv[2])
  client_controller(server_ip, server_port)