# comma-reader
## Installation for backend (linux)
1. Have Python 3.5+ with pip installed.
2. Recommend making a virtualenv:
  * `$ python3 -m venv venv`
  * `$ . venv/bin/activate`
3. In project root: 
  a. `$ pip install -r requirements.txt`
  b. I don't think you need to, but you may need to run `$ pip install -e .`
  c. `$ export FLASK_APP=api`
  d. `$ flask init-db` (creates the sqlite database on disk)

## Running the backend (linux)
1. Complete installation steps.
2. In project root:
  a. `$ export FLASK_APP=api` if you haven't run before in this session
  b. `$ flask run`
  c. API should be running on localhost:5000, if the port is different you will need to update the `API_URL` constant in `/web/api/index.js` to reflect that.

## Testing the backend (both)
1. In project root:
  a. `$ pytest`

## Installation for frontend (linux + probably windows)
1. Have node.js and npm installed.
2. In the `/web` directory:
  a. `$ npm install`

## Running the frontend (linux + probably windows)
1. Complete installation steps.
2. In the `/web` directory:
  a. `$ npm run serve` to serve locally

# Stuff I would change
1. Parse CSV into JSON async instead of at the time of upload, same with date stats which are calculated on-demand.
2. Store csv files on disk instead of in db, reference them in db with a guid.
3. I had never worked with flask before and was very rusty with Vue.js and decided to get my weekly dose of masochism by using both in this coding challenge, but I did enjoy the opportunity to toy with them.
4. Expanded testing, tests that are there were just to help me practice a light form of TDD.

# Missed Requirements
1. Download functionality on frontend is missing. This is implemented in the backend, you can download directly by something similar to: `$ curl http://localhost:5000/csvfiles/download/1 > file.csv`, replacing 1 with the id of the file you want to download.
2. Similarly, delete functionality is missing. A well-formed (where well-formed means matching what I expect in the backend) DELETE request to `http://{api}/csvfiles` will work.
3. The application should run on Windows as well, but I haven't tested this as my development machine at home is running Ubuntu.
4. You will need to refresh the page after uploading.

# references
* Referenced https://flask.palletsprojects.com/en/1.1.x/tutorial/ for flask boilerplating. 
* Plenty of StackOverflow usage