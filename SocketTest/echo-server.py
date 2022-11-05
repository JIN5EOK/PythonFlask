#서버 예제

import socket

HOST = "127.0.0.1" # localhost
PORT = 65432 # Port to listen on 수신포트 

#터미널에 python echo-server.py 입력

# with문 -> 자원을 획득하고 반납해야 하는 경우 주로 사용한다.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #AF_INET은 IPv4연결에 사용된다, IPv6 연결은 AF_INET6, SOCK_STREAM : 스트림, TCP 프로토콜 전송방식
    s.bind((HOST, PORT)) # 소켓에 사용할 주소값들, IPv4 연결이므로 HOST, PORT값이 필요하다.
    s.listen() # 클라이언트가 연결요청이 가능하도록 대기상태로 전환하는 함수, 백로그 매개변수로 정수값을 넣을 수 있는데 최대 연결 가능한 사용자 숫자를 의미함
    conn, addr = s.accept() # 연결 요청을 수락하는 함수, 누군가 접속하여 연결되면 새 소켓 개체와 클라이언트 주소를 포함하는 튜플이 반환된다.
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024) # conn.recv()가 빈 문자열 객체를 반환하면 연결이 끝났다는 의미이다.
            if not data:
                break
            conn.sendall(data) # 클라이언트에게 정보를 보낸다.