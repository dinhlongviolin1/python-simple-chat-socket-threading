import select
import socket
from login import login
from chat import chatBox
SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


# Login Box 
def getName(self):
    username.append(self.e1.get())
    self.end()

username = []
login(getName) # open login window
username = username[0]
client.sendall(bytes(username,'UTF-8'))
print(username)

# chat Box
def buttonFunction(self):
    out_data = self.text.get("1.0", self.tk.END)
    if out_data!="":
        self.text.delete("1.0", self.tk.END)
        client.sendall(bytes(out_data,'UTF-8'))
        if out_data=='bye':
            chat.end()
            client.close()
def manageChatBox(self):
    client.setblocking(0)
    ready = select.select([client], [], [], 0.05)
    if ready[0]:
        in_data = client.recv(1024)
        print("From Server :" ,in_data.decode())
        self.mylist.insert(self.tk.END, in_data)

chat = chatBox(username, buttonFunction)
chat.start(manageChatBox)


