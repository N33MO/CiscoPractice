from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import constants
import logging
logging.basicConfig(filename=constants.LOG_FILE, encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

class MyServer(BaseHTTPRequestHandler):
    # basic HTTP GET request listener
    def do_GET(self):
        isValid = self.verifyProxyRequest(self.path)
        
        if (not isValid):
            self.send_response(400)
            isMalware = False
        else:
            self.send_response(200)
            # mock waiting time
            time.sleep(3)
            isMalware = self.verifyURLwithQueryStr(self.path[len(constants.REQ_PREFIX):])

        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        data = {}
        data["isValid"] = isValid
        data["isMalware"] = isMalware
        json_data = json.dumps(data)
        self.wfile.write(json_data.encode(encoding='utf_8'))
        logging.debug(f"Respond with json: {json_data}")

    # verify GET request pattern
    def verifyProxyRequest(str) -> bool:
        if (len(str) <= len(constants.REQ_PREFIX)):
            logging.debug(f"Invalid request: {str}")
            return False
        if (str[:len(constants.REQ_PREFIX)] == constants.REQ_PREFIX):
            return True
        logging.debug(f"Invalid request: {str}")
        return False
    
    # verify malware URL
    def verifyURLwithQueryStr(str) -> bool:
        return False
        

if __name__ == "__main__":        
    webServer = HTTPServer((constants.HOSTNAME, constants.SERVERPORT), MyServer)
    logging.info("Server started http://%s:%s" % (constants.HOSTNAME, constants.SERVERPORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    logging.info("Server stopped.")