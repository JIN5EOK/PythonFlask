import sys
import socket
import selectors
import types

def accept_wrapper(sock):
    conn, addr = sock.accept() # 소켓으로부터 연결을 받아들인다, 소켓,주소정보로 구성되는 튜플을 리턴한다.
    print(f"Accepted connection from {addr}") # 연결되었음을 출력한다.
    conn.setblocking(False) # 소켓을 비차단 모드로 전환한다.
    data = types.SimpleNamespace(addr = addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE # 읽기 가능, 쓰기 가능
    sel.register(conn, events, data=data) # 셀렉터에 등록시킴

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024) #1024바이트 길이만큼 데이터를 받아옴
        
        


sel = selectors.DefaultSelector()
host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False) # 에코 서버와의 가장 큰 차이점, setblocking(False)를 통해 소켓을 비차단 모드로 구성한다.
sel.register(lsock, selectors.EVENT_READ, data=None) # sel.select()로 모니터링할 소켓을 등록, 수신 소켓의 경우 읽기 이벤트인 selectors.EVENT_READ가 필요
#소켓과 함께 원하는 임의의 데이터를 저장하려면 data 인자를 사용, select()가 반환될 때 반환된다.

try:
    while True:
        events = sel.select(timeout = None) # I/O를 위한 소켓이 준비될때까지 기다린다.
        for key, mask in events: # events는 각 소켓에 대해 키와 마스크 튜플을 반환한다.
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key,mask)
except KeyboardInterrupt: # 코드 실행중 Ctrl+C를 누르면 발생하는 오류 예외처리
    print("Caught Keyboard interrupt, exiting")
finally:
    sel.close()
    