import socket, threading
from queue import Queue
import select

queue = Queue()
class ClientThread(threading.Thread):
    def __init__(self, client1, client2):
        threading.Thread.__init__(self)
        self.addr1 = client1[0]
        self.sock1 = client1[1]
        self.addr2 = client2[0]
        self.sock2 = client2[1]
        print ("New connection added: ", self.addr1, self.addr2)
    def run(self):
        print ("Connection from : ", self.addr1, self.addr2)
        self.username1 = self.sock1.recv(1024).decode()
        self.username2 = self.sock2.recv(1024).decode()
        msg = ''
        while True:
            self.sock1.setblocking(0)
            self.sock2.setblocking(0)
            ready1 = select.select([self.sock1], [], [], 0.05)
            if ready1[0]:
                data1 = self.sock1.recv(2048)
                msg1 = data1.decode()
                if msg1=='bye':
                    break
                msg1 = self.username1 + ": " + msg1
                print ("from client 1", msg1)
                self.sock2.send(bytes(msg1,'UTF-8'))
            ready2 = select.select([self.sock2], [], [], 0.05)
            if ready2[0]:
                data2 = self.sock2.recv(2048)
                msg2 = data2.decode()
                if msg2=='bye':
                    break
                msg2 = self.username2 + ": " + msg2
                print ("from client 2", msg2)
                self.sock1.send(bytes(msg2,'UTF-8'))
        print ("Client at ", self.addr1, self.addr2 , " disconnected...")

LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP protocol
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen()
    clientSocket, clientAddress = server.accept()
    queue.put([clientAddress,clientSocket])
    if queue.qsize() > 1:
        newthread = ClientThread(queue.get(), queue.get())
        newthread.start()