CREATE TABLE IF NOT EXISTS users(
  phone VARCHAR(20) PRIMARY KEY  NOT NULL UNIQUE,
  name  VARCHAR(20) NOT NULL,
  description  VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS messages(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_phone VARCHAR(20),
  message TEXT,
  receipt_date DATETIME,
  processed INTEGER DEFAULT 0,
  FOREIGN KEY (user_phone) REFERENCES users(phone)
);

CREATE TABLE IF NOT EXISTS conversations(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_phone VARCHAR(20),
  status VARCHAR(20),
  FOREIGN KEY (user_phone) REFERENCES users(phone)
);