# app.py

import sys
from flask import Flask, request

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def result():
  json_data = request.get_json()
  user_id = json_data.get('user_id')
  password = json_data.get('password')
  print(json_data)
  print(f"user_id : {user_id}")
  print(f"password : {password}")
  return ("Server : Message received successfully.\r\n", 200)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python server.py <port>")
    sys.exit(1)
  
  server_port = int(sys.argv[1])
  app.run(host='0.0.0.0', port=server_port)