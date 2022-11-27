import accessor
import unittest

class TestVerifyProxyRequest(unittest.TestCase):
    
    def test_invalid_request(self):
        req1 = "/v1/urlinfo3/www.fakelink.com"
        result = accessor.MyServer.verifyProxyRequest(req1)
        self.assertEqual(result, False)
    
    def test_valid_request(self):
        req1 = "/v1/urlinfo/www.fakelink.com"
        result = accessor.MyServer.verifyProxyRequest(req1)
        self.assertEqual(result, True)
        
if __name__ == '__main__':
    unittest.main()