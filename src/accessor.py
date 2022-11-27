from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import constants
import dbConnector
import pymongo
import logging
logging.basicConfig(filename=constants.Constants.LOG_FILE, encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

class MyServer(BaseHTTPRequestHandler):
    # basic HTTP GET request listener
    def do_GET(self):
        isValid = self.verifyProxyRequest(self.path)
        
        if (not isValid):
            self.send_response(400)
            isMalware = None
        else:
            isMalware = self.verifyURLwithQueryStr(self.path[len(constants.Constants.REQ_PREFIX):])
            if (isMalware == None):
                self.send_response(502)
            else:
                self.send_response(200)

        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        data = {}
        data["isValid"] = isValid
        data["isMalware"] = isMalware
        json_data = json.dumps(data)
        self.wfile.write(json_data.encode(encoding='utf_8'))
        logging.debug(f"Respond with json: {json_data}")

    # verify GET request pattern
    def verifyProxyRequest(self, str) -> bool:
        if (len(str) <= len(constants.Constants.REQ_PREFIX)):
            logging.debug(f"Invalid request: {str}")
            return False
        if (str[:len(constants.Constants.REQ_PREFIX)] == constants.Constants.REQ_PREFIX):
            return True
        logging.debug(f"Invalid request: {str}")
        return False
    
    # verify malware URL
    def verifyURLwithQueryStr(self, str) -> bool:
        try:
            collection = dbConnector.dbConnector.getDBCollection(self)
        except pymongo.errors.ConnectionFailure:
            logging.error("Unable to connect to database")
            return None
        else:
            result = list(collection.find({"url": str}))
            dbConnector.dbConnector.closeClient(self)
            if (len(result) == 0):
                return False
            return True
        

if __name__ == "__main__":        
    webServer = HTTPServer((constants.Constants.HOSTNAME, constants.Constants.SERVERPORT), MyServer)
    logging.info("Server started http://%s:%s" % (constants.Constants.HOSTNAME, constants.Constants.SERVERPORT))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    logging.info("Server stopped.")