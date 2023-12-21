import socket
import pickle
from encrypting import Encrypting

class Network:
    def __init__(self):
        '''The class is responsible for handling the network connection between the client and server.'''

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#tcp
        self.server = "192.168.1.19" # Server IP address
        self.port = 5000 # Server port
        self.addr = (self.server, self.port) # Server address
        self.p = self.connect() # Connect to the server and get the initial game data


    def getP(self):
        return self.p #Returns the player object received from the server.


    def connect(self):
        try:
            self.client.connect(self.addr) # Connect the client to the server
            e = Encrypting()
            self.private_key = e.private_key(self.client)#gets a socket
            print("private key is : ", self.private_key)
            return pickle.loads(self.client.recv(2048*4)) # Receive the initial game data from the server

        except:
            pass

    def send(self, data):#,Player
        try:
            data.x = data.x + self.private_key
            data.y = data.y + self.private_key
            pickled_data = pickle.dumps(data)  # Serialize the data
            self.client.sendall(pickled_data)# Send the serialized data to the server
            data.x = data.x - self.private_key
            data.y = data.y - self.private_key
            response = self.client.recv(2048)  # Receive the response from the server
            if response:
                return pickle.loads(response)  # Deserialize and return the response
            else:
                print("Empty response received from the server.")
                return None
        except (socket.error, pickle.PickleError) as e:
            print("Error occurred during sending/receiving data:", e)
            return None


