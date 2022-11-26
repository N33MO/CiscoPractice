from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    # basic HTTP GET request listener
    def do_GET(self):
        
        isValid = self.verifyProxyRequest(self.path)
        isMalware = self.verifyURLwithQueryStr(self.path[13:])
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<p>Valid Request: %s</p>" % isValid, "utf-8"))
        self.wfile.write(bytes("<p>Malware URL: %s</p>" % isMalware, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    # verify GET request pattern
    def verifyProxyRequest(self, str) -> bool:
        print(str[:12])
        if (str[:12] == "/v1/urlinfo/"):
            return True
        return False
    
    # verify malware URL
    def verifyURLwithQueryStr(self, str) -> bool:
        print(str)
        return False
        

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")