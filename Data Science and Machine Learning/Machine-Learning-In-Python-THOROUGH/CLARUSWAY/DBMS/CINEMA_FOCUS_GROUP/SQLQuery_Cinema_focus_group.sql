

CREATE TABLE City
(CityID INT IDENTITY(1,1),
CityName VARCHAR(100) NOT NULL,
PRIMARY KEY (CityID)
)
;



CREATE TABLE Cinema
(
CinemaID INT IDENTITY(100, 1),
CinemaName VARCHAR(100) NOT NULL,
CinemaOperator VARCHAR(100) NOT NULL,
CityID INT NOT NULL,
PRIMARY KEY (CinemaID),
FOREIGN KEY (CityID) REFERENCES City(CityID)
);


CREATE TABLE CinemaHall
(
CinemaID INT NOT NULL,
HallNo INT NOT NULL,
HallCapacity INT NOT NULL,
PRIMARY KEY (CinemaID, HallNo),
FOREIGN KEY (CinemaID) REFERENCES Cinema(CinemaID)
);


CREATE TABLE Film
(
FilmID INT IDENTITY(200, 1),
FilmTitle VARCHAR(100) NOT NULL,
FilmLength INT NOT NULL,
PRIMARY KEY (FilmID)
);



CREATE TABLE HallFilm
(
CinemaID INT  NOT NULL,
HallNo INT   NOT NULL,
FilmID INT  NOT NULL,
ShowTime DATETIME NOT NULL,
Audio VARCHAR(100) CHECK (Audio in ('Yes','No')),
Subtitle VARCHAR(50) CHECK (Subtitle in ('English','German', 'French', 'No Subtitle')),
PRIMARY KEY (CinemaID, HallNo, FilmID, ShowTime),
FOREIGN KEY (CinemaID, HallNo) REFERENCES CinemaHall(CinemaID, HallNo),
FOREIGN KEY (FilmID) REFERENCES Film(FilmID)
);


INSERT INTO City (CityName)
VALUES('Ankara'),
('Istanbul'),
('İzmir'),
('Erzincan');


INSERT INTO Cinema (CinemaName, CinemaOperator, CityID)
VALUES('Cinemax', 'Ali Güzel', 1),
('Arcadium', 'Mehmet Şen', 2),
('Cinevizyon', 'Ahmet Şen', 3),
('Cinevizyon2', 'Ayşe Gel', 1),
('armada', 'Aydın yeşil', 3);


INSERT INTO CinemaHall (CinemaID, HallNo, HallCapacity)
VALUES(100, 1, 20),
(100, 2, 25),
(100, 3, 30),
(101, 1, 50),
(101, 2, 60),
(101, 3, 70);


INSERT INTO Film (FilmTitle, FilmLength)
VALUES('Herşey Güzel Olacak', 120),
('Grandfather-1', 130),
('Grandfather-2', 140),
('Batman', 130),
('Superman', 130);


INSERT INTO HallFilm (CinemaID, HallNo, FilmID, ShowTime, Audio, Subtitle)
VALUES(100, 1, 200, '2020-08-05 10:00:00', 'No', 'English'),
(100, 2, 201, '2020-08-05 13:00:00', 'Yes', 'English'),
(100, 3, 202, '2020-08-05 16:00:00', 'No', 'English'),
(101, 1, 200, '2020-08-05 11:00:00', 'No', 'German'),
(101, 2, 201, '2020-08-05 14:00:00', 'Yes', 'German'),
(101, 3, 202, '2020-08-05 17:00:00', 'Yes', 'French');


select * from City
select * from Cinema
select * from CinemaHall
select * from Film
select * from HallFilm



CREATE FUNCTION check_volume()
RETURNS INT
AS
BEGIN
DECLARE @ret int
IF EXISTS(SELECT CityID, Count(CinemaID)
FROM Cinema
GROUP BY CityID
HAVING Count(CinemaID) > 3)
SELECT @ret = 1 ELSE SELECT @ret = 0;
RETURN @ret;
END;

ALTER TABLE Cinema
ADD CONSTRAINT square_volume CHECK(dbo.check_volume() = 0);





INSERT INTO City (CityName)
VALUES('Ankara'),
('Istanbul'),
('Izmir'),
('Erzincan');

select * from City

INSERT INTO Cinema (CinemaName, CinemaOperator, CityID)
VALUES('Cinemax', 'Ali Güzel', 1),
('Arcadium', 'Mehmet Sen', 2),
('Cinevizyon', 'Ahmet Sen', 3),
('Cinevizyon2', 'Ayse Gel', 1),
('armada', 'Aydin Yesil', 3);

INSERT INTO Cinema (CinemaName, CinemaOperator, CityID)
VALUES('Cinemax2', 'Veli Sahin', 1)

INSERT INTO Cinema (CinemaName, CinemaOperator, CityID)
VALUES('Cinemax3', 'Cem Gedik', 1)


select * from Cinema

INSERT INTO CinemaHall (CinemaID, HallNo, HallCapacity)
VALUES(100, 1, 20),
(100, 2, 25),
(100, 3, 30),
(101, 1, 50),
(101, 2, 60),
(101, 3, 70);

select * from CinemaHall

INSERT INTO Film (FilmTitle, FilmLength)
VALUES('Herþey Güzel Olacak', 120),
('Grandfather-1', 130),
('Grandfather-2', 140),
('Batman', 130),
('Superman', 130);


INSERT INTO HallFilm (CinemaID, HallNo, FilmID, ShowTime, Audio, Subtitle)
VALUES(100, 1, 200, '2020-08-05 10:00:00', 'Yes', 'English'),
(100, 2, 201, '2020-08-05 13:00:00', 'Yes', 'English'),
(100, 3, 202, '2020-08-05 16:00:00', 'No', 'English'),
(101, 1, 200, '2020-08-05 11:00:00', 'No', 'German'),
(101, 2, 201, '2020-08-05 14:00:00', 'Yes', 'German'),
(101, 3, 202, '2020-08-05 17:00:00', 'Yes', 'French');

INSERT INTO HallFilm (CinemaID, HallNo, FilmID, ShowTime, Audio, Subtitle)
VALUES(102, 1, 200, '2020-08-05 10:00:00', 'Yes', 'No Subtitle')

INSERT INTO HallFilm (CinemaID, HallNo, FilmID, ShowTime, Audio, Subtitle)
VALUES(100, 1, 200, '2020-08-05 13:00:00', 'Yes', 'No Subtitle'),
(100, 1, 200, '2020-08-05 16:00:00', 'Yes', 'English')


INSERT INTO HallFilm (CinemaID, HallNo, FilmID, ShowTime, Audio, Subtitle)
VALUES(100, 1, 200, '2020-08-05 19:00:00', 'Yes', 'English')



