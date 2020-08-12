DROP TABLE IF EXISTS csv_files;

CREATE TABLE csv_files (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  raw_content TEXT NOT NULL,
  parsed_content TEXT
)
