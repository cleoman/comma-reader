Linux instructions:
1. Have Python 3.5+ with pip installed.
2. Recommend making a virtualenv:
  * `$ python3 -m venv venv`
  * `$ . venv/bin/activate`
3. `$ pip install -r requirements.txt`
4. `$ python3 -m flask run`
5. API will be hosted on `http://127.0.0.1:5000/` by default

# Example Commands with curl
`$ curl --header "Content-Type: application/json" --request POST --data "{\"name\":\"test.csv\", \"raw_content\":\"ay,lmao\"}" http://localhost:5000/csvfiles`
`$ curl http://localhost:5000/csvfiles`
