"""
For this problem, you will build a simple chat server.

The intent of this server is that users will connect to it using a direct socket connection, so netcat or socket.connect
should both be capable of talking to the server.

The server itself should consist of one main function that listens on a provided port for incoming connections.
Each time a connection is received, it should create a new thread to handle that connection. Think about
what that thread will need, at a minimum it should take the connection it is handling.

A client should be prompted to enter their name for the chat server. Once they have entered it, all future messages
they send should be relayed to the rest of the clients connected to the server, with gthe user's name prepended.

Think about how this will be accomplished. You will likely need some sort of data structure to keep track of all
connections that can be shared amount the threads. This data structure will need to be updated as new clients connect.
When a thread receives a client message it can then use this data structure to send messages to all other clients.
Make sure that each thread adds and removes it's connection to the data structure as it goes.

Hint 1: You could use a dictionary to map the client names to their connections. This dictionary could be shared, and
by checking the client name each thread can make sure it doesn't accidentally send the clients message back to itself.

Hint 2: Use a lock when accessing the structure keeping track of the clients. This will prevent changes being made to
it by one thread while another is iterating through it, which can cause errors.

Hint 3: The code for the main server function can be pretty simple. It only needs to get connections and hand them off
to threads. This can be performed in an infinite while loop, not need for an option to gracefully shutdown the server.

"""


def handle_client():
    pass


def chat_server(port: int):
    pass
