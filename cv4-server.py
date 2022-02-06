#!/usr/bin/env python3

import socket
from enum import IntEnum
import threading
import json

ADRESA = "0.0.0.0"
PORT = 9999

#zoznam pouzivatelov
USERS = list()

class Sprava:
    def __init__(self, paOd, paKomu, paOperacia, paText):
        self.aOd = paOd
        self.aKomu = paKomu
        self.aOperacia = paOperacia
        self.aText = paText

    @staticmethod
    def jsonParser(obj):
        return Sprava(obj['aOd'], obj['aKomu'], obj['aOperacia'], obj['aText'])

class Operacia(IntEnum):
    LOGIN = 1
    EXIT = 2
    USERS = 3

def handleClient(clientSock, clientAddr):
    while(True):
            data = clientSock.recv(1500)
            sprava = json.loads(data.decode(), object_hook=Sprava.jsonParser)

            if sprava.aOperacia == Operacia.LOGIN:
                USERS.append(sprava.aOd)
                print("Prihlasil sa klient: {}:{}, nick: {}".format(clientAddr[0], clientAddr[1], sprava.aOd))
                continue
            if sprava.aOperacia == Operacia.EXIT:
                USERS.remove(sprava.aOd)
                print("Odhlasil sa klient: {}:{}, nick: {}".format(clientAddr[0], clientAddr[1], sprava.aOd))
                clientSock.close()
                return
            if sprava.aOperacia == Operacia.USERS:
                sprava = Sprava('', '', Operacia.USERS, USERS)
                jsonStr = json.dumps(sprava.__dict__)
                clientSock.send(jsonStr.encode())
                continue
                
            print("Sprava {}:{}, od: {}, komu: {}, text: {}".format(
                clientAddr[0], clientAddr[1],
                sprava.aOd, sprava.aKomu, sprava.aText
            ))
          

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ADRESA, PORT))
    sock.listen(10)

    print("Server pre CHAT spusteny na {}:{}".format(ADRESA, PORT))

    while(True):
        (clientSock, clientAddr) = sock.accept()
        vlakno = threading.Thread(target=handleClient, args=(clientSock, clientAddr))
        vlakno.start()
