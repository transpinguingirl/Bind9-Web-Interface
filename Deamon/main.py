import socket
import sys
import os
from thread import *
MAX_Clients =  100
VERSION     =  0.0.1
HOST        = '127.0.0.1'
PORT        = '2000'
pid         = str(os.getpid())
pidfile     = "/tmp/Bind9-Webinterface-deamon.pid"
if os.path.isfile(pidfile):
    print( pidfile + " already exists, exiting")
    sys.exit()
file(pidfile, 'w').write(pid)

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((HOST,PORT))
    except socket.error as errormsg:
        prind "Bind failed. Error : " + str(errormsg[0]) + "Message : " + str(errormsg[1])
        sys.exit()
    server.listen(MAX_Clients)
    def client(connection):
        connection.send("Bind9-Webinterface Version:"+VERSION)
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            decoded = data.decode("utf-8")
            if "get" in decoded:
                if "getAll" in decoded:
                    connection.sendall("all data")
            if "UPDATE_DNS_ENTRY" in decoded:
                connection.sendall("READY_TO_RECEIVE")


        connection.close()

    while True:
        connection, addr = server.accept()
        start_new_thread(client,connection)#or (clinet,(connection,))
    server.close()
finally:
    os.unlink(pidfile)
