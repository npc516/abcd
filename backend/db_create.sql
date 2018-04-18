PRAGMA foreign_keys = ON;

CREATE TABLE Cat(
  cat_id INTEGER PRIMARY KEY,
  age INTEGER NOT NULL,
  breed TEXT NOT NULL,
  color TEXT NOT NULL,
  eye_color TEXT NOT NULL,
  hometown TEXT NOT NULL,
  name TEXT NOT NULL,
  photo_path TEXT NOT NULL,
  sex INTEGER NOT NULL,
  weight NUMERIC NOT NULL,
  buy_it_now INTEGER,
  ranking INTEGER,
  insurer_crn TEXT,
  sponsor_crn TEXT,
  policy_id INTEGER,
  sponsorship_id INTEGER,
  trainer_ssn TEXT REFERENCES Trainer(ssn),
  owner_email TEXT REFERENCES User(email) NOT NULL,
  audition_id INTEGER REFERENCES Audition(event_id),
  FOREIGN KEY(insurer_crn, policy_id) REFERENCES Policy(crn, policy_id),
  FOREIGN KEY(sponsor_crn, sponsorship_id) REFERENCES Sponsorship(crn, sponsorship_id)
);

CREATE TABLE User(
  email TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  password TEXT NOT NULL,
  bank_account TEXT NOT NULL,
  phone INTEGER NOT NULL,
  address TEXT NOT NULL
);

CREATE TABLE Company(
  crn TEXT PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE Audition(
  event_id INTEGER PRIMARY KEY,
  location TEXT NOT NULL,
  start_day INTEGER NOT NULL,
  entry_fee INTEGER NOT NULL,
  duration INTEGER NOT NULL
);

CREATE TABLE Tournament(
  tournament_id INTEGER PRIMARY KEY,
  start_day INTEGER NOT NULL,
  prize INTEGER NOT NULL
);

CREATE TABLE Match(
  event_id INTEGER PRIMARY KEY,
  location TEXT NOT NULL,
  day INTEGER NOT NULL,
  duration INTEGER NOT NULL,
  result INTEGER,
  tournament_id INTEGER REFERENCES Tournament(tournament_id) NOT NULL,
  cat1_id INTEGER REFERENCES Cat(cat_id) NOT NULL,
  cat2_id INTEGER REFERENCES Cat(cat_id) NOT NULL
);

CREATE TABLE Auction(
  auction_id INTEGER PRIMARY KEY,
  start_time INTEGER NOT NULL,
  start_price INTEGER NOT NULL,
  duration INTEGER NOT NULL,
  bid_increment INTEGER NOT NULL,
  cat_id INTEGER REFERENCES Cat(cat_id) NOT NULL
);

CREATE TABLE Bid(
  bid_id INTEGER PRIMARY KEY,
  price INTEGER NOT NULL,
  user_email TEXT REFERENCES User(email) NOT NULL,
  auction_id INTEGER REFERENCES Auction(auction_id) NOT NULL
);

CREATE TABLE Policy(
  policy_id INTEGER NOT NULL,
  duration INTEGER NOT NULL,
  price INTEGER NOT NULL,
  content TEXT NOT NULL,
  crn TEXT REFERENCES Company(crn) ON DELETE CASCADE NOT NULL,
  PRIMARY KEY (crn, policy_id)
);

CREATE TABLE Sponsorship(
  sponsorship_id INTEGER NOT NULL,
  duration INTEGER NOT NULL,
  payment INTEGER NOT NULL,
  content TEXT NOT NULL,
  crn TEXT REFERENCES Company(crn) ON DELETE CASCADE NOT NULL,
  PRIMARY KEY (crn, sponsorship_id)
);

CREATE TABLE Trainer(
  ssn TEXT PRIMARY KEY,
  license TEXT NOT NULL,
  name TEXT NOT NULL,
  routine TEXT NOT NULL,
  experience INTEGER,
  rating INTEGER REFERENCES RatingFee(rating)
);

CREATE TABLE RatingFee(
  rating INTEGER PRIMARY KEY,
  fee NUMERIC NOT NULL
);

CREATE TABLE DeliveryFee(
  destination TEXT NOT NULL,
  current_location TEXT NOT NULL,
  fee INTEGER NOT NULL,
  PRIMARY KEY (current_location, destination)
);

CREATE TABLE Comments(
  comment_id INTEGER PRIMARY KEY,
  content TEXT NOT NULL,
  user_email TEXT REFERENCES User(email) NOT NULL,
  cat_id INTEGER REFERENCES Cat(cat_id) NOT NULL
);

CREATE TABLE Delivery(
  delivery_id INTEGER PRIMARY KEY,
  eta INTEGER NOT NULL,
  condition TEXT NOT NULL,
  current_location TEXT NOT NULL,
  destination TEXT NOT NULL,
  cat_id INTEGER REFERENCES Cat(cat_id) NOT NULL,
  receiver_email TEXT REFERENCES User(email) NOT NULL,
  FOREIGN KEY (current_location, destination) REFERENCES DeliveryFee(current_location, destination)
);
