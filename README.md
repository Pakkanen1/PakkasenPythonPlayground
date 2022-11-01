Hiekkalaatikko kaikennäköseen webdevaus kikkailuun pythonilla, lähinnä flaskia käyttäen.
Tavoitteena ois pitää projketin rakenne ns. "realistisena" esim: https://github.com/gothinkster/flask-realworld-example-app

Asennusohjeet:
1. Luo python venv: ``python -m venv .venv``
2. Aktivoi venv: ``.venv\Scripts\active.ps1`` tai ``source .venv/Scripts/active``
3. Asenna riippuvuudet: ``python -m pip install -r requirements.txt``
4. Initialisoi tietokanta:
   1. ``flask db init``
   2. ``flask db migrate -m "initial migration"``
   3. ``flask db upgrade``

Homman saa käyntiin komennolla ``flask run``

Testidataa:
```
--INSERT INTO factions VALUES (1, "testname", "/static/images/factionsymbols/test.png", "test description", "#FF0000", datetime('now'), datetime('now'));
--INSERT INTO factions VALUES (2, "testname2", "/static/images/factionsymbols/test2.png", "test description2", "#FF0011", datetime('now'), datetime('now'));
--INSERT INTO factiontofactionreputations VALUES (1, 1, 2, 5, datetime('now'), datetime('now'));
--select * from factions;
select * from factiontofactionreputations;
```