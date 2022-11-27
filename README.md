# CiscoPractice
## Summary
This project implement a Malware URL lookup service. This service can help a HTTP proxy to decide if the HTTP connection is requesting harmful resources.

## Usage
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

## Roadmap
- [x] Initial Design 
- [x] POC: Connection between HTTP proxy and service
- [x] POC: Create Database and Connection between service and DB
- [x] Implement Request/Response feature
- [ ] Implement Database operation (SELECT)
- [ ] Unit Test
- [ ] Improvements
- [ ] Documentation