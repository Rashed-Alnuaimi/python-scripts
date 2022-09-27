import socket #essential import to create a server/client.

hostname = socket.gethostname() #TESTING
IPAddr = socket.gethostbyname(hostname) #TESTING

HOST = socket.gethostbyname(socket.gethostname()) #Register a local IP Address in a variable for the device to run on according to the host name.
PORT = 5050 #Creating a port to run a server in.
ADDR = (HOST, PORT) #Containing both the IP Address and the Port in one variable.

HEADER = 64 #Will be used to specify the size of the message in bites later.
FORMAT = 'utf-8' #Specifies the format used to encode/decode the message.

C_DISCONNECT = "!disconnect" #Preset server disconnection command.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Setting up the socket for the client.
client.connect(ADDR) #Connecting the client to the IPv4 Address and Port.

def send(msg): #Creating a complex function to send the message inputted by the client.
    message = msg.encode(FORMAT) #Encode the string into bites.
    msg_len = len(message) #Read the length of the message.
    send_len = str(msg_len).encode(FORMAT) #Encode msg_len into a string.
    send_len += b' ' * (HEADER - len(send_len)) #Pad send_len so the size of the message is the same as HEADER.
    client.send(send_len) #Send the length of the message.
    client.send(message) #Create the message inputted by the Client.

transmittion = "" #Setup an empty text as a placeholder.

while transmittion != C_DISCONNECT: #Reading the message to see whether or not the message has the disconnect command.
    transmittion = input("Enter the message you want to send to the server: ") #Prompt the client host to write a message.
    go = transmittion #Label the message inputted.
    send(go) #Transmit the message to the server.
    print("Input delivered. \n")

else: #Specify the condition when the server is disconnected.
    print("\n[DISCONNECT] The server is being disconnected. Thank you for using the server.")





#==================================================
#send("Hello, World!")
#input()
#send("I am sending a message from the client side!")
#input()
#send("Cya!")
#input()

#send(C_DISCONNECT)
#print("DISCONNECTING")




#print(f"Received {data!r}")