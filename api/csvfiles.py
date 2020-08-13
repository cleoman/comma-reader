import csv
import json

from flask import Blueprint, g, jsonify, request
from dateutil.parser import parse
from datetime import *

from api.db import get_db, query_db

def get_parsed_json_from_csv_string(csv_string):
  list_of_lines = csv_string.splitlines()
  data = []
  csv_reader = csv.DictReader(list_of_lines, restval="BLANK")
  for row in csv_reader:
    data.append(row)
  return json.dumps(data)

def get_date_stats(json_content):
  # pretty slow on example.csv, should do this async
  dict_of_years_to_count = {}
  unparsed_csv_rows = json_content[0]['parsed_content']
  csv_rows = json.loads(unparsed_csv_rows)
  for row in csv_rows:
    date_string = row['date']
    date_datetime = parse(date_string)
    year = date_datetime.year
    if year not in dict_of_years_to_count.keys():
      dict_of_years_to_count[year] = 0
    dict_of_years_to_count[year] += 1
  return dict_of_years_to_count

bp = Blueprint('csvfiles', __name__)

@bp.route('/csvfiles', methods=('GET', 'POST', 'DELETE'))
def csvfiles():
  db = get_db()
  # return all csv_files
  if request.method == 'GET':
    csvfiles = query_db("SELECT * FROM csv_files")
    return jsonify(csvfiles)

  # create new csv file
  if request.method == 'POST':
    request_json = request.json
    name = request_json['name']
    raw_content = request_json['raw_content']
    # would probably be better to just parse into date stats and store those,
    # but here we are
    parsed_content = get_parsed_json_from_csv_string(raw_content)
    db.execute('INSERT INTO csv_files (name, raw_content, parsed_content) VALUES (?, ?, ?)', (name, raw_content, parsed_content))
    db.commit()
    return jsonify({'status':'success'})

  # delete csv file
  if request.method == 'DELETE':
    request_json = request.json
    #TODO: unsafe parse here
    id_to_delete = int(request_json['id'])
    db.execute('DELETE FROM csv_files WHERE id = ?', (id_to_delete,))
    db.commit()
    return jsonify({'status':'success'})

@bp.route('/csvfiles/stats/<int:id>')
def csvfilestats(id=None):
  if id is None:
    return jsonify({'status':'error'})

  csv_file = query_db('SELECT parsed_content FROM csv_files WHERE ID = ?', [id], one=True)
  date_stats = get_date_stats(csv_file)
  return jsonify({'status':'success', 'dates': date_stats})
