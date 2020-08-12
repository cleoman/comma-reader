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
  assert json_content[0]['name'] == 'namevalue'
  assert json_content[0]['test'] == 'testvalue'
