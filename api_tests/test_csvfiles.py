import pytest
import json

from api.db import get_db

EXAMPLE_CSV = 'name,test\nnamevalue,testvalue\nvaluename,valuetest'

# test that nothing borks with an empty db
def test_empty_db(client):
  response = client.get("/csvfiles").get_json()
  assert response == []

# test uploading a csvfile
def test_post_csvfile(client):
  response = client.post('/csvfiles', json={'name':'test.csv', 'raw_content':EXAMPLE_CSV}).get_json()
  assert response['status'] == 'success'
  response = client.get("/csvfiles").get_json()
  assert response[0]['name'] == 'test.csv'
  assert response[0]['raw_content'] == EXAMPLE_CSV
  json_content = json.loads(response[0]['parsed_content'])
  assert response[0]['id'] == 1
  assert json_content[0]['name'] == 'namevalue'
  assert json_content[0]['test'] == 'testvalue'

# test uploading the provided (large) example csv, this is SLOW right now because of
# parsing happening at the time of upload
def test_upload_example_csv(client):
  example_csv = open("api_tests/example.csv")
  example_csv_string = example_csv.read()
  response = client.post('/csvfiles', json={'name':'example.csv', 'raw_content':example_csv_string}).get_json()
  assert response['status'] == 'success'
  response = client.get("/csvfiles").get_json()
  assert response[0]['id'] == 1
  assert response[0]['raw_content'] == example_csv_string

# test that we can get the date stats
# TODO: verify date stats (probably self generate a simpler example for testing too)
def test_example_csv_dates(client):
  example_csv = open("api_tests/example.csv")
  example_csv_string = example_csv.read()
  response = client.post('/csvfiles', json={'name':'example.csv', 'raw_content':example_csv_string}).get_json()
  assert response['status'] == 'success'
  response = client.get('/csvfiles/stats/1').get_json()
  assert response['status'] == 'success'
  # verify stats

# test deleting uploaded csvfile
def test_delete_csvfile(client):
  example_csv = EXAMPLE_CSV
  response = client.post('/csvfiles', json={'name':'example.csv', 'raw_content':example_csv}).get_json()
  assert response['status'] == 'success'
  response = client.delete('/csvfiles', json={'id':1}).get_json()
  assert response['status'] == 'success'
  response = client.get("/csvfiles").get_json()
  assert response == []