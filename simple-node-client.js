var http = require('http');

// IP adresa
var options = {
  host: '127.0.0.1',
  port: 8888,
  path: '/index.html'
};

callback = function(response) {
  var str = '';

  // preuzimanje odgovora od servere
  response.on('data', function (chunk) {
        str += chunk;
  });

  // kraj preuzimanja
  response.on('end', function () {
        console.log(str);
  });
}

http.request(options, callback).end();
