from pymongo import MongoClient

# connect to mongoDB
def connectDB():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.CiscoPractice
    collection = db.testCollection
    return collection

# check url in DB
def isMalwareURL(url) -> bool:
    collection = connectDB()
    result = list(collection.find({"url": url}))

    if (len(result) == 0):
        return False
    return True

if __name__ == "__main__":
    result1 = isMalwareURL("www.malware1.com")
    print(f"www.malware1.com is Malware URL is: {result1}")
    result2 = isMalwareURL("www.notMalware.com")
    print(f"www.notMalware.com is Malware URL is: {result2}")