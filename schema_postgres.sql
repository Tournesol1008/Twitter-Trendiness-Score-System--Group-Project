CREATE SCHEMA milestone2
SET search_path TO 'milestone2';
CREATE TABLE IF NOT EXISTS Trendiness(
   CreationDate timestamp NOT NULL,
   Word varchar(255) NOT NULL,
   WordNum integer NOT NULL,
   TrendinessScore float NOT NULL);

