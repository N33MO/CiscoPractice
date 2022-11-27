from pymongo import MongoClient
import pymongo
import constants

class dbConnector():
    client = None
    attempt = 0
    # connect to mongoDB and get collection
    def getDBCollection(self):
        dbConnector.client = MongoClient(constants.Constants.MONGO_CLIENT)
        if (dbConnector.client == None):
            self.retryConnection()
        db = dbConnector.client.CiscoPractice
        collection = db.testCollection
        return collection
    
    # retry connection if failed, within a max attempt limit
    def retryConnection(self):
        if (dbConnector.attempt > constants.Constants.MAX_RECONNECT_ATTEMPTS):
            raise pymongo.errors.ConnectionFailure
        dbConnector.attempt = dbConnector.attempt + 1
        dbConnector.client = MongoClient(constants.Constants.MONGO_CLIENT)
        if (dbConnector.client == None):
            self.retryConnection()

    # close connection after use
    def closeClient(self):
        dbConnector.client.close()