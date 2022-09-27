#   Necessary functions for creating a server.
import socket #essential import to create a server/client.
import threading #allow specified commands to run in a separate thread and doesn't have to wait for other codes to finish.

#   Necessary functions to allow for server shutdown.
import signal
#import readchar



#   Testing.
hostname = socket.gethostname() #TESTING
IPAddr = socket.gethostbyname(hostname) #TESTING


#   Term identification.
HOST = socket.gethostbyname(socket.gethostname()) #Register a local IP Address in a variable for the device to run on according to the host name.
PORT = 5050 #Creating a port to run a server in.
ADDR = (HOST, PORT) #Containing both the IP Address and the Port in one variable.

HEADER = 64 #Will be used to specify the size of the message in bites later.
FORMAT = 'utf-8' #Specifies the format used to encode/decode the message.

C_DISCONNECT = "!disconnect" #Preset server disconnection command.


#   Initial response to the server opening.
print (f"Welcome {hostname}. Your IP Address is {HOST}.\n")


#   Main server socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket to open the device to the connection.
server.bind(ADDR) #Binding the socket to the IP Address.


#   Client communication.
def handle_client(conn, addr): #Will handle the individual connection between a client and a server.
    print(f"[NEW CONNECTION] {addr} connected.\n")
    connection = True #Label the status of the connection for ease of use.
    while connection: #Continue to run until connection is no longer "True".
        msg_len = conn.recv(HEADER).decode(FORMAT) #Receive the message and decode from bite to string in UDF-8 to it to start reading the size.
        if msg_len: #Making sure msg_len has a content held within it.
            msg_len = int(msg_len) #Turn the message length's variable into integer and mention how long the message is.
            message = conn.recv(msg_len).decode(FORMAT) #Receive the message from the client according to the specified size.
            if message == C_DISCONNECT: #Check to see if the disconnect command was inputted.
                connection = False #Disconnect the client from the server by ending the while loop.

            print(f"[Client{addr}]  [Size {msg_len}]:    {message} \n") #Display the message the client sent.
    conn.close() #Close the connection.


def start(): #activate the socket server and distribute the destination of the clients.
    server.listen() #Searching for new connection.
    print (f"[LISTENING] Server is listening on {HOST}.")
    print (f"[NOTICE] To close the server, press the Ctrl and C keys.\n")
    while True: #Will go on an infinite loop until the server ends
        conn, addr = server.accept() #Will wait for a new connection to the server.
        thread = threading.Thread(target=handle_client, args=(conn,addr)) #Create a new thread with the handle_client function. 
        thread.start() #Start the handle_client function in a separate thread.
        thread_count = threading.activeCount() - 1
        print(f"[ACTIVE CONNECTIONS] {thread_count}\n") #Specify how many threadings are connected without including the current one.
    

def server_exit(sig, frame):
    res = input("\nCtrl-C was inputted. Do you really want to exit? y/n ")
    if res == 'y' or res == 'Y' or res == 'yes':
        exit(1)


signal.signal(signal.SIGINT, server_exit)

print ("[STARTING] Server is starting...")
start() #Start the server.