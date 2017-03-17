# HTTP server - Ja sam server, a onaj koji mi se obraca je klijent
import socket

uticnica = socket.socket()       # Kreiranje socket-a ( prikljucka )
uticnica.bind(('', 8888))        # Povezivanje sa port-om
uticnica.listen(5)               # Max. broj zahteva u redu za cekanje je 5

print("Čekam zahteve na portu: ",8888)   # Log
while True:
    klijent, adresa = uticnica.accept()                             # Čekaj i prihvati novi zahtev
    zahtev = klijent.recv(1024)                                     # Preuzmi sadržaj zahteva
    print("Poziv sa adrese: ",adresa,"\n",zahtev.decode("utf-8"))   # Prikaži zahtev
    klijent.send(str.encode('HTTP/1.1 200 OK\r\n'))                 # Potvrda prijema zahteva,
    klijent.send(str.encode("Content-Type: text/html\r\n\r\n"))     # Tip odgovora
    klijent.send(str.encode("Pozdrav iz Beograda!"))                # Odgovor na zahtev
    klijent.close()                                                 # Prekini vezu sa korsinikom

uticnica.close()  # Zatvaranje server socket-a
