import socket

# Kreiraj uticnicu
uticnica = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Povezi se na server
#uticnica.connect(("216.58.208.142",80)) # Google
uticnica.connect(("localhost",8888))
# Pošalji zahtev
uticnica.send(str.encode("GET / HTTP/1.1\n\n"))

# Prihvati odgovor
while True:
    resp = uticnica.recv(2048).decode("utf-8")
    print (resp)
    if resp == "": break

# Zatvori uticnicu
uticnica.close()
