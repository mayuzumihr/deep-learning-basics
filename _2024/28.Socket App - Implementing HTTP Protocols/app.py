# app.py

import sys
from flask import Flask, request

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def result():
  data = request.data.decode()
  print(data)
  return ("Server : Message received successfully.\r\n", 200)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python server.py <port>")
    sys.exit(1)
  
  server_port = int(sys.argv[1])
  app.run(host='0.0.0.0', port=server_port)