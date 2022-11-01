Hiekkalaatikko kaikennäköseen webdevaus kikkailuun pythonilla, lähinnä flaskia käyttäen.
Tavoitteena ois pitää projketin rakenne ns. "realistisena" esim: https://github.com/gothinkster/flask-realworld-example-app

Asennusohjeet:
1. Luo python venv: ``python -m venv .venv``
2. Aktivoi venv: ``.venv\Scripts\active.ps1`` tai ``source .venv/Scripts/active``
3. Asenna riippuvuudet: ``python -m pip install -r requirements.txt``
4. Initialisoi tietokanta:
   1. ``flask db init``
   2. ``flask db migrate``
   3. ``flask db upgrade``

Homman saa käyntiin komennolla ``flask run``