import csv
import json

from flask import Blueprint, g, jsonify, request

from api.db import get_db, query_db

def get_parsed_json_from_csv_string(csv_string):
  list_of_lines = csv_string.splitlines()
  data = []
  csv_reader = csv.DictReader(list_of_lines)
  for row in csv_reader:
    data.append(row)
  return json.dumps(data)

bp = Blueprint('csvfiles', __name__)

@bp.route('/csvfiles', methods=('GET', 'POST'))
def csvfiles():
  db = get_db()

  if request.method == 'GET':
    csvfiles = query_db("SELECT * FROM csv_files")
    return jsonify(csvfiles)

  if request.method == 'POST':
    request_json = request.json
    name = request_json['name']
    raw_content = request_json['raw_content']
    parsed_content = get_parsed_json_from_csv_string(raw_content)
    db.execute('INSERT INTO csv_files (name, raw_content, parsed_content) VALUES (?, ?, ?)', (name, raw_content, parsed_content))
    db.commit()
    return jsonify({'status':'success'})
