import socket

Udp_Socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
Udp_Socket.bind(("192.168.0.3",8080))
Recv_Data = Udp_Socket.recvfrom(1024)
Recv_Msg = Recv_Data[0]
Sender_Addr = Recv_Data[1]

print(Recv_Data)
print(Sender_Addr)