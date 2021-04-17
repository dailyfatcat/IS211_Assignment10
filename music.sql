
/*******************************************************************************
   Assignment Part 1 Music Database

Modeling music artists, the albums they create and the songs that appear on those albums

A set of relational tables that will sufficiently model what is described above.
Submit a file named music.sql, with SQL CREATE queries that will create the tables with the proper schema of your model.
********************************************************************************/

CREATE TABLE artist
( id INTEGER PRIMARY KEY ASC,
    name CHAR(100),
);

CREATE TABLE album
( id INTEGER PRIMARY KEY ASC,
    name CHAR(100),
    artist CHAR(100)
);

CREATE TABLE song
( id INTEGER PRIMARY KEY ASC,
    name CHAR(100),
    track INTEGER,
    length INTEGER,
    album CHAR(100)
);
