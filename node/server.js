var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
		amtCPU = os.cpus().length;
		freeMem = os.freemem();
		avaMem = freeMem / (1024 * 1024);
		totalMemory= os.totalmem();
		totalMemoryMB = totalMemory / (1024 * 1024);
		serverUptime=os.uptime;	
       	days = Math.floor(serverUptime / (60*60*24));
		hours = Math.floor((serverUptime % (60*60*24)) / (60*60));
		minutes = Math.floor((serverUptime % (60 * 60)) / 60);
		seconds = Math.floor(serverUptime % 60);
		
		
		html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p><b>Hostname:</b> ${myHostName}</p>
            <p><b>IP:</b> ${ip.address()}</p>
            <p><b>Server Uptime:</b> ${days} Days ${hours} Hours ${minutes} Minutes ${seconds} Seconds</p>
            <p><b>Total Memory:</b> ${totalMemoryMB.toFixed(2)} MB </p>
            <p><b>Free Memory:</b> ${avaMem.toFixed(2)} MB </p>
            <p><b>Number of CPUs:</b> ${amtCPU} </p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");