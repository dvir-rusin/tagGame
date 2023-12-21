import socket
import threading
from _thread import *
from player import Player
import pickle
import random
import traceback



# Server configuration
server = "192.168.1.19"
port = 5000

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Bind socket to server address and port
    s.bind((server, port))
except socket.error as e:
    # Print any socket error that occurs during binding
    str(e)

# Listen for incoming connections
s.listen(2)
print("Waiting for a connection, Server Started")



# Create a lock for synchronizing access to shared data
players_lock = threading.Lock()

players = [Player(0, 230, 40, 40, (255, 0, 0),1234), Player(460, 230, 40, 40, (0, 0, 255),4321)]

def threaded_client(conn, player):#player's socket, player's number
    """
        Handle communication with a client in a separate thread.

        Args:
            conn (socket.socket): The client's socket connection.
            player (int): The player index assigned to the client.

        Returns:
            None
        """



    try:
        # Perform the key exchange protocol
        p = int(conn.recv(100).decode())
        g = random.randint(1, 10)
        conn.send(str(g).encode())

        b = random.randint(1, 10)
        B = (g ** b) % p
        A = int(conn.recv(100).decode())
        conn.send(str(B).encode())

        private_key = (A ** b) % p
        # test: print the private key to the console
        print("private key is", private_key)


        # Send the initial player object to the client
        conn.send(pickle.dumps(players[player]))
        reply = ""
        while True:
            try:
                # Receive and update the player object from the client
                data = pickle.loads(conn.recv(2048*4))
                #encryption
                data.x = data.x - private_key
                data.y = data.y - private_key
                # Acquire the lock before modifying the players list
                with players_lock:
                    players[player] = data

                if not data:
                    # If no data is received, the client has disconnected
                    print("Disconnected")
                    break
                else:
                    if player == 1:
                        reply = players[0]
                    else:
                        reply = players[1]
                    #######print("Received: ", data)
                    ######print("Sending: ", reply)
                # Send the updated player object back to the client
                conn.sendall(pickle.dumps(reply))
            except Exception as e:
                print("Error:", e)
                traceback.print_exc()
                break

    except Exception as e:
        print("Error:", e)
        traceback.print_exc()

    finally:
        print("Lost connection")
        # Acquire the lock before modifying the players list

        # Notify the remaining player(s) about the disconnection
        if len(players) >0:
            # Send a special signal to indicate disconnection
            disconnection_signal = "DISCONNECTED"
            conn.sendall(disconnection_signal.encode())
            print(disconnection_signal)
        players[player].connected = False
        conn.close()


currentPlayer = 0

while True:
    # Accept a new connection
    conn, addr = s.accept()#player's socket, server and port
    print("Connected to:", addr)


    players[currentPlayer].connected=True


    # Start a new thread to handle the connection
    start_new_thread(threaded_client, (conn, currentPlayer))

    print(f"player {currentPlayer} has joined")
    currentPlayer += 1