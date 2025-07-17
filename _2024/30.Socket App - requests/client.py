# client.py

import sys
import requests

def client_controller(server_ip, server_port):
  while True:
    user_id = input("ユーザー名を入力してください >>> ")
    if (user_id == "#quit"):
      break
    password = input("パスワードを入力してください >>> ")
    if (password == "#quit"):
      break
    
    json_data = {
        "user_id": user_id,
        "password": password
    }

    url = f'http://{server_ip}:{server_port}/result'
    response = requests.post(url, json=json_data)
    print("Client : Request message has been sent.\r\n")
    print(response.text)

if __name__ == "__main__":
  if len(sys.argv) != 3:
      print("Usage: python client.py <server_ip> <server_port>")
      sys.exit(1)
  
  server_ip = sys.argv[1]
  server_port = int(sys.argv[2])
  client_controller(server_ip, server_port)