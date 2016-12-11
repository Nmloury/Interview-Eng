/* First Query */

-- SELECT FirstName, LastName
-- FROM customer
-- LIMIT 10;

-- What are the genres in the database?

-- SELECT *
-- FROM genre
-- LIMIT 1000;

-- What are the customer names that are from California?

-- SELECT FirstName, LastName, State
-- FROM customer
-- WHERE State = 'CA';

-- How many songs are longer than 10 minutes
-- SELECT COUNT(*)
-- FROM TRACK
-- WHERE Milliseconds > 600000;
-- 260

-- How many invoices between
-- SELECT COUNT(*)
-- FROM Invoice
-- WHERE InvoiceDate BETWEEN '2010-01-01'
--     AND '2010-02-01'
-- 7

-- How many tracks have a null composer?
-- SELECT COUNT(*)
-- FROM TRACK
-- WHERE Composer IS NULL;
-- 978

-- How Many distinct album title are there?
-- SELECT COUNT(DISTINCT Title)
-- FROM ALBUM;
-- 347

-- How Many distinct album title are there?
-- SELECT COUNT(DISTINCT AlbumId)
-- FROM ALBUM;
-- 348

-- What are the 5 longest songs?
-- SELECT Name, AlbumId, Milliseconds/1000./60. AS Minutes
-- FROM TRACK
-- ORDER BY Milliseconds DESC
-- LIMIT 5;

-- Name|AlbumId|Minutes
-- Occupation / Precipice|227|88.1158833333333
-- Through a Looking Glass|229|84.8139666666667
-- Greetings from Earth, Pt. 1|253|49.3382166666667
-- The Man With Nine Lives|253|49.2833
-- Battlestar Galactica, Pt. 2|253|49.2680166666667

-- Songs with R.E.M.
-- SELECT *
-- FROM ARTIST
-- WHERE Name LIKE '%R.E.M.%';

-- ArtistId|Name
-- 122|R.E.M. Feat. Kate Pearson
-- 123|R.E.M. Feat. KRS-One
-- 124|R.E.M.

-- How many 'Love' song are there?
-- SELECT COUNT(*)
-- FROM Track
-- WHERE (Name LIKE '%love%' AND Name NOT LIKE '%glove%')
--     OR Name LIKE '%loving%';
-- 114

-- Create a new table
-- CREATE TABLE IF NOT EXISTS ds_songs(
--     song_id INTEGER,
--     genre VARCHAR(64),
--     artist VARCHAR(64),
--     song_name VARCHAR(128),
--     track_length FLOAT(2)
-- );

-- Insert values into the new table
-- INSERT INTO ds_songs
--     (song_id, genre, artist, song_name, track_length)
--     VALUES (01, 'R&B', 'Vrushank Vora', 'Radical Transparency', 2.6);

-- Drop Table
-- DROP TABLE IF EXISTS ds_songs;

-- How many tracks are rock or alternative?
-- SELECT COUNT(*)
-- FROM track
-- JOIN genre
-- on track.genreid = genre.genreid
-- WHERE genre.name IN ('Rock', 'Alternative',
--                         'Rock And Roll', 'Alternative &');
-- 1337

-- How many tracks are performed by R.E.M. excluding collaborators?
-- SELECT COUNT(*)
-- FROM track
-- JOIN album
-- ON track.albumid = album.albumid
-- JOIN artist
-- ON album.artistid = artist.artistid
-- WHERE artist.name = 'R.E.M.';
-- 41

-- How many tracks are performed by R.E.M. with collaborators?
-- SELECT COUNT(*)
-- FROM track
-- JOIN album
-- ON track.albumid = album.albumid
-- JOIN artist
-- ON album.artistid = artist.artistid
-- WHERE artist.name LIKE '%R.E.M.%'
--     AND artist.name != 'R.E.M.';
-- 11

-- What are other interesting queries can you create that join 2 tables?

-- What is the most popular media type by total sales?
-- SELECT type, SUM(total)
-- FROM (
--     SELECT mediatype.name AS type, invoiceline.unitprice * invoiceline.quantity AS Total
--     FROM invoiceline
--     JOIN track
--     ON invoiceline.trackid = track.trackid
--     JOIN mediatype
--     ON track.mediatypeid = mediatype.mediatypeid
-- )
-- GROUP BY type;

-- What was the sales total for January 2010?
-- SELECT SUM(Total) AS sales_total
-- FROM invoice
-- WHERE invoicedate BETWEEN '2010-01-%';
-- 52.62

-- What is the average length of a song by R.E.M.?
-- SELECT AVG(t.Milliseconds)/1000./60. AS Minutes
-- FROM track AS t
-- JOIN album AS al
-- ON t.albumid = al.albumid
-- JOIN artist AS ar
-- ON al.artistid = ar.artistid
-- WHERE ar.name LIKE '%R.E.M.%';

-- 4.04347884615385

-- Which Artists Have the Most Tracks?
-- SELECT ar.name, COUNT(*) AS tracks
-- FROM track AS t
-- JOIN album AS al
--     ON t.albumid = al.albumid
-- JOIN artist AS ar
--     ON al.artistid = ar.artistid
-- GROUP BY ar.name
-- ORDER BY tracks DESC
-- LIMIT 25;

-- Name         tracks
-- -----------  ----------
-- Iron Maiden  213
-- U2           135
-- Led Zeppeli  114
-- Metallica    112
-- Deep Purple  92
-- Lost         92
-- Pearl Jam    67
-- Lenny Kravi  57
-- Various Art  56
-- The Office   53
-- Faith No Mo  52
-- Van Halen    52
-- Os Paralama  49
-- Eric Clapto  48
-- Red Hot Chi  48
-- Queen        45
-- Foo Fighter  44
-- Guns N' Ros  42
-- R.E.M.       41
-- The Rolling  41
-- Audioslave   40
-- Creedence C  40
-- Titãs       38
-- Miles Davis  37
-- Chico Scien  36

-- Which Albums Have the Longest Playing Time?
SELECT al.title, SUM(t.Milliseconds/1000./60.) AS playing_time
FROM track AS t
JOIN album AS al
    ON t.albumid = al.albumid
GROUP BY al.title
ORDER BY playing_time DESC
LIMIT 25;

-- Title           playing_time
-- --------------  ------------
-- Lost, Season 3  1177.7597
-- Battlestar Gal  1170.2297333
-- Lost, Season 1  1080.9156
-- Lost, Season 2  1054.8271833
-- Heroes, Season  996.3378
-- Battlestar Gal  879.78401666
-- LOST, Season 4  657.80721666
-- The Office, Se  638.61825
-- The Office, Se  477.2701
-- Greatest Hits   251.09551666
-- Unplugged       135.22126666
-- The Office, Se  132.9194
-- Minha Historia  131.26071666
-- Live After Dea  97.130933333
-- Instant Karma:  85.581433333
-- A Matter of Li  79.253983333
-- A-Sides         79.200483333
-- Load            78.97675
-- BBC Sessions [  78.318466666
-- Pure Cult: The  77.545666666
-- Up An' Atom     77.283516666
-- The Essential   76.626166666
-- My Generation   76.3344
-- Greatest Kiss   76.250416666
-- Jorge Ben Jor   76.18775

-- Which Albums Have the Longest Playing Time (music only)?
SELECT ar.name, al.title, SUM(t.Milliseconds/1000./60.) AS playing_time
FROM track AS t
JOIN album AS al
    ON t.albumid = al.albumid
JOIN mediatype AS m
    ON t.mediatypeid = m.mediatypeid
JOIN artist AS ar
    ON al.artistid = ar.artistid
WHERE m.name LIKE '%audio%'
GROUP BY ar.name, al.title
ORDER BY playing_time DESC
LIMIT 25;

-- Title          playing_time
-- -------------  ----------------
-- Greatest Hits  251.095516666667
-- Unplugged      135.221266666667
-- Minha Histori  131.260716666667
-- Live After De  97.1309333333333
-- Instant Karma  85.5814333333333
-- A Matter of L  79.2539833333333
-- A-Sides        79.2004833333333
-- Load           78.97675
-- BBC Sessions   78.3184666666667
-- Pure Cult: Th  77.5456666666667
-- Up An' Atom    77.2835166666667
-- The Essential  76.6261666666667
-- My Generation  76.3344
-- Greatest Kiss  76.2504166666667
-- Jorge Ben Jor  76.18775
-- Use Your Illu  76.1222
-- ReLoad         76.1050666666667
-- Greatest Hits  75.9756833333333
-- Use Your Illu  75.9535166666667
-- Retrospective  75.8115666666667
-- My Way: The B  75.6656833333333
-- Acústico MTV  75.3966
-- St. Anger      75.1176166666667
-- Supernatural   75.0091833333333
-- Chronicle, Vo  74.9969666666667





