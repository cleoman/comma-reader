import pytest
import json

from api.db import get_db

EXAMPLE_CSV = 'name,test\nnamevalue,testvalue\nvaluename,valuetest'

def test_empty_db(client):
  response = client.get("/csvfiles").get_json()
  assert response == []

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

def test_upload_example_csv(client):
  example_csv = open("api_tests/example.csv")
  example_csv_string = example_csv.read()
  response = client.post('/csvfiles', json={'name':'example.csv', 'raw_content':example_csv_string}).get_json()
  assert response['status'] == 'success'
  response = client.get("/csvfiles").get_json()
  assert response[0]['id'] == 1
  assert response[0]['raw_content'] == example_csv_string

def test_example_csv_dates(client):
  example_csv = open("api_tests/example.csv")
  example_csv_string = example_csv.read()
  response = client.post('/csvfiles', json={'name':'example.csv', 'raw_content':example_csv_string}).get_json()
  assert response['status'] == 'success'
  response = client.get("/csvfiles/stats/1")
  # verify stats