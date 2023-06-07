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
FOREIGN KEY(driverID) REFERENCES drivers(driverID));"""

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
	select driverID, sum(position = 1) as wins from drivers_results group by driverID
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
	select constructorID, sum(position = 1) as wins from drivers_results group by constructorID
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