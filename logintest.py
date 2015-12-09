__author__ = 'Pramod.Kumar'

import unittest
import urllib
import urllib2
import json
# unittest for login.
class authtest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:5000/Authenticate'
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        self.parameters={}
    def testloginSuccess(self):


        self.parameters["useremail"]="0"
        self.parameters["password"]="1"
        self.parameters["rememberMe"] = True
        challenge='{"useremail":"0","password":"1","rememberMe":false}'
        values = {'parameters' : json.dumps(self.parameters)
                  }

        result='{"NAME": "01", "FirstName": null, "companyid": 1, "LastName": null, "companyname": "mansfield", "AlternativeContactNumber": null, "ContactNumber": null, "Role": "admin", "MailId": "0", "PASSWORD": "1", "Id": 5}'
        headers = { 'User-Agent' : self.user_agent }
        data = urllib.urlencode(values)
        req = urllib2.Request(self.url, data, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        self.assertEqual(result,the_page,msg="Not Equal")

    def testloginFailPassword(self):
        self.parameters["useremail"]="0"
        self.parameters["password"]="11"
        self.parameters["rememberMe"] = True
        challenge='{"useremail":"0","password":"1","rememberMe":false}'
        values = {'parameters' : json.dumps(self.parameters)
                  }

        result="invalid password"

        headers = { 'User-Agent' : self.user_agent }
        data = urllib.urlencode(values)
        req = urllib2.Request(self.url, data, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        self.assertEqual(result,the_page.lower(),msg="Not Equal")

def main():
    unittest.main()

if __name__ == '__main__':
    main()