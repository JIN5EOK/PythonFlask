import socket
import threading
import time

DISCONNECT_MESSAGE = "!DISCONNECT"
HEADER = 64
PORT = 5050 # 다른 용도로 사용되지 않는 포트로 설정하도록 한다.
SERVER = socket.gethostbyname(socket.gethostname()) # 호스트 이름을 통해 아이피를 얻는다
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4연결, 소켓 스트림
server.bind(ADDR) # bind함수를 통해 주소 정보를 전달한다.

def handle_client(conn, addr):
    # 연결 시작
    print("[NEW CONNECTION] {addr} connected.") #
    connected = True 
    while connected: #연결이 된 동안
        msg_length = conn.recv(HEADER).decode(FORMAT) # HEADER 만큼의 바이트의 데이터를 받아와 디코딩
        if msg_length: #msg_length가 NULL이 아닐경우 (NULL값일때 int를 정수형으로 변환하면 에러 발생하므로)
            msg_length = int(msg_length) # msg_length를 정수형으로 변환
            msg = conn.recv(msg_length).decode(FORMAT) # meg_length만큼 받아와서 디코딩
            if msg == DISCONNECT_MESSAGE: # DISCONNECT_MESSAGE 수신할 경우
                connected = False #연결을 끊는다.
            print(f"[{addr}] {msg}") #수신한 msg 출력한다
            conn.send("Msg received".encode(FORMAT))
    conn.close()
    
def start():
    server.listen() #listen() 함수를 통해 연결 수신상태로 변경한다.
    print(f"[LISTENING] Server is listening on {server}")
    while True:
        conn, addr = server.accept()
        # accept() 함수는 소켓, 주소정보로 구성되는 튜플을 리턴한다
        # 이때 생성된 소켓은 처음생성된 소켓과는 '별개의 객체'로 클라이언트와 연결이 구성되어 실제로 데이터를 주고받을 수 있는 창구가 된다.
        # 이 소켓은 연결이 들어와서 listen(), accept()가 호출될 때 마다 생성될 수 있으므로 연결이 구성된 소켓을 멀티스레드로 처리한다면 1:N의 처리도 가능하다.
        thread = threading.Thread(target=handle_client, args=(conn,addr)) # 쓰레드로 실행할 target 함수, 매개변수 
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}") # 현재 실행중인 쓰레드 개수 출력

print("[STARTING] server is starting...")
start()