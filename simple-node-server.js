var http = require('http');                         // Importuj http objekat

function Odgovor(request, response){                // Hendler zahteva
  response.end('Zahtevali ste: ' + request.url);   // Odgovor na zahtev
}

var server = http.createServer(Odgovor);            // Kreiraj server

server.listen(9999, function(){                     // Startovanje servera

  console.log("Čekam zahteve na: http://localhost: ", 9999);

});
