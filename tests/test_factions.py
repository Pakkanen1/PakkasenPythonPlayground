import unittest
import requests
import json

TEST_URL = "http://localhost:5000"

class test_factions(unittest.TestCase):

    def test_update_character_reputation_in_faction(self):
        json_data = {
            "character_id": 1,
            "faction_id": 1,
            "reputation_to_add": 5
        }
        resp = requests.patch(f"{TEST_URL}/api/character-reputation/update", data=json.dumps(json_data),
                              headers={"Content-Type": "application/json"})
        print(resp.json())
        assert resp.status_code == 200

    def test_update_faction_reputation_with_another_faction(self):
        json_data = {
            "faction_id": 1,
            "target_faction_id": 2,
            "reputation_to_add": 32
        }
        resp = requests.patch(f"{TEST_URL}/api/faction-reputation/update", data=json.dumps(json_data),
                              headers={"Content-Type": "application/json"})
        print(resp.json())
        assert resp.status_code == 200


if __name__ == '__main__':
    unittest.main()
