import socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind(('localhost', 1235))

mySocket.listen(5)

i=0

try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')
        peticion= recvSocket.recv(2048).decode('utf-8', "strict")
        print(peticion)

        favicon = (peticion.split()[1][1:])

        if favicon == "favicon.ico":
            recvSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1>Not Found</h1></body></html>\r\n","utf-8"))
            recvSocket.close()
            continue

        if i==0:
            recurso = peticion.split()[1][1:]
            try:
                recurso = int(recurso)
            except ValueError:
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body>" +
                                "<p>Incorrecto. Me das una " + str(recurso) +
                                "</p>" +
                                "</body></html>" +
                                "\r\n", "utf-8"))
                mySocket.close()
                break

            print ('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body>" +
                            "<p>Me das un " + str(recurso) +
                            "</p>" +
                            "</body></html>" +
                            "\r\n", "utf-8"))
            recvSocket.close()
            i=1
        else:
            recurso_dos = peticion.split()[1][1:]
            try:
                recurso_dos = int(recurso_dos)
            except ValueError:
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body>" +
                                "<p>Incorrecto. Me das una " + str(recurso_dos) +
                                "</p>" +
                                "</body></html>" +
                                "\r\n", "utf-8"))
                mySocket.close()
                break

            print ('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body>" +
                            "<p>Me diste un " + str(recurso) + " Ahora un " + str(recurso_dos) + " Suman: " + str(recurso + recurso_dos) +
                            "</p>" +
                            "</body></html>" +
                            "\r\n", "utf-8"))
            recvSocket.close()
            i=0

except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
