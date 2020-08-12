from flask import Flask, jsonify

# some dummy data for now
CSV_FILES = [
  {
    'name': 'test.csv',
    'parsed_guid': 'mv089j894ma1',
    'raw_guid': 'n5891m3k0d'
  },
  {
    'name': 'test2.csv',
    'parsed_guid': '0923mz89orh',
    'raw_guid': '09jcx978nmje'
  }
]

app = Flask(__name__)

@app.route('/csv_files')
def all_csv_files():
  return jsonify({
    'status': 'success',
    'csv_files': CSV_FILES
  })
