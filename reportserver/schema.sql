DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

DROP TABLE IF EXISTS report;

CREATE TABLE report (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    participant TEXT NOT NULL,
    completedTimeStamp INTEGER NOT NULL,
    completedDate TEXT NOT NULL,
    clientMD5 TEXT NOT NULL
);

INSERT INTO user (username, password) VALUES ('admin', 'apiaprilfools');
