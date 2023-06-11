from User_data import host, user, password
import pymysql

pymysql.install_as_MySQLdb()



db = pymysql.connect(host=host,
                     user=user,
                     password=password)

with db:
    cursor = db.cursor()
    execute = cursor.execute('create database if not exists formula1;')
    execute = cursor.execute('use formula1;')
    #
    # execute = cursor.execute(
    #     'drop table if exists constructors, drivers, circuits, drivers_results, driver_standings;')

create_table_constructors =  """CREATE TABLE constructors(
constructorID VARCHAR(15) NOT NULL PRIMARY KEY,
name VARCHAR(50) NOT NULL);"""

create_table_drivers =  """CREATE TABLE drivers(
driverID VARCHAR(30) NOT NULL PRIMARY KEY,
driver VARCHAR(40) NOT NULL,
country VARCHAR(20) NOT NULL,
constructorID VARCHAR(50) NOT NULL,
FOREIGN KEY(constructorID) REFERENCES constructors(constructorID));"""

create_table_circuits =  """CREATE TABLE circuits(
circuitID VARCHAR(2) NOT NULL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
country VARCHAR(30) NOT NULL,
city VARCHAR(30) NOT NULL,
date DATE NOT NULL,
time TIME NOT NULL);"""

create_table_drivers_results = """CREATE TABLE drivers_results(
dr_id int AUTO_INCREMENT PRIMARY KEY,
driverID VARCHAR(30) NOT NULL,
position INT NOT NULL,
points INT NOT NULL,
constructorID VARCHAR(50) NOT NULL,
laps INT NOT NULL,
circuitID VARCHAR(2) NOT NULL,
FOREIGN KEY(circuitID) REFERENCES circuits(circuitID),
FOREIGN KEY(driverID) REFERENCES drivers(driverID),
CONSTRAINT unique_combination UNIQUE (circuitID, driverID));"""


create_table_driver_standings =  """CREATE TABLE driver_standings(
ds_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
points INT,
wins INT,
driverID VARCHAR(30) NOT NULL,
constructorID VARCHAR(50) NOT NULL,
FOREIGN KEY(constructorID) REFERENCES constructors(constructorID),
FOREIGN KEY(driverID) REFERENCES drivers(driverID));"""

create_table_constructor_standings =  """CREATE TABLE constructor_standings(
cs_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
points INT,
wins INT,
constructorID VARCHAR(50) NOT NULL,
FOREIGN KEY(constructorID) REFERENCES constructors(constructorID));"""


db = pymysql.connect(host=host,
                     user=user,
                     password=password,
                     database='formula1')

with db:
    cursor = db.cursor()
    execute = cursor.execute(create_table_constructors)
    execute = cursor.execute(create_table_drivers)
    execute = cursor.execute(create_table_circuits)
    execute = cursor.execute(create_table_drivers_results)
    execute = cursor.execute(create_table_driver_standings)
    execute = cursor.execute(create_table_constructor_standings)

cursor.close()

#update driver standings points
trigger1 ="""
CREATE TRIGGER update_points after insert on drivers_results for each row
BEGIN
	update driver_standings ds
    inner join (select driverID, sum(points) as total from drivers_results group by driverID) x on ds.driverID = x.driverID
    set ds.points = x.total;
END;"""

#update wins
trigger2 = """
CREATE TRIGGER wins after insert on drivers_results for each row
BEGIN
	update driver_standings ds
inner join (
	select driverID, sum(position = 1) as wins from drivers_results
	 WHERE circuitID REGEXP '^[0-9]+$'
	 group by driverID
) x on ds.driverID = x.driverID
SET ds.wins = x.wins;
END;"""


#update constructor standings points
trigger3 ="""
CREATE TRIGGER update_points2 after insert on drivers_results for each row
BEGIN
	update constructor_standings cs
    inner join (select constructorID, sum(points) as total from drivers_results group by constructorID) x on cs.constructorID = x.constructorID
    set cs.points = x.total;
END;"""

#update wins
trigger4 = """
CREATE TRIGGER wins2 after insert on drivers_results for each row
BEGIN
	update constructor_standings cs
inner join (
	select constructorID, sum(position = 1) as wins from drivers_results
	WHERE circuitID REGEXP '^[0-9]+$'
	group by constructorID
) x on cs.constructorID = x.constructorID
SET cs.wins = x.wins;
END;"""


db = pymysql.connect(host=host,
                     user=user,
                     password=password,
                     database='formula1')

with db:
    cursor = db.cursor()
    cursor.execute(trigger1)
    db.commit()
    cursor.execute(trigger2)
    db.commit()
    cursor.execute(trigger3)
    db.commit()
    cursor.execute(trigger4)
    db.commit()
cursor.close()


drivers = [('max_verstappen', 'Max Verstappen','Dutch','red_bull'),
           ('hamilton', 'Lewis Hamilton','British','mercedes'),
           ('alonso', 'Fernando Alonso','Spanish','aston_martin'),
           ('stroll', 'Lance Stroll','Canadian','aston_martin'),
           ('perez', 'Sergio Pérez','Mexican','red_bull'),
           ('norris', 'Lando Norris','British','mclaren'),
           ('hulkenberg', 'Nico Hülkenberg','German','haas'),
           ('piastri', 'Oscar Piastri','Australian','mclaren'),
           ('zhou', 'Guanyu Zhou','Chinese','alfa'),
           ('tsunoda', 'Yuki Tsunoda','Japanese','alphatauri'),
           ('bottas', 'Valtteri Bottas','Finnish','alfa'),
           ('sainz', 'Carlos Sainz','Spanish','ferrari'),
           ('gasly', 'Pierre Gasly','French','alpine'),
           ('ocon', 'Esteban Ocon','French','alpine'),
           ('de_vries', 'Nyck de Vries','Dutch','alphatauri'),
           ('sargeant', 'Logan Sargeant','American','williams'),
           ('kevin_magnussen', 'Kevin Magnussen','Danish','haas'),
           ('russell', 'George Russell','British','mercedes'),
           ('albon', 'Alexander Albon','Thai','williams'),
           ('leclerc', 'Charles Leclerc','Monegasque','ferrari')
]

constructors = [('red_bull','Red Bull'),
                ('mercedes','Mercedes'),
                ('aston_martin','Aston Martin'),
                ('mclaren','McLaren'),
                ('haas','Haas F1 Team'),
                ('alfa','Alfa Romeo'),
                ('alphatauri','AlphaTauri'),
                ('ferrari','Ferrari'),
                ('alpine','Alpine F1 Team'),
                ('williams','Williams')]

circuits = [(1,'Bahrain Grand Prix', 'Bahrain', 'Sakhir', '2023-3-5', '15:00:00'),
            (2,'Saudi Arabian Grand Prix', 'Saudi Arabia', 'Jeddah',
             '2023-3-19','17:00:00'),
            (3,'Australian Grand Prix', 'Australia', 'Melbourne',
             '2023-4-2','05:00:00'),
            (4, 'Azerbaijan Grand Prix', 'Azerbaijan', 'Baku', '2023-4-30', '11:00:00'),
            ('4s', 'Azerbaijan Grand Prix', 'Azerbaijan', 'Baku', '2023-4-30', '11:00:00'),
            (5, 'Miami Grand Prix', 'USA', 'Miami, FL', '2023-5-7', '19:30:0'),
            (6, 'Grand Prix de Monaco', 'Monaco', 'Monaco', '2023-5-28', '13:00:00'),
            (7, 'Gran Premio de Espana', 'Spain', 'Barcelona', '2023-6-4', '13:00:00'),
            (8, 'Grand Prix du Canada', 'Canada', 'Montreal', '2023-6-18', '18:00:00'),
            (9, 'Grosser Preis von Osterreich', 'Austria', 'Spielberg',
             '2023-7-2', '13:00:00'),
            (10, 'British Grand Prix', 'Great Britain', 'Silverstone',
             '2023-7-9', '14:00:00'),
            (11, 'Hungarian Grand Prix', 'Hungary', 'Budapest', '2023-7-23', '13:00:00'),
            (12, 'Belgian Grand Prix', 'Belgium', 'Spa', '2023-7-30', '13:00:00'),
            (13, 'Dutch Grand Prix', 'Netherlands', 'Zandvoort',
             '2023-8-27', '13:00:00'),
            (14, "Gran Premio d'Italia", 'Italy', 'Monza', '2023-9-3', '13:00:00'),
            (15, 'Singapore Grand Prix', 'Singapore', 'Singapore',
             '2023-9-17', '12:00:00'),
            (16, 'Japanese Grand Prix', 'Japan', 'Suzuka', '2023-9-24', '05:00:00'),
            (17, 'Qatar Grand Prix', 'Qatar', 'Losail', '2023-10-8', '14:00:00'),
            (18, 'United States Grand Prix', 'USA', 'Austin, TX',
             '2023-10-22', '19:00:00'),
            (19, 'Gran Premio de la Ciudad de Mexico', 'Mexico',
             'Mexico City', '2023-10-29', '20:00:00'),
            (20, 'Grande Premio de Sao Paulo', 'Brazil', 'Sao Paulo',
             '2023-11-5', '17:00:00'),
            (21, 'Las Vegas Grand Prix', 'USA', 'Las Vegas, NV',
             '2023-11-19', '06:00:00'),
            (22,'Abu Dhabi Grand Prix', 'United Arab Emirates', 'Abu Dhabi',
            '2023-11-26', '13:00:00')]

driver_standings = [('max_verstappen', 'red_bull'),
                    ('perez', 'red_bull'),
                    ('alonso', 'aston_martin'),
                    ('hamilton', 'mercedes'),
                    ('sainz', 'ferrari'),
                    ('stroll', 'aston_martin'),
                    ('russell', 'mercedes'),
                    ('norris', 'mclaren'),
                    ('hulkenberg', 'haas'),
                    ('leclerc', 'ferrari'),
                    ('bottas', 'alfa'),
                    ('ocon', 'alpine'),
                    ('piastri', 'mclaren'),
                    ('gasly', 'alpine'),
                    ('zhou', 'alfa'),
                    ('tsunoda', 'alphatauri'),
                    ('kevin_magnussen', 'haas'),
                    ('albon', 'williams'),
                    ('sargeant', 'williams'),
                    ('de_vries', 'alphatauri')]

constructor_standings = [('red_bull'),
                ('mercedes'),
                ('aston_martin'),
                ('mclaren'),
                ('haas'),
                ('alfa'),
                ('alphatauri'),
                ('ferrari'),
                ('alpine'),
                ('williams')]


db = pymysql.connect(host=host,
                     user=user,
                     password=password,
                     database='formula1')

with db:
    cursor = db.cursor()
    for constructor in constructors:
        cursor.execute(
            "insert into constructors(constructorID, name) values(%s, %s)",
            constructor)
        db.commit()

    for driver in drivers:
        cursor.execute(
            "insert into drivers(driverID,driver, country, constructorID) values(%s, %s, %s, %s)",
            driver)
        db.commit()

    for circuit in circuits:
        cursor.execute(
            "insert into circuits(circuitID, name, country, city, date, time) values(%s, %s, %s, %s, %s, %s)",
            circuit)
        db.commit()

    for ds in driver_standings:
        cursor.execute(
            "insert into driver_standings(driverID, constructorID) values(%s, %s)",ds)
        db.commit()

    for cs in constructor_standings:
        cursor.execute(
            "insert into constructor_standings(constructorID) values(%s)",cs)
        db.commit()

