import socket
import sys
import thread

if(len(sys.argv) < 3) :
    print 'Usage : python telnet.py hostname port'
    sys.exit()
 
host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Socket Created")

try:
	s.bind((host,port))
except socket.error:
	print("Binding Failed")
	sys.exit()

print("Socket has been created")

s.listen(10)

print("Socket Is Ready")

def clientthread(conn):
	message = "Welcome to the server...."
	conn.send(message.encode())
	
	while True:
		data = conn.recv(2048)
		reply = ">> " + data.encode()
		if not data:
			break;
		print(reply)
		conn.sendall(data)
	conn.close()

while 1:
	conn, addr = s.accept()
	print("Connected: " + addr[0] +":" + str(addr[1]))
	thread.start_new_thread(clientthread, (conn,))
s.close()


