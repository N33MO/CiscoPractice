import accessor
import unittest

class TestVerifyProxyRequest(unittest.TestCase):

    def test_invalid_request(self):
        req1 = "/v1/urlinfo3/www.fakelink.com"
        result = accessor.MyServer.verifyProxyRequest(self, req1)
        self.assertEqual(result, False)

    def test_valid_request(self):
        req1 = "/v1/urlinfo/www.fakelink.com"
        result = accessor.MyServer.verifyProxyRequest(self, req1)
        self.assertEqual(result, True)

    def test_malware_url(self):
        url1 = "www.malware1.com"
        result = accessor.MyServer.verifyURLwithQueryStr(self, url1)
        self.assertEqual(result, True)

    def test_normal_url(self):
        url1 = "www.malware3.com"
        result = accessor.MyServer.verifyURLwithQueryStr(self, url1)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()