import unittest
import requests
import json

TEST_URL = "http://localhost:5000"

class test_factions(unittest.TestCase):

    def test_update_character_reputation_in_faction(self):
        json_data = {
            "kikkeli": "pippeli",
            "kakkeli": "kukkeli"
        }
        resp = requests.patch(f"{TEST_URL}/api/reputation/update", data=json.dumps(json_data),
                            headers={"Content-Type": "application/json"})
        print(resp.json())


if __name__ == '__main__':
    unittest.main()
