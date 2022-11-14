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
INSERT INTO campaigns VALUES (1, "The Rogue Inquisitor of Nordgard", "Campaign set on the continent of Rol'Vetal in the county of Nordgard, within the Empire of Auron.", datetime('now'), datetime('now'));
INSERT INTO countries VALUES (1, "Auron", "Empire of Auron", "#dbdbdb", 1, "/static/images/countrysymbols/auron.png", datetime('now'), datetime('now'));
INSERT INTO cities VALUES (1, "Nordbay", "Port city in the country of Nordgard within the Auronian Empire", "#5bb5b2", 1, 0, 1, "/static/images/citysymbols/nordbay.png", datetime('now'), datetime('now'));
INSERT INTO factions VALUES (1, "Black Horizon", "/static/images/factionsymbols/bhorizon.png", "test description", "#440b5e", 1, datetime('now'), datetime('now'));
INSERT INTO factions VALUES (2, "Platinum Verum", "/static/images/factionsymbols/verum.png", "test description2", "#9c9c9c", 1, datetime('now'), datetime('now'));
INSERT INTO factions VALUES (3, "Sect of Aurel", "/static/images/factionsymbols/sectofaurel.png", "test description3", "#fff07d", 1, datetime('now'), datetime('now'));
INSERT INTO factions VALUES (4, "The Loyal Shields / Nordbay City Watch", "/static/images/factionsymbols/nordbaywatch.png", "test description3", "#73f0ec", 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (1, 1, 2, 5, 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (2, 1, 3, 7, 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (3, 1, 4, 10, 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (4, 2, 1, 10, 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (5, 2, 3, 10, 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (6, 2, 4, 10, 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (7, 3, 1, 7, 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (8, 3, 2, 7, 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (9, 3, 4, 7, 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (10, 4, 1, 7, 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (11, 4, 2, 7, 1, datetime('now'), datetime('now'));
INSERT INTO factiontofactionreputations VALUES (12, 4, 3, 7, 1, datetime('now'), datetime('now'));
INSERT INTO characters VALUES (1, "Karuna", "Wood-elf monk", 1, 0, "#7db57f", 1, datetime('now'), datetime('now'));
INSERT INTO characters VALUES (2, "Kilian", "Tabaxi ranger", 1, 0, "#026305", 1, datetime('now'), datetime('now'));
INSERT INTO characters VALUES (3, "Autismus Maximus", "Dwarven cleric", 1, 0, "#e0e089", 1, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (1, 1, 1, 10, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (2, 1, 2, 10, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (3, 1, 3, 10, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (4, 1, 4, 10, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (5, 2, 1, 15, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (6, 2, 2, 10, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (7, 2, 3, 10, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (8, 2, 4, 10, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (9, 3, 1, 10, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (10, 3, 2, 15, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (11, 3, 3, 10, datetime('now'), datetime('now'));
INSERT INTO charactertofactionreputations VALUES (12, 3, 4, 10, datetime('now'), datetime('now'));
--select * from factions;
--select * from factiontofactionreputations;
--select * from charactertofactionreputations;
```