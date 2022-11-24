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
        with self._create_session() as s:
            print(s.cookies)
            refresh = s.cookies['refresh_token_cookie']
            resp = s.patch(f"{TEST_URL}/api/character-reputation/update", data=json.dumps(json_data),
                             headers={"Content-Type": "application/json",
                                      "Authorization": f"Bearer {refresh}"})
            print(resp.json())
            assert resp.status_code == 200

    def test_update_faction_reputation_with_another_faction(self):
        json_data = {
            "faction_id": 1,
            "target_faction_id": 2,
            "reputation_to_add": -2
        }
        with self._create_session() as s:
            print(s.cookies)
            refresh = s.cookies['refresh_token_cookie']
            resp = s.patch(f"{TEST_URL}/api/faction-reputation/update", data=json.dumps(json_data),
                             headers={"Content-Type": "application/json",
                                      "Authorization": f"Bearer {refresh}"})
            print(resp.json())
            assert resp.status_code == 200

    def _create_session(self) -> requests.Session:
        headers = {"User-Agent": "Mozilla/5.0"}
        form_data = {"username": "olav", "password": "massionhalpaa123"}
        session = requests.Session()
        session.post(f"{TEST_URL}/login", headers=headers, data=form_data)
        return session


if __name__ == '__main__':
    unittest.main()
