import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.2"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) #utf-8 인코딩
    msg_length = len(message) # 송신할 메시지의 길이
    send_length = str(msg_length).encode(FORMAT) # msg_length를 문자열로 변환하고 utf_8로 인코딩한다.
    send_length += b' ' * (HEADER - len(send_length)) # 헤더가 64바이트이므로 길이를 맞춤
    client.send(send_length) # 송신할 메시지의 길이를 보낸다
    client.send(message) # 메시지를 송신한다
    print(client.recv(2048).decode(FORMAT))

send("Hello 1!")
send("Hello 2!!")
send("Hello 3!!!")
input()
print("Press any key to Disconnect")
send(DISCONNECT_MESSAGE)