from pymongo import MongoClient
import pymongo
import constants

"""
    This is the database connection class
    It will try to reconnect database with a max
    limit of attempts.
    If connection is unsuccessful, it raise an error
    of ConnectionFailuer
"""
class dbConnector():
    client = None
    attempt = 0
    # connect to mongoDB and get collection
    # when connection failed, goto retryConnection()
    # output: database collection
    def getDBCollection(self):
        dbConnector.client = MongoClient(constants.Constants.MONGO_CLIENT)
        if (dbConnector.client == None):
            self.retryConnection()
        db = dbConnector.client[constants.Constants.DB]
        collection = db[constants.Constants.COLLECTION]
        return collection
    
    # retry connection if failed, within a max attempt limit
    # within MAX_RECONNECT_ATTEMPTS numbers of attempt, this method keep 
    # reconnect to database upon failure, will raise ConnectionFailure
    # error once reached predefined max attempts
    def retryConnection(self):
        if (dbConnector.attempt > constants.Constants.MAX_RECONNECT_ATTEMPTS):
            raise pymongo.errors.ConnectionFailure
        dbConnector.attempt = dbConnector.attempt + 1
        dbConnector.client = MongoClient(constants.Constants.MONGO_CLIENT)
        if (dbConnector.client == None):
            self.retryConnection()

    # close connection after use
    # once query from database is finished, connection could be closed
    # by calling this method
    def closeClient(self):
        dbConnector.client.close()