import requests
import unittest

class TestWebsiteLoading(unittest.TestCase):
   
    def test_website_loading(self):
        # Step 1: Print a log statement indicating that the test is starting
        print("Starting test to check if the website loads properly...")
       
        # Step 2: Make an HTTP GET request to the website
        response = requests.get("https://www.atg.world")
       
        # Step 3: Print the status code of the HTTP response
        print("Status code:", response.status_code)
       
        # Step 4: Assert that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200, "Website did not load properly")
       
        # Step 5: Print a log statement indicating that the test passed
        print("Website loaded successfully!")

if _name_ == "_main_":
    unittest.main()
