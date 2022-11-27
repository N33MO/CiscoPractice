# CiscoPractice
## Summary
This project implement a Malware URL lookup service. This service can help a HTTP proxy to decide if the HTTP connection is requesting harmful resources.

## Usage
To use the service:
1. Prerequisite: Availlable MongoDB service, e.g. client ```'mongodb://localhost:27017/'```
2. start a sample HTTP server by running ```python -m http.server```
3. start the service from accessor.py by running ```python accessor.py```
4. send GET request from a web browser or postman
    In web browser type ```http://localhost:8080/v1/urlinfo/www.malware1.com```
    In postman use ```GET``` with url ```http://localhost:8080/v1/urlinfo/www.malware2.com```
    The return data will look like this ```{"isValid": true, "isMalware": false}```

A proxy sends a GET request to the service like below:
```
GET /v1/urlinfo/{resource_url_with_query_string}
```
The response will in json format, contains two pieces of info:
```
{
    "isValid": True/False       # if the request from proxy is valid
    "isMalware": True/False     # if the request resources contain malware
}
```
The service will query mongoDB everytime a GET request is received, since the database only keeps urls contain malware resources, it will return a non-empty value when it is a malware link saved in database

## Improvements
+ For increasing size of URL list
  - Use multiple databases to store URL data, use hash map to map URL into database evenly
  - Apply Apache Spark kind of techniques (e.g. MapReduce), to handle large data size
+ For excessive request 
  - Utilize load balancing solution to keep server running
  - Keep each request is responded in a fairly time (e.g. 3s), and process each request queue accordingly
  - Introduce extra server
+ For continuous URL update
  - Decide what to prioritize: Integrity or Availability
  - For average 5000 updates a day, create a separate table store update data and update several times a day

## Roadmap
- [x] Initial Design 
- [x] POC: Connection between HTTP proxy and service
- [x] POC: Create Database and Connection between service and DB
- [x] Implement Request/Response feature
- [x] Implement Database operation (SELECT)
- [x] Unit Test
- [x] Improvements: discussed here
- [x] Documentation