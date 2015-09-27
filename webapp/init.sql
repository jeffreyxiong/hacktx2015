DROP TABLE IF EXISTS video;
CREATE TABLE video (
  vID INTEGER PRIMARY KEY UNIQUE NOT NULL,
  winner INTEGER,
  loser INTEGER,
  url TEXT,
  tournament TEXT,
  year INTEGER,
  FOREIGN KEY(winner) REFERENCES player(pID),
  FOREIGN KEY(loser) REFERENCES player(pID)
);

DROP TABLE IF EXISTS game;
CREATE TABLE game (
  gID INTEGER PRIMARY KEY UNIQUE NOT NULL,
  vID INTEGER,
  winner INTEGER,
  loser INTEGER,
  stage STRING,
  match INTEGER,
  FOREIGN KEY(vID) REFERENCES video(vID),
  FOREIGN KEY(winner) REFERENCES player(pID),
  FOREIGN KEY(loser) REFERENCES player(pID)
);

DROP TABLE IF EXISTS player;
CREATE TABLE player (
  pID INTEGER PRIMARY KEY UNIQUE NOT NULL,
  name TEXT
);

DROP TABLE IF EXISTS playerGameCharacter;
CREATE TABLE playerGameCharacter (
  game INTEGER,
  player INTEGER,
  character STRING,
  FOREIGN KEY(game) REFERENCES game(gID),
  FOREIGN KEY(player) REFERENCES player(pID),
  PRIMARY KEY (game, player, character)
);