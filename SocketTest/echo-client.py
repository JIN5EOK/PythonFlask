# 클라이언트 예제
import socket

# 서버를 실행시킨 후 python echo-client.py 서버를 실행시킨 터미널과 다른 터미널에 입력.

HOST = "127.0.0.1" # 서버의 호스트 이름이나 IP주소
PORT = 65432  # 서버의 포트번호

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world") # 서버에게 데이터를 전송한다, send() 메소드의 경우 recv와 마찬가지로 보내는 바이트 수를 적어야 함
    data = s.recv(1024) # 서버의 데이터를 받아온다, 1024는 한번에 받아올 수 있는 데이터 양 (바이트)를 뜻함
    
print(f"Received {data!r}") # 서버에게 받은 데이터를 출력한다