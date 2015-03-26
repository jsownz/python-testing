import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9998

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind((bind_ip,bind_port))

#server.listen(5)

print "[*] listening on %s:%d" % (bind_ip,bind_port)

#def handle_client(client_socket):
  
#  request,addr = client_socket.recvfrom(1024)

#  print "[*] received: %s" % request

#  client_socket.sendto("ACK!",(addr[0],addr[1]))

#  client_socket.close()

while True:

  client,addr = server.recvfrom(4096)

  print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
  
  server.sendto("AABBCCDD",(addr[0],addr[1]))

#  client_handler = threading.Thread(target=handle_client,args=(client,))
#  client_handler.start()
