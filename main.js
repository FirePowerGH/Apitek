import http from 'http';
import fs from 'fs';

http.createServer(function (req, res) {
    fs.readFile('frontend/index.html', function(err, data) {
        if (err) {
            res.writeHead(404, {'Content-Type': 'text/html'});
            return res.end('404 Not Found');
        }
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        return res.end();
    });
}).listen(8080, '192.168.1.33');